# -*- coding: utf-8 -*-
import logging
from pathlib import Path
from dotenv import find_dotenv, load_dotenv
import csv
import pandas as pd
import os
import zipfile
# find .env automagically by walking up directories until it's found, then
# load up the .env entries as environment variables
load_dotenv(find_dotenv())
from kaggle.api.kaggle_api_extended import KaggleApi


def main():
    #Runs scripts to download zipped data from kaggle and unzip csv into (../raw) ready to be processed.
    logger = logging.getLogger(__name__)
    api = KaggleApi()
    api.authenticate()
    logger.info('downloading zipped data from kaggle')
    api.dataset_download_file('yuanyuwendymu/airline-delay-and-cancellation-data-2009-2018',file_name='2018.csv', path='../../data/raw/')
    
    logger.info('Unzipping csv file')
    with zipfile.ZipFile('../../data/raw/2018.csv.zip', 'r') as zipref:
        zipref.extractall('../../data/raw')

    #Runs data processing scripts and find important features using PCA and save processed data in (../processed).
    logger.info('Starting data processing')
    df = pd.read_csv('../../data/raw/2018.csv')
    #print(df.head())
    df.info()


if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    #not used in this stub but often useful for finding various files
    #project_dir = Path(__file__).resolve().parents[2]
    main()
