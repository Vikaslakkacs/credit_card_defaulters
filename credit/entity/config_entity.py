from collections import namedtuple

## Data ingestion Config
"""For Data ingestion:
1. Collect Dataset url
2. path of tgz url if it is in tgz format
3.path of raw data (which in case here it is csv)
4. path of ingested train data
5. path of ingested test data
"""
DataIngestionConfig=namedtuple("DataIngestionConfig",
                                ["dataset_download_url",
                                "raw_data_dir",
                                "balanced_data_dir",
                                "ingested_train_dir",
                                "ingested_test_dir"])

TrainingPipelineConfig = namedtuple("TrainingPipelineConfig", ["artifact_dir"])

DataValidationConfig= namedtuple("DataValidationConfig", [
                                                     "schema_file_path",
                                                     "report_file_path",
                                                     "report_page_file_path"])