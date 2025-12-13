from src.DataScienceProject.config.configuration import ConfigurationManager
from src.DataScienceProject.components.data_transformation import Datatransformation
from src.DataScienceProject import logger
STAGE_NAME="Data transformation Stage"

class DatatransformationTranningPipeline:
    def __init__(self):
        pass
    def initiate_data_transformation(self):
        config=ConfigurationManager()
        data_transformation_config=config.get_data_transformation_config()
        data_transformation=Datatransformation(config=data_transformation_config)
        data_transformation.train_test_splitting()

if __name__=="__main__":
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DatatransformationTranningPipeline()
        obj.initiate_data_transformation()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(f"Error in stage {STAGE_NAME}: {e}")
        raise e