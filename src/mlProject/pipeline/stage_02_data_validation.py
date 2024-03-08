from mlProject.config.configuration import ConfigurationManager
from mlProject.components.data_validation import DataValidation
from mlProject import logger


STAGE_NAME = "Data Validation Stage"

class DataValidationTrainingPipeline:
    def __init__(self):
        pass
    def main(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(config=data_validation_config)
        data_validation.validate_all_columns()
    




if __name__ == '__main__':
    try:
        #Log start of the data validation stage
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