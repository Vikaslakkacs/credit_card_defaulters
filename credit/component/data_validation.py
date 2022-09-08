import os, sys
from xmlrpc.client import boolean
from credit.exception import CreditException
from credit.logger import logging
from credit.entity.config_entity import DataIngestionConfig, DataValidationConfig
from credit.entity.artifact_entity import DataIngestionArtifact

class DataValidation:
    """Validating Dataset
    1. by comparing with previous data whether any additional features or feature values has been added
    2. Verifying data types and many more.
    """
    

    def __init__(self,data_ingestion_artifact=DataIngestionArtifact, 
                    data_validation_config= DataValidationConfig):
        
        try:
            logging.info(f"{'>>'* 20} data Validation has started {'<<' * 20}")
            self.data_ingestion_artifact= data_ingestion_artifact
            self.data_validation_config= data_validation_config
        except Exception as e:
            raise CreditException(e, sys) from e

    
    def is_train_test_file_exists(self)->boolean:
        """To check whether train and test files are present

        Returns:
            boolean: True: present, False: any one of the files are absent
        """
        try:
            train_file_path= self.data_ingestion_artifact.train_file_path
            test_file_path= self.data_ingestion_artifact.test_file_path
            ## If files are present in both train and test then True
            if all([os.path.exists(train_file_path), os.path.exists(test_file_path)]):
                logging.info(f"Train and test datasets are present in the respective paths")
                return True
            else:
                logging.info("Train or Test dataset is not available")
                return False
        except Exception as e:
            raise CreditException(e, sys) from e


    
    def initiate_data_validation(self):
        try:
            train_test_dataset_available= self.is_train_test_file_exists()
        except Exception as e:
            raise CreditException(e, sys) from e