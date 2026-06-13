from WineQuality import logger
from WineQuality.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from WineQuality.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from WineQuality.pipeline.stage_03_data_transformation import DataTransformationrainingPipeline
from WineQuality.pipeline.stage_04_model_trainer import ModelTrainingPipeline
from WineQuality.pipeline.stage_05_model_evaluation import ModelEvaluationPipeline


STAGE_NAME="Data Ingestion stage"
try:
    logger.info(f">>>>>>>>>>> Stage {STAGE_NAME} started >>>>>>>>>>>>>>>>>>>")
    obj=DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>>>>>> Stage {STAGE_NAME} completed >>>>>>>>>>>>>>>>>")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME="Data Validation stage"
try:
    logger.info(f">>>>>>>>>>> Stage {STAGE_NAME} started >>>>>>>>>>>>>>>>>>>")
    obj=DataValidationTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>>>>>> Stage {STAGE_NAME} completed >>>>>>>>>>>>>>>>>")
except Exception as e:
    logger.exception(e)
    raise e





STAGE_NAME="Data Transformation stage"
try:
    logger.info(f">>>>>>>>>>> Stage {STAGE_NAME} started >>>>>>>>>>>>>>>>>>>")
    obj=DataTransformationrainingPipeline()
    obj.main()
    logger.info(f">>>>>>>>>>> Stage {STAGE_NAME} completed >>>>>>>>>>>>>>>>>")
except Exception as e:
    logger.exception(e)
    raise e



STAGE_NAME="Model Training stage"
try:
    logger.info(f">>>>>>>>>>> Stage {STAGE_NAME} started >>>>>>>>>>>>>>>>>>>")
    obj=ModelTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>>>>>> Stage {STAGE_NAME} completed >>>>>>>>>>>>>>>>>")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME="Model Evaluation stage"
try:
    logger.info(f">>>>>>>>>>> Stage {STAGE_NAME} started >>>>>>>>>>>>>>>>>>>")
    obj=ModelEvaluationPipeline()
    obj.main()
    logger.info(f">>>>>>>>>>> Stage {STAGE_NAME} completed >>>>>>>>>>>>>>>>>")
except Exception as e:
    logger.exception(e)
    raise e
