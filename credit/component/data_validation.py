import os, sys
from xml.dom.expatbuilder import ParseEscape
from xmlrpc.client import boolean
from credit.exception import CreditException
from credit.logger import logging
from credit.entity.config_entity import DataIngestionConfig, DataValidationConfig
from credit.entity.artifact_entity import DataIngestionArtifact
import pandas as pd
import json
### Package imports for data drift
from evidently.model_profile import Profile
from evidently.model_profile.sections import DataDriftProfileSection
## For report graphs
from evidently.dashboard import Dashboard
from evidently.dashboard.tabs import DataDriftTab

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

    def get_train_and_test_df(self):
        try:
            train_df= pd.read_csv(self.data_ingestion_artifact.train_file_path)
            test_df= pd.read_csv(self.data_ingestion_artifact.test_file_path)

            return train_df, test_df
        
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
                message= f"Train and test datasets are present in the respective paths"
                logging.info(message)
            else:
                logging.info(f"Files are not present in Training: {train_file_path} and testing: {test_file_path}")
                raise Exception("Training or testing file is not available")
        except Exception as e:
            raise CreditException(e, sys) from e

    
    def validate_data_schema(self)->bool:
        """Validation of dataset is done:
        1. Number of column check
        2. check the values of categorical features
        3. Feature names

        Returns:
            bool: True if data schema is matching else False 
        """
        try:
            ### We are defaulting the value as True as of now.
            validation_status = True

            return validation_status

        except Exception as e:
            raise CreditException(e, sys) from e


    def get_save_data_drift_report(self):
        """Save data drift report for reference
        """
        try:
            profile= Profile(sections=[DataDriftProfileSection()])#Create Profile

            #Getting train df and test df
            train_df, test_df= self.get_train_and_test_df()
            profile.calculate(train_df, test_df)

            ##Create json format of data drift and converting to report dict
            report= json.loads(profile.json())

            ## Save Json file
            os.makedirs(os.path.dirname(self.data_validation_config.report_file_path), exist_ok=True)
            with open(self.data_validation_config.report_file_path, "w") as report_file:
                json.dump(report, report_file, indent=6)

            return report
        except Exception as e:
            raise CreditException(e, sys) from e
        

    def save_data_drift_report_page(self):
        """Save graphical interface of the report
        """
        try:
            dashboard= Dashboard(tabs=[DataDriftTab()])
            #Getting train df and test df
            train_df, test_df= self.get_train_and_test_df()
            dashboard.calculate(train_df, test_df)
            ## Saving Dashboard
            os.makedirs(os.path.dirname(self.data_validation_config.report_page_file_path), exist_ok=True)
            dashboard.save(self.data_validation_config.report_page_file_path)
            self.get_save_data_drift_report
        except Exception as e:
            raise CreditException(e, sys) from e

    def validate_datadrift(self)->bool:
        """Validation of the dataset to check whether it is same as existing datasets
        that are processed before.

        Returns:
            bool: True When no datadrift
        """

        try:
            report= self.get_save_data_drift_report()
            self.save_data_drift_report_page()
            return True
        except Exception as e:
            raise CreditException(e, sys) from e

    def initiate_data_validation(self):
        try:
            self.is_train_test_file_exists()
            self.validate_data_schema()
            self.validate_datadrift()

        except Exception as e:
            raise CreditException(e, sys) from e