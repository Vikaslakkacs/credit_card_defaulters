import os, sys
from credit.exception import CreditException
from credit.logger import logging
from credit.constant import *
from credit.config.configuration import Configuration

from credit.entity.artifact_entity import DataIngestionArtifact
from credit.entity.config_entity import DataIngestionConfig
from credit.component.data_ingestion import DataIngestion##For Data ingestion process

class Pipeline():


    def __init__(self, config=Configuration()):

        try:
            logging.info(f"{'>>' * 20} Pipeline has started {'<<' * 20}")
            self.config= config
        except Exception as e:
            raise CreditException(e, sys) from e

    def start_data_ingestion(self)->DataIngestionArtifact:
        """Executes Data ingestion process:
        1. Downloads data from source (url, file etc)
        2. Balance the data if there is any imbalance data
        3. splits data into train and test

        Returns:
            DataIngestionArtifact: Tuple which has the details of dataset that needs to be processed
                                   for next step of action
        """

        try:
            data_ingestion_config= self.config.get_data_ingestion_config()
            data_ingestion= DataIngestion(data_ingestion_config=data_ingestion_config)
            data_ingestion_artifact= data_ingestion.initiate_data_ingestion()
            return data_ingestion_artifact
        except Exception as e:
            raise CreditException(e, sys) from e

    

    def run_pipeline(self):
        """Initiating pipeline with step by step process
        """
        try:
            data_ingestion_artifact= self.start_data_ingestion()

        except Exception as e:
            raise CreditException(e, sys) from e