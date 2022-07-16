from storesales.entity.config_entity import DataIngestionConfig
import sys, os
from storesales.exception import StoresalesException
from storesales.logger import logging

class DataIngestion:

    def __init__(self,data_ingestion_config:DataIngestionConfig):
        try:
            logging.info(f"{'='*20}Data Ingestion log started.{'='*20}")
            self.data_ingestion_config=data_ingestion_config
        except Exception as e:
            raise StoresalesException(e,sys)
    

    def initaite_data_ingestion(self)->DataIngestionArtifact:
        try:
            pass
        except Exception as e:
            raise StoresalesException(e,sys) from e

    
