from src.DataScienceProject import logger
from src.DataScienceProject.pipeline.data_ingestion_pipeline   import DataIngestionTranningPipeline


logger.info("Starting the main application...")

STAGE_NAME="Data Ingestion Stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = DataIngestionTranningPipeline()
    obj.initiate_data_ingestion()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(f"Error in stage {STAGE_NAME}: {e}")
    raise e

