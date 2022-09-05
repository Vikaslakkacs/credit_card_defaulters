import os, sys
from credit.logger import logging
from credit.exception import CreditException
from credit.entity.config_entity import DataIngestionConfig
from credit.entity.artifact_entity import DataIngestionArtifact
from urllib import request






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
    
    def download_data(self)->str:
        """Download data from from source

        Returns:
            str: file path where downloaded data is stored.
        """
        url_details=self.data_ingestion_config.dataset_download_url
        ### Create folders if there is no folder created in the name of data ingestion
        ### in artifact folder
        ## save it in raw data folder
        ### Create folder if not exists
        os.makedirs(self.data_ingestion_config.raw_data_dir, exist_ok=True)
        print(self.data_ingestion_config.raw_data_dir)
        raw_file_name= os.path.join(self.data_ingestion_config.raw_data_dir,"creditcard_defaulters.csv")
        request.urlretrieve(url_details,raw_file_name)

        logging.info(f"File has been downloaded in : {raw_file_name}")
        return raw_file_name


    def initiate_data_ingestion(self)->DataIngestionArtifact:
        """Initiate data ingestion process to perform actions on dataset

        Returns:
            DataIngestionArtifact: Dataingestion artifact details
        """

        try:
            ##Download Dataset from url 
            raw_file_name= self.download_data()
            logging.info(f"Data download has been successful.")
        except Exception as e:
            raise CreditException(e, sys) from e
    

