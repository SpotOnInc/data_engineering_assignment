import time

from config import Spoton
from ingest import Ingest
from minio import Minio
from spoton_kaggle import Kaggle


def download_data_from_kaggle():
    kaggle = Kaggle()
    kaggle.kaggle_authenticate()
    kaggle.download_dataset()
    kaggle.unzip_dataset()


def load_data_into_s3():
    minio = Minio()
    minio.create_minio_bucket()
    minio.upload_to_minio()


def s3_to_psql():
    ingest = Ingest()
    ingest.pull_from_s3()
    ingest.s3_to_db()


if __name__ == "__main__":
    # Give DB enough time to spin up
    time.sleep(2)

    download_data_from_kaggle()
    load_data_into_s3()
    s3_to_psql()
