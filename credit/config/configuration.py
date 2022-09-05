import os, sys
from credit.logger import logging
from credit.exception import CreditException
from credit.entity.config_entity import DataIngestionConfig, TrainingPipelineConfig
import yaml
from credit.util.util import read_yaml_file
from credit.constant import *

class Configuration:

    """Creating configuration attributes for components involved
    This will result in the paths and other configurable attributes that re required for the project.
    """
    def __init__(self,
                config_file_path:str=CONFIG_FILE_PATH,
                current_time_stamp:str=CURRENT_TIME_STAMP)-> None:
        self.config_info= read_yaml_file(file_path=config_file_path)
        logging.info("Configuration from Yaml file has been read")
        self.train_pipeline_config= self.get_training_pipeline_config()
        self.time_stamp= current_time_stamp
        


    def get_data_ingestion_config(self)->DataIngestionConfig:
        """Assign all the inputs related to Data ingestion to DataIngestionConfig tuple.

        Returns:
            DataIngestionConfig: Named Tuple with assigned configuration
        """
        pass

    def get_training_pipeline_config(self)->TrainingPipelineConfig:
        """It generates pipeline configuration such as configuring directories such as where all
        the dataset details shoud store while performing analysis


        Returns:
            TrainingPipelineConfig: Tuple of pipeline configuraiton
        """
        try:
            pipleline_config= self.config_info[TRAINING_PIPELINE_CONFIG_KEY]
            artifact_dir= os.path.join(ROOT_DIR, pipleline_config[TRAINING_PIPELINE_NAME_KEY],
                                        pipleline_config[TRAINING_PIPELINE_ARTIFACT_DIR_KEY])

            training_pipeline_config= TrainingPipelineConfig(artifact_dir=artifact_dir)
            logging.info(f"Training pipeline config: {training_pipeline_config}")
            return training_pipeline_config
        except Exception as e:
            raise CreditException(e, sys) from e
