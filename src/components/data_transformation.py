import sys
import os

import pandas as pd
import numpy as np
from dataclasses import dataclass

from src.loggers import logging
from src.exception import CustomException

from sklearn.impute import SimpleImputer ## HAndling Missing Values
from sklearn.preprocessing import StandardScaler # HAndling Feature Scaling
from sklearn.preprocessing import OrdinalEncoder # Ordinal Encoding
## pipelines
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer

@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path=os.path.join('artifcats','preprocessor.pkl')
    
class DataTransformation:
    def __init__(self):
        self.DataTransformationConfig()
    
    def get_data_transformation_object(self):
        try:
            logging.info("Data Trnasirmation is intiated")
            
            catergorical_cols=['cut','color','clarity']
            numerical_cols=['carat','depth','table','x','y','z']
            
            cut_categories = ['Fair', 'Good', 'Very Good','Premium','Ideal']
            color_categories = ['D', 'E', 'F', 'G', 'H', 'I', 'J']
            clarity_categories = ['I1','SI2','SI1','VS2','VS1','VVS2','VVS1','IF']
            
            logging.info('Pipeline initiated')
            ## Numerical Pipeline
            num_pipeline=Pipeline(
                steps=[
                ('imputer',SimpleImputer(strategy='median')),
                ('scaler',StandardScaler())
                ]
            )

            # Categorigal Pipeline
            cat_pipeline=Pipeline(
                steps=[
                ('imputer',SimpleImputer(strategy='most_frequent')),
                ('ordinalencoder',OrdinalEncoder(categories=[cut_categories,color_categories,clarity_categories])),
                ('scaler',StandardScaler())
                ]
            )

            preprocessor=ColumnTransformer([
            ('num_pipeline',num_pipeline,numerical_cols),
            ('cat_pipeline',cat_pipeline,categorical_cols)
            ])
            return preprocessor
            
            logging.info("Pipeline Completed")

            
        except Exception as e:
            logging.info("Error in data transformation")
            raise CustomException(e,sys)
    
    def initiate_data_transformation(self,train_path,test_path):
        try:
            train_df=pd.read_csv(train_path)
            test_df=pd.read_csv(test_path)
            
            logging.info('Reading train and test data split is completed')
            logging.info(f'Train dataframe head : \n{train_df.head().to_string()}')
            logging.info(f'Train dataframe head : \n{test_df.head().to_string()}')
            
            logging.info('Obtaining preprocessing object')
            
            target_column_name='price'
            drop_columns=[target_column_name,'id']
            
            input_feature_train_df=train_df.drop(columns=drop_columns,axis=1)
            target_feature_train_df=train_df[target_column_name]
            
            input_featured_test_df=test_df.drop(columns=drop_columns,axis=1)
            target_feature_test_df=test_df[target_column_name]
            
            preprocessing_obj=self.get_data_transformation_object()
            
        except Exception as e:
            logging.info("Exception occured in the initiate_data_transformation")
            raise CustomException(e,sys)