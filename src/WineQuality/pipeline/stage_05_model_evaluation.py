from WineQuality import logger
from WineQuality.components.model_evaluation import ModelEvaluation
from  WineQuality.config.configuration import ConfigurationManager




STAGE_NAME="Model Evaluation Stage"

class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config=ConfigurationManager()
        model_evaluation_config=config.get_model_evaluation_config()
        model_evaluation=ModelEvaluation(config=model_evaluation_config)
        model_evaluation.log_into_mlflow()
                



if __name__=='__main__':
    try:
        logger.info(f">>>>>>>>>>>>>>>>>>>>> Stage {STAGE_NAME} started >>>>>>>>>>>>>>>>>>>>>>>>>>")
        obj=ModelEvaluationPipeline()
        obj.main()
        logger.info(f">>>>>>>>>>>>>>>>>>>>> Stage {STAGE_NAME} completed >>>>>>>>>>>>>>>>>>>>>>>>")
    except Exception as e:
        logger.exception(e)
        raise e