import os, sys
from credit.logger import logging
from credit.exception import CreditException
from credit.entity.config_entity import DataIngestionConfig
from credit.entity.artifact_entity import DataIngestionArtifact
from urllib import request
import pandas as pd
from imblearn.over_sampling import SMOTE
from credit.constant import *
import shutil
from sklearn.model_selection import StratifiedShuffleSplit




class DataIngestion:
    """Data ingestion process exceutes from downloading data from source to splitting the dataset
    between train and test
    Steps:
    * Download data from Url
    * Handle imbalance dataset
    * Splitting data for testing
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
        raw_file_name= os.path.join(self.data_ingestion_config.raw_data_dir,DATASET_FILE_NAME)
        
        '''request.urlretrieve(url_details,raw_file_name)
            Data download is currently down due to incorrect url.
            So we are copying file directly to  desired path.
        '''
        shutil.copy(DATASET_FILE_NAME,raw_file_name)
        logging.info(f"File has been downloaded in : {raw_file_name}")
        return raw_file_name
    
    def create_balanced_dataset(self)->None:
        """When there is imbalance dataset, we will over sample the dataset using SMOTE process
        and create balanced dataset
        """
        try:
            ## read data from file
            raw_data_file_dir= self.data_ingestion_config.raw_data_dir
            raw_data_file_path= os.path.join(raw_data_file_dir, DATASET_FILE_NAME)
            #print(raw_data_file_path)
            cc_imbalance= pd.read_csv(raw_data_file_path)
            ##input and output
            X, y= cc_imbalance.drop(columns=['default.payment.next.month'], axis=1), cc_imbalance['default.payment.next.month']
            ## resample data using SMOTE
            X_resampled, y_resampled= SMOTE().fit_resample(X, y)
            logging.info("Data balanced")

            ## Concating x and y data frames
            y_resampled_df=pd.DataFrame(y_resampled.values, columns=['defaulted'])

            resampled_df= pd.concat([X_resampled, y_resampled_df], axis=1)
            

            ## Saving to file
            file_path_dir=self.data_ingestion_config.balanced_data_dir
            ##Create Dataset
            os.makedirs(file_path_dir, exist_ok=True)
            file_name=os.path.join(file_path_dir, DATASET_FILE_NAME)

            resampled_df.to_csv(file_name)
            logging.info(f"Dataset has been balanced in path: {file_name}")
            return file_name
        except Exception as e:
            raise CreditException(e, sys) from e


    def get_data_split(self)->DataIngestionArtifact:
        """Splitting dataset into train and test and saving into respective folder paths
        Train dataset: Will be used to train model
        Test dataset: once model is ready testing happens with completely new dataset
        """
        try:
            balanced_dataset_path= self.data_ingestion_config.balanced_data_dir
            balanced_dataset_file_path= os.path.join(balanced_dataset_path, DATASET_FILE_NAME)
            ## Create dataframe
            balanced_df= pd.read_csv(balanced_dataset_file_path)
            ## Input and Output
            X_balanced=balanced_df.drop(columns=['defaulted'], axis=1)
            y_balanced= balanced_df['defaulted']

            ## Stratified split
            sss= StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)

            ## Split the data
            for train_index, test_index in sss.split(X_balanced,  y_balanced):
                balanced_train_df= pd.concat([X_balanced.loc[train_index], y_balanced.loc[train_index]], axis=1)
                balanced_test_df= pd.concat([X_balanced.loc[test_index], y_balanced.loc[test_index]], axis=1)

            ### Create fodler paths for balanced train and test datasets
            os.makedirs(self.data_ingestion_config.ingested_train_dir, exist_ok=True)
            os.makedirs(self.data_ingestion_config.ingested_test_dir, exist_ok=True)

            ingested_train_file_path= os.path.join(self.data_ingestion_config.ingested_train_dir, DATASET_FILE_NAME)
            ingested_test_file_path= os.path.join(self.data_ingestion_config.ingested_test_dir, DATASET_FILE_NAME)

            ## Save datasets to respective folder paths
            balanced_train_df.to_csv(ingested_train_file_path)
            balanced_test_df.to_csv(ingested_test_file_path)
            data_ingestion_artifact= self.create_data_ingestion_artifact(ingested_train_file_path, ingested_test_file_path)

            logging.info(f"ingested train and test datasets has been created. Details: {data_ingestion_artifact}")
            return data_ingestion_artifact
        except Exception as e:
            raise CreditException(e, sys) from e

    def create_data_ingestion_artifact(self, train_file_path, test_file_path)->DataIngestionArtifact:
        """create Data ingestion artifact by considering train and test file paths

        Returns:
            DataIngestionArtifact: Tuple with data ingestion data
        """
        try:
            data_ingestion_artifact= DataIngestionArtifact(train_file_path=train_file_path,
                                                           test_file_path=test_file_path,
                                                           is_ingested=True,
                                                           message=f"Data ingestion is successful")
            return data_ingestion_artifact
        except Exception as e:
            raise CreditException(e, sys) from e

    def initiate_data_ingestion(self)->DataIngestionArtifact:
        """Initiate data ingestion process to perform actions on dataset

        Returns:
            DataIngestionArtifact: Dataingestion artifact details
        """

        try:
            ##Download Dataset from url 
            raw_file_name= self.download_data()
            logging.info(f"Data download has been successful.")
            ## balancing the dataset using SMOTE process
            balanced_dataset_path= self.create_balanced_dataset()
            ##Create ingested train and test datasets by splitting
            data_ingestion_artifact= self.get_data_split()
            return data_ingestion_artifact

        except Exception as e:
            raise CreditException(e, sys) from e

        