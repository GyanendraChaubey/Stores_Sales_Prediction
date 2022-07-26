from ast import Store
from tkinter import E
from storesales.exception import StoresalesException
from storesales.logger import logging
import sys, os
from storesales.entity.artifact_entity import DataIngestionArtifact, DataValidationArtifact
from storesales.entity.config_entity import DataIngestionConfig, DataValidationConfig
from storesales.component.data_ingestion import DataIngestion
from storesales.component.data_validation import DataValidation
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
    
    def start_data_validation(self, data_ingestion_artifact: DataIngestionArtifact)-> DataValidationArtifact:
        try:
            data_validation = DataValidation(data_validation_config=self.config.get_data_validation_config(),
                                             data_ingestion_artifact=data_ingestion_artifact
                                             )
            return data_validation.initiate_data_validation()
        except Exception as e:
            raise StoresalesException(e, sys) from e
    
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
            data_validation_artifact = self.start_data_validation(data_ingestion_artifact=data_ingestion_artfact)
        
        except Exception as e:
            raise StoresalesException(e,sys) from e
