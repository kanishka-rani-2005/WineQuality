from WineQuality import logger
from WineQuality.components.model_trainer import ModelTrainer
from  WineQuality.config.configuration import ConfigurationManager




STAGE_NAME="Model Training Stage"

class ModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config=ConfigurationManager()
        model_trainer_config=config.get_model_trainer_config()
        model_trainer=ModelTrainer(config=model_trainer_config)
        model_trainer.train()
                



if __name__=='__main__':
    try:
        logger.info(f">>>>>>>>>>>>>>>>>>>>> Stage {STAGE_NAME} started >>>>>>>>>>>>>>>>>>>>>>>>>>")
        obj=ModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>>>>>>>>>>>>>>>> Stage {STAGE_NAME} completed >>>>>>>>>>>>>>>>>>>>>>>>")
    except Exception as e:
        logger.exception(e)
        raise e