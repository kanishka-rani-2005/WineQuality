from WineQuality import logger
from WineQuality.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline




logger.info("welcome")


STAGE_NAME="Data Ingestion stage"
try:
    logger.info(f">>>>>>>>>>> Stage {STAGE_NAME} started >>>>>>>>>>>>>>>>>>>")
    obj=DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>>>>>> Stage {STAGE_NAME} completed >>>>>>>>>>>>>>>>>")
except Exception as e:
    logger.exception(e)
    raise e