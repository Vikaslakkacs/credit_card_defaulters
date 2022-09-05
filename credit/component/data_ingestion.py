import os, sys
from tkinter import E
from credit.logger import logging
from credit.exception import CreditException
from credit.entity.config_entity import DataIngestionConfig
from credit.entity.artifact_entity import DataIngestionArtifact






class DataIngestion:
    """Data ingestion process exceutes from downloading data from source to splitting the dataset
    between train and test
    """

    def __init__(self, data_ingestion_config:DataIngestionConfig):
        try:
            logging.info(f"{'=' * 20} Data ingestion log started {'=' * 20}")
            self.data_ingestion_config= data_ingestion_config
        except Exception as e:
            raise CreditException(e, sys) from e
    
    def initiate_data_ingestion(self)->DataIngestionArtifact:
        """Initiate data ingestion process to perform actions on dataset

        Returns:
            DataIngestionArtifact: Dataingestion artifact details
        """

        try:
            pass
        except Exception as e:
            raise CreditException(e, sys) from e
    

