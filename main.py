from src.datascience import logger
logger.info("Datascience package initialized.")

from src.datascience.pipeline.data_ingestion_pipline import DataIngestionTrainingPipeline 
from src.datascience.pipeline.data_validation_pipline import DataValidationTrainingPipeline 


STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.initiate_data_ingestion()
    logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<<\n\n")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data Validation Stage"

try:
    logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<")
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<<\n\n")  
except Exception as e:
    logger.exception(e)
    raise e     

