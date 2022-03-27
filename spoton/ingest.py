import os
from tempfile import NamedTemporaryFile

from sqlalchemy import create_engine
import pandas as pd

from aws import Aws
from config import Spoton


class Ingest:
    def __init__(self):
        self.engine = create_engine(os.getenv("DATABASE_URL"))
        self.aws = Aws()

    def pull_from_s3(self):
        for bucket_object in self.aws.s3.Bucket("spotondata").objects.all():
            self.s3_to_db(bucket_object)

    def s3_to_db(self, bucket_object):
        table_name = bucket_object.key.split(".", 1)[0]
        with NamedTemporaryFile("wb") as temp_file:
            self.aws.s3.Bucket("spotondata").download_file(
                bucket_object.key, temp_file.name
            )
            df = pd.read_csv(temp_file.name)
            df.to_sql(table_name, self.engine, if_exists="replace", index=False)
