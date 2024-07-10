from textSummarizer.logging import logger
from textSummarizer.pipeline.Stage_01_data_ingestion import DataIngestionPipeline
from textSummarizer.pipeline.Stage_02_data_validation import DataValidationPipeline
from textSummarizer.pipeline.Stage_03_data_transformation import DataTransformationPipeline
from textSummarizer.pipeline.Stage_04_model_trainer import ModelTrainerPipeline
from textSummarizer.pipeline.Stage_05_model_evaluation import ModelEvaluationPipeline


STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f"---------------- STAGE {STAGE_NAME} STARTED ----------------")
    data_ingestion = DataIngestionPipeline()
    data_ingestion.main()
    logger.info(f"---------------- STAGE {STAGE_NAME} COMPLETED --------------- \n\n")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data Validation Stage"
try:
    logger.info(f"---------------- STAGE {STAGE_NAME} STARTED ----------------")
    data_ingestion = DataValidationPipeline()
    data_ingestion.main()
    logger.info(f"---------------- STAGE {STAGE_NAME} COMPLETED --------------- \n\n")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data Transformation Stage"
try:
    logger.info(f"---------------- STAGE {STAGE_NAME} STARTED ----------------")
    data_ingestion = DataTransformationPipeline()
    data_ingestion.main()
    logger.info(f"---------------- STAGE {STAGE_NAME} COMPLETED --------------- \n\n")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Model Trainer Stage"
try:
    logger.info(f"---------------- STAGE {STAGE_NAME} STARTED ----------------")
    data_ingestion = ModelTrainerPipeline()
    data_ingestion.main()
    logger.info(f"---------------- STAGE {STAGE_NAME} COMPLETED --------------- \n\n")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Model Evaluation Stage"
try:
    logger.info(f"---------------- STAGE {STAGE_NAME} STARTED ----------------")
    data_ingestion = ModelEvaluationPipeline()
    data_ingestion.main()
    logger.info(f"---------------- STAGE {STAGE_NAME} COMPLETED --------------- \n\n")
except Exception as e:
    logger.exception(e)
    raise e