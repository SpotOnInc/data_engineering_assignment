import boto3
from botocore.client import Config

import os


# TODO: get at least some of these from the environment
BUCKET_NAME = "brazilian-ecommerce"
S3_ACCESS_KEY_ID = "minioadmin"
S3_SECRET_ACCESS_KEY = "minioadmin"
MINIO_HOST = "http://minio-s3:9000"

s3 = boto3.resource(
    "s3",
    endpoint_url=MINIO_HOST,
    aws_access_key_id=S3_ACCESS_KEY_ID,
    aws_secret_access_key=S3_SECRET_ACCESS_KEY,
    config=Config(signature_version="s3v4"),
    region_name="us-east-1",
)

found = s3.Bucket(BUCKET_NAME) in s3.buckets.all()

if not found:
    s3.create_bucket(Bucket=BUCKET_NAME)
    print(f"{BUCKET_NAME} bucket created")
else:
    print(f"{BUCKET_NAME} bucket already exists")

upload_list = []

for root, dirs, files in os.walk(BUCKET_NAME):
    for file in files:
        if file.endswith("csv"):
            print(file)
            upload_list.append(file)

print("files to be uploaded: ", upload_list)

for f in upload_list:
    try:
        print("Upload: ", f)
        s3.Bucket(BUCKET_NAME).upload_file(f"{BUCKET_NAME}/{{}}".format(f), f)
    except Exception as e:
        print("Upload: ", f, "failed")
        print(e)
