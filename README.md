Flight Data Modelling
==============================

Dataset from Kaggle : kaggle.com/datasets/yuanyuwendymu/airline-delay-and-cancellation-data-2009-2018

Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── processed      <- Processed data and plots
    │   └── raw            <- The original, immutable data dump.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    └── src                <- Source code for use in this project.
        ├── __init__.py    <- Makes src a Python module
        │
        ├── make_dataset.py <- Scripts to download or generate data
        │
        ├── build_features.py <- Scripts to analyse data
        │
        └── data_analysis.ipynb  <- Scripts to train models and then use trained models to make
                                predictions


--------

<p><small>Project for DS-GA 3001 - Spring 2022</small></p>
