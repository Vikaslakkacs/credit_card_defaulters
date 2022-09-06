from credit.component.data_ingestion import DataIngestion
from credit.config.configuration import Configuration
## Get Data ingestion data
#config_file_path=
config= Configuration()
data_ingestion_config= config.get_data_ingestion_config()
#print(data_ingestion_config)
data_inges=DataIngestion(data_ingestion_config)
data_inges.initiate_data_ingestion()