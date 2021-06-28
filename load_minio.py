import boto3
from botocore.client import Config
from minio import Minio
from minio.error import S3Error
import os

s3 = boto3.resource('s3',
                    endpoint_url='http://localhost:9000',
                    aws_access_key_id='minioadmin',
                    aws_secret_access_key='minioadmin',
                    config=Config(signature_version='s3v4'),
                    region_name='us-east-1')

found = s3.Bucket('brazilian-ecommerce') in s3.buckets.all() 
if not found:
	client.make_bucket('brazillian_ecommerce')
	print('brazilian-ecommerce bucket created')
else:
	print('brazillian-ecommerce bucket already exists')

upload_list = []
for root, dirs, files in os.walk('brazilian-ecommerce'):
	for file in files:
		if file.endswith('csv'):
			print(file)
			upload_list.append(file)
print('files to be uploaded: ', upload_list)

for f in upload_list:
	try:
		print('Upload: ', f)
		s3.Bucket('brazilian-ecommerce').upload_file('brazilian-ecommerce/{}'.format(f), f)
	except Exception as e:
		print('Upload: ', f, 'failed')
		print(e)
