# Create Entity (the return type of any function)
from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    """Configuration class for data ingestion."""

    root_dir: Path        # Root directory where data will be stored
    source_URL: str       # URL from where the data will be downloaded
    local_data_file: Path  # Path to the local data file
    unzip_dir: Path       # Directory where the data will be extracted after downloading


@dataclass(frozen=True)
class DataValidationConfig:
    """Configuration class for data ingestion."""

    root_dir: Path        # Root directory where data will be stored
    STATUS_FILE: str
    unzip_data_dir: Path
    all_schema: dict


# Data Transformation configuration entity
@dataclass(frozen=True)
class DataTransformationConfig:
    """
    Configuration class for Data Transformation.

    Attributes:
    - root_dir (Path): The root directory for data transformation.
    - data_path (Path): The path to the data.
    """
    root_dir: Path
    data_path: Path
