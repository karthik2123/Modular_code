"""
Objective:-

"""
from my_modular_code.exception import InsuranceException
import os
import sys
from datetime import datetime
from my_modular_code.logger import logging

File_name="insureance.csv"
Train_File_Name="train.csv"
Test_File_Name="test.csv"
class TrainingPipelineConfig:
    def __init__(self) :
        try:
            self.artifact_dir=os.path.join(os.getcwd(),"artifact",f"{datetime.now().strftime('%m$d%Y_%H%M%S')}")
        except Exception as e:
            raise InsuranceException(e,sys)
class DataIngestionConfig:
    def __init__(self,training_pipeline_config:TrainingPipelineConfig):
        try:
            self.database_name = "INSURANNCE"
            self.collection_name = "INSURANCE_PROJECT"
            self.data_ingestion_dir = os.path.join(training_pipeline_config.artifact_dir,"data_ingestion")
            self.feature_store_file_name = os.path.join(self.data_ingestion_dir,"feature_store",File_name)
            self.train_file_path=os.path.join(self.data_ingestion_dir,"dataset",Train_File_Name)
            self.test_file_path=os.path.join(self.data_ingestion_dir,"dataset",Test_File_Name)
            self.test_size=0.2
        
        except Exception as e:
            raise InsuranceException(e,sys)
        
    
    def to_dict(self):
        try:
            return self.__dict__
        except Exception as e:
            raise InsuranceException(e,sys)
    

class DataValidationConfig:
    def __init__(self,training_pipeline_config:TrainingPipelineConfig):

        self.data_validation_dir=os.path.join(training_pipeline_config.artifact_dir,"data_validation")
        self.report_file_path=os.path.join(self.data_validation_dir, "report.yaml")
        self.missingthreshold:float = 0.2
        # self.base_file_path=os.path.join("insureance.csv")
        self.base_file_path=os.path.join("insurance.csv")
        

