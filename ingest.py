from kaggle.api.kaggle_api_extended import KaggleApi
from kaggle.api_client import ApiClient
from zipfile import ZipFile

api = KaggleApi(ApiClient())
api.authenticate()

print("Downloading files...")

api.dataset_download_files("olistbr/brazilian-ecommerce")

print("Files downloaded...")

zf = ZipFile("./brazilian-ecommerce.zip")
zf.extractall("brazilian-ecommerce")
zf.close()
