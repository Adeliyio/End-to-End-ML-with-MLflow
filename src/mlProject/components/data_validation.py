import os
from mlProject import logger
from mlProject.entity.config_entity import DataValidationConfig
import pandas as pd

#update component

class DataValidation:
    def __init__(self, config: DataValidationConfig):
        """
        Initializes the DataValidation object with a configuration.

        Args:
        - config (DataValidationConfig): The configuration for data validation.
        """
        self.config = config

    def validate_all_columns(self) -> bool:
        """
        Validates all columns in the data against the provided schema.

        Returns:
        - bool: True if all columns are validated against the schema, False otherwise.
        """
        try:
            validation_status = None

            # Read the data from CSV
            data = pd.read_csv(self.config.unzip_data_dir)
            all_cols = list(data.columns)

            # Get all columns specified in the schema
            all_schema = self.config.all_schema.keys()

            # Loop through each column
            for col in all_cols:
                if col not in all_schema:
                    # Column not found in schema, set validation status to False
                    validation_status = False
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation status: {validation_status}")
                else:
                    # Column found in schema, set validation status to True
                    validation_status = True
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation status: {validation_status}")

            return validation_status
        
        except Exception as e:
            # Raise any exceptions that occur during validation
            raise e
