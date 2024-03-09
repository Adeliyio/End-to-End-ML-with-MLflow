from mlProject.constants import *
from mlProject.utils.common import read_yaml,create_directories
from mlProject.entity.config_entity   import (DataIngestionConfig,
                                              DataValidationConfig,
                                              DataTransformationConfig)


# Class for managing configuration settings
class ConfigurationManager:
    def __init__(
        self,
        config_filepath=CONFIG_FILE_PATH,  # Path to the configuration file
        params_filepath=PARAMS_FILE_PATH,  # Path to the parameters file
        schema_filepath=SCHEMA_FILE_PATH # Path to the schema file
    ):
        # Initialize the configuration and parameters
        self.config = read_yaml(config_filepath)  # Read configuration from YAML file
        self.params = read_yaml(params_filepath)  # Read parameters from YAML file
        self.schema = read_yaml(schema_filepath)

        # Create necessary directories
        create_directories([self.config.artifacts_root])

    # Method to retrieve data ingestion configuration
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        # Get data ingestion configuration from the main configuration
        config = self.config.data_ingestion

        # Create directories specified in the configuration
        create_directories([config.root_dir])

        # Create DataIngestionConfig object using the retrieved configuration
        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,              # Root directory for data ingestion
            source_URL=config.source_URL,          # URL for data source
            local_data_file=config.local_data_file,# Path to local data file
            unzip_dir=config.unzip_dir            # Directory for extracted data
        )

        return data_ingestion_config
    



    def get_data_validation_config(self) -> DataValidationConfig:
        """
        Retrieves the data validation configuration.

        Returns:
        - DataValidationConfig: The data validation configuration object.
        """
        # Access data validation configuration and schema from main configuration
        config = self.config.data_validation
        schema = self.schema.COLUMNS

        # Create necessary directories for data validation
        create_directories([config.root_dir])

        # Create DataValidationConfig object with extracted parameters
        data_validation_config = DataValidationConfig(
            root_dir=config.root_dir,
            STATUS_FILE=config.STATUS_FILE,
            unzip_data_dir=config.unzip_data_dir,
            all_schema=schema,
        )

        return data_validation_config


    def get_data_transformation_config(self) -> DataTransformationConfig:
        config = self.config.data_transformation

        create_directories([config.root_dir])

        data_transformation_config = DataTransformationConfig(
            root_dir=config.root_dir,
            data_path=config.data_path,
        )

        return data_transformation_config 