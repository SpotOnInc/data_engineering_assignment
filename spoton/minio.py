import os
import boto3

from config import Spoton
from aws import Aws

from botocore.client import Config


class Minio:
    def __init__(self):
        self.aws = Aws()

    @property
    def s3_bucket(self):
        return "spotondata"

    def create_minio_bucket(self):
        self.aws.create_bucket(self.s3_bucket)

    def upload_to_minio(self):
        self.aws.upload_data(Spoton.target_data_sets, self.s3_bucket)

    # def _get_s3_client(self):
    #     return boto3.resource(
    #         "s3",
    #         endpoint_url="http://minio-s3:9000",
    #         aws_access_key_id=os.getenv("MINIO_ROOT_USER"),
    #         aws_secret_access_key=os.getenv("MINIO_ROOT_PASSWORD"),
    #         config=Config(signature_version="s3v4"),
    #         region_name="us-east-1",
    #     )
    #
    # def create_bucket(self):
    #     # S3 will throw an exception if the bucket already exists. Make it idempotent.
    #     try:
    #         self.s3.create_bucket(Bucket=self.s3_bucket)
    #     except:
    #         pass
    #
    # def upload_data_sets(self):
    #     for dataset in Spoton.target_data_sets:
    #         self.s3.Bucket(self.s3_bucket).upload_file(
    #             f"{Spoton.unzipped_target_data}/{dataset}", dataset
    #         )
