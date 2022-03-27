import os
import boto3

from config import Spoton

from botocore.client import Config


class Aws:
    def __init__(self):
        self.s3 = self._get_s3_client()

    @property
    def s3_bucket(self):
        return "spotondata"

    def _get_s3_client(self):
        return boto3.resource(
            "s3",
            endpoint_url="http://minio-s3:9000",
            aws_access_key_id=os.getenv("MINIO_ROOT_USER"),
            aws_secret_access_key=os.getenv("MINIO_ROOT_PASSWORD"),
            config=Config(signature_version="s3v4"),
            region_name="us-east-1",
        )

    def create_bucket(self, bucket_name):
        # S3 will throw an exception if the bucket already exists. Make it idempotent.
        try:
            self.s3.create_bucket(Bucket=bucket_name)
        except:
            pass

    def upload_data(self, datasets, bucket):
        for dataset in datasets:
            self.s3.Bucket(bucket).upload_file(
                f"{Spoton.unzipped_target_data}/{dataset}", dataset
            )
