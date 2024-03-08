from mlProject import logger
from mlProject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from mlProject.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from mlProject.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline

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



STAGE_NAME = "Data Transformation Stage"

try:
    # Log start of the stage
    logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<")
    # Initialize DataTransformationTrainingPipeline object
    obj = DataTransformationTrainingPipeline()
    # Execute main method of the pipeline
    obj.main()
    # Log completion of the stage
    logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        # Log any exceptions that occur during the stage
        logger.exception(e)
        # Re-raise the exception for further handling
        raise e

