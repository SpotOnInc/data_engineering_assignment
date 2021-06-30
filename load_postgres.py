import os
from io import BytesIO
import boto3
import sqlalchemy as sa
import pandas as pd

# TODO: get at least some of these from the environment
BUCKET_NAME = "brazilian-ecommerce"
S3_ACCESS_KEY_ID = "minioadmin"
S3_SECRET_ACCESS_KEY = "minioadmin"
MINIO_HOST = "http://minio-s3:9000"
DB_URI = 'postgresql://postgres:postgres@db:5432/postgres' 

s3 = boto3.client(
    "s3",
    endpoint_url=MINIO_HOST,
    aws_access_key_id=S3_ACCESS_KEY_ID,
    aws_secret_access_key=S3_SECRET_ACCESS_KEY,
    region_name="us-east-1",
)

engine = sa.create_engine(DB_URI)

file_dict = s3.list_objects(Bucket="brazilian-ecommerce")

for f in file_dict['Contents']:
	file_name = f['Key']
	table_name = file_name[:-4]
	with BytesIO() as f:
		s3.download_fileobj(BUCKET_NAME, file_name, f)
		f.seek(0)
		df = pd.read_csv(f)
		print(df)
	df.to_sql(table_name, engine, if_exists='replace', index=False,)
		
