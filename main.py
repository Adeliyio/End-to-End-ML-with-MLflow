from src.mlProject import logger
from mlProject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from mlProject.pipeline.stage_02_data_validation import DataValidationTrainingPipeline

STAGE_NAME = "Data Ingestion stage"

try:
    # Log start of the data ingestion stage
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")

    # Instantiate the DataIngestionTrainingPipeline object
    pipeline = DataIngestionTrainingPipeline()

    # Execute the main method to run the data ingestion pipeline
    pipeline.main()

    # Log completion of the data ingestion stage
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        # Log any exceptions that occur during the pipeline execution
        logger.exception(e)
        raise e  # Re-raise the exception for further handling



STAGE_NAME = "Data Validation Stage"

try:
    # Log start of the data validation stage
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")

    # Instantiate the DataValidationTrainingPipeline object
    pipeline = DataValidationTrainingPipeline()

    # Execute the main method to run the data validation pipeline
    pipeline.main()

    # Log completion of the data validation stage
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    # Log any exceptions that occur during the pipeline execution
    logger.exception(e)
    raise e  # Re-raise the exception for further handling
