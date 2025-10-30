
import zipfile
import urllib.request as request
from src.datascience import logger   
import zipfile
import os
from src.datascience.entity.config_entity import DataIngestionConfig

class DataIngestion: 
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_data(self):
        if not os.path.exists(self.config.local_data_file):

            filename, headers = request.urlretrieve(url = self.config.source_URL,filename=self.config.local_data_file)
            logger.info(f"Downloading data from {self.config.source_URL} to {self.config.local_data_file}")
            logger.info("Download completed.")

    def extract_zip(self):
        """Extracts the downloaded zip file to the specified directory.
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)
        logger.info(f"Extracted zip file {self.config.local_data_file} to {unzip_path}")
