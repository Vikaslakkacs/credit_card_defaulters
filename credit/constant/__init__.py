import os
from datetime import datetime



ROOT_DIR=os.getcwd()### Current working directory
CONFIG_DIR="config"
CONFIG_FILE_NAME="config.yaml"
CONFIG_FILE_PATH=os.path.join(ROOT_DIR,CONFIG_DIR,CONFIG_FILE_NAME)##Configuration file path

## Current time stamp
CURRENT_TIME_STAMP= f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}"
DATASET_FILE_NAME="credit_card_defaulters.csv"

## Training pipeline
TRAINING_PIPELINE_CONFIG_KEY="training_pipeline_config"
TRAINING_PIPELINE_NAME_KEY="pipeline_name"## The main folder where all the project code resides
TRAINING_PIPELINE_ARTIFACT_DIR_KEY="artifact_dir"## The folder where all the dataset related operations are present


## Data ingestion pipeline
DATA_INGESTION_CONFIG_KEY="data_ingestion_config"
DATA_INGESTION_ARTIFACT_DIR_KEY= "data_ingestion_artifact_dir"
DATA_INGESTION_DOWNLOAD_URL_KEY="dataset_download_url"
DATA_INGESTION_RAW_DATA_DIR_KEY="raw_data_dir"
DATA_INGESTION_BALANCED_DIR_KEY="balanced_dataset_dir"
DATA_INGESTION_DIR_NAME_KEY="ingested_dir"
DATA_INGESTION_TRAIN_DIR_KEY="ingested_train_dir"
DATA_INGESTION_TEST_DIR_KEY="ingested_test_dir"