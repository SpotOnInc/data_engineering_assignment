import zipfile
from kaggle.api.kaggle_api_extended import KaggleApi
from config import Spoton


class Kaggle:
    def __init__(self):
        self.kaggle_api = KaggleApi()

    def kaggle_authenticate(self):
        try:
            self.kaggle_api.authenticate()
        except:
            exit()

    def download_dataset(self):
        self.kaggle_api.dataset_download_files(
            "olistbr/brazilian-ecommerce", path=Spoton.kaggle_target_data
        )

    def unzip_dataset(self):
        with zipfile.ZipFile(
            "./spoton/kaggle_data/brazilian-ecommerce.zip", "r"
        ) as zip_file:
            zip_file.extractall(
                path=Spoton.unzipped_target_data, members=Spoton.target_data_sets
            )
