from ast import Store
from tkinter import E
from storesales.exception import StoresalesException
from storesales.logger import logging
import sys, os
from storesales.entity.artifact_entity import DataIngestionArtifact
from storesales.entity.config_entity import DataIngestionConfig, DataTransformationConfig, DataValidationConfig
from storesales.component.data_ingestion import DataIngestion
from storesales.config.configuration import Configuration


class Pipeline:

    def __init__(self, config: Configuration=Configuration())->None:
        try:
            self.config=config
        except Exception as e:
            raise StoresalesException(e,sys) from e
    
    def start_data_ingestion(self)->DataIngestionArtifact:
        try:
            data_ingestion = DataIngestion(data_ingestion_config=self.config.get_data_ingestion_config())
            return data_ingestion.initaite_data_ingestion()
        except Exception as e:
            raise StoresalesException(e,sys) from e
    
    def start_data_validation(self):
        try:
            pass
        except Exception as e:
            raise StoresalesException(e,sys) from e
    
    def start_data_transformation(self):
        try:
            pass
        except Exception as e:
            raise StoresalesException(e,sys) from e
    
    def start_model_training(self):
        try:
            pass
        except Exception as e:
            raise StoresalesException(e,sys) from e
    
    def start_model_evaluation(self):
        try:
            pass
        except Exception as e:
            raise StoresalesException(e,sys) from e
    
    def start_model_pusher(self):
        try:
            pass
        except Exception as e:
            raise StoresalesException(e,sys) from e
    
    def run_pipeline(self):
        try:
            data_ingestion_artfact=self.start_data_ingestion()
        except Exception as e:
            raise StoresalesException(e,sys) from e
