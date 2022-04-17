# -*- coding: utf-8 -*-
import logging
from pathlib import Path
from dotenv import find_dotenv, load_dotenv
import pandas as pd
import os
from pandas.plotting import table
from config.definitions import ROOT_DIR
import plotly
import plotly.express as px
import plotly.io as pio
import plotly.graph_objects as go
import plotly.figure_factory as ff
import numpy as np
# find .env automagically by walking up directories until it's found, then
# load up the .env entries as environment variables
load_dotenv(find_dotenv())

def main():
    logger = logging.getLogger(__name__)
    #Runs data processing scripts and find important features using PCA and save processed data in (../processed).
    logger.info('Starting data processing')
    df = pd.read_csv(os.path.join(ROOT_DIR, 'data','raw', '2018.csv'))
    logger.info('Data loaded into panda df')

    #Drop unneccesary columns
    df2 = df.drop(['CANCELLATION_CODE', 'DIVERTED', 'CARRIER_DELAY', 'WEATHER_DELAY',
                'NAS_DELAY', 'SECURITY_DELAY', 'LATE_AIRCRAFT_DELAY','Unnamed: 27'], axis=1)
    #Drop all rows with NA
    df2 = df2.dropna()

    logger.info('Building Plotly interactive graph for Correlation heatmap')
    corr = df2.corr()
    x = list(corr.columns)
    y = list(corr.index)
    z = np.array(corr)
    fig = px.imshow(z, text_auto='.2f', labels={x,y,z}, x=x, y=y, aspect="auto")
    fig.write_html(os.path.join(ROOT_DIR, 'data','processed', 'corr_heatmap3.html'))
    logger.info('Plotly Correlation heatmap saved in HTML')

if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)
    main()
