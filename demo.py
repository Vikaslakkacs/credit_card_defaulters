from credit.pipeline.pipeline import Pipeline
import os, sys
from credit.logger import logging
from credit.exception import CreditException
from credit.config.configuration import Configuration
from credit.constant import *
from credit.component.data_validation import DataValidation
from credit.entity.artifact_entity import DataIngestionArtifact
'''def main():
    try:
        pipeline= Pipeline()
        pipeline.run_pipeline()
    except Exception as e:
        logging.error(f"{e}")
        raise CreditException(e, sys) from e
'''
def main():
    config= Configuration(config_file_path=CONFIG_FILE_PATH)
    print(config.get_data_validation_config())
    data_val= DataValidation(DataIngestionArtifact(train_file_path='/Users/vikaslakka/Desktop/FSDS/Machine_learning/Projects/Credit_card_defaulters/credit_card_defaulters/credit/artifact/data_ingestion/2022-09-08-17-41-44/ingested_data/train/credit_card_defaulters.csv', test_file_path='/Users/vikaslakka/Desktop/FSDS/Machine_learning/Projects/Credit_card_defaulters/credit_card_defaulters/credit/artifact/data_ingestion/2022-09-08-17-41-44/ingested_data/test/credit_card_defaulters.csv', is_ingested=True, message='Data ingestion is successful')
                            , config.get_data_validation_config())
    print(data_val.is_train_test_file_exists())
    data_val.initiate_data_validation()

if __name__=="__main__":
    main()