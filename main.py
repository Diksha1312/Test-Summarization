from textSummarizer.logging import logger
from textSummarizer.pipeline.Stage_01_data_ingestion import DataIngestionPipeline


STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f"---------------- STAGE {STAGE_NAME} STARTED ----------------")
    data_ingestion = DataIngestionPipeline()
    data_ingestion.main()
    logger.info(f"---------------- STAGE {STAGE_NAME} COMPLETED --------------- \n\n")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data Ingestion Stage"