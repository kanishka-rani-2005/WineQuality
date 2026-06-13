from WineQuality import logger
from WineQuality.components.data_transformation import DataTransformation
from  WineQuality.config.configuration import ConfigurationManager




STAGE_NAME="Data Transformation Stage"

class DataTransformationrainingPipeline:
    def __init__(self):
        pass

    def main(self):
            config=ConfigurationManager()
            data_transformation_config=config.get_data_transformation_config()
            data_transformation=DataTransformation(config=data_transformation_config)
            data_transformation.train_test_split()
        



if __name__=='__main__':
    try:
        logger.info(f">>>>>>>>>>>>>>>>>>>>> Stage {STAGE_NAME} started >>>>>>>>>>>>>>>>>>>>>>>>>>")
        obj=DataTransformationrainingPipeline()
        obj.main()
        logger.info(f">>>>>>>>>>>>>>>>>>>>> Stage {STAGE_NAME} completed >>>>>>>>>>>>>>>>>>>>>>>>")
    except Exception as e:
        logger.exception(e)
        raise e