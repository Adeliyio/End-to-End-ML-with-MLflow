
import os
from mlProject import logger
from sklearn.model_selection import train_test_split
import pandas as pd
from mlProject.entity.config_entity import DataTransformationConfig


class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        """
        Constructor for DataTransformation class.

        Args:
            config (DataTransformationConfig): Configuration object for data transformation.
        """
        self.config = config

        # NB: We can add several data transformation techniques such as scalar, PCA, and all.
        # We can perform all kinds of EDA in the ML cycle here before passing the data to the model,
        # but since I'm using clean data, I'll proceed.

    def train_test_split(self):
        """
        Splits the data into training and test sets.
        """
        # Read data from CSV file
        data = pd.read_csv(self.config.data_path)

        # Split the data into training and test sets (0.75, 0.25).
        train, test = train_test_split(data, test_size=0.25, random_state=42)

        # Save the split data to CSV files.
        train.to_csv(os.path.join(self.config.root_dir, "train.csv"), index=False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"), index=False)

        # Log information about the split data.
        logger = logging.getLogger(__name__)
        logger.info("Split data into training and test sets")
        logger.info(f"Training data shape: {train.shape}")
        logger.info(f"Test data shape: {test.shape}")

        # Print information about the split data.
        print(f"Training data shape: {train.shape}")
        print(f"Test data shape: {test.shape}")
