import os
import urllib.request as request
import zipfile
from mlProject import logger
from mlProject.utils.common import get_size
from pathlib import Path
from mlProject.entity.config_entity import (DataIngestionConfig,
                                            DataValidationConfig)


# Update Component
class DataIngestion:
    """
    A class for handling data ingestion tasks such as downloading and extracting files.

    Attributes:
        config (DataIngestionConfig): Configuration object containing necessary parameters.
    """

    def __init__(self, config: DataIngestionConfig):
        """
        Initializes DataIngestion class with provided configuration.

        Args:
            config (DataIngestionConfig): Configuration object containing necessary parameters.
        """
        self.config = config

    def download_file(self):
        """
        Downloads the file specified in the configuration if it doesn't already exist locally.

        If the file already exists locally, it logs its size; otherwise, it downloads the file from the
        specified URL and logs download information.
        """
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url=self.config.source_URL,
                filename=self.config.local_data_file
            )
            logger.info(f"{filename} downloaded with the following info:\n{headers}")
        else:
            logger.info(f"File already exists with size: {get_size(Path(self.config.local_data_file))}")

    def extract_zip_file(self):
        """
        Extracts the contents of a zip file to the specified directory.

        If the directory doesn't exist, it creates it. Then, it extracts the contents of the zip file
        specified in the configuration to the directory.
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)
