from src.DataScienceProject.config.configuration import ConfigurationManager
from src.DataScienceProject.components.model_trianer import ModelTraner
from src.DataScienceProject import logger
STAGE_NAME="Model training Stage"

class ModelTranningPipeline:
    def __init__(self):
        pass
    def initiate_Model_tranier(self):
        config=ConfigurationManager()
        Model_Trainer_config=config.get_model_trainer_config()
        Model_Trainer_config=ModelTraner(config=Model_Trainer_config)
        Model_Trainer_config.train()

if __name__=="__main__":
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = ModelTranningPipeline()
        obj.initiate_Model_tranier()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(f"Error in stage {STAGE_NAME}: {e}")
        raise e