# Vendor Performance Data Analytics

In the retail and wholesale industry, it is important to maintain effective inventory and sales management practices to optimize profit. This goal is achieved by companies through checking and ensuring they are not incurring losses due inefficient pricing, poor inventory turnover, or vendor dependency.
This project uses SQL, Python, PowerBI, and Jupyter Notebooks to analyze the sales, pricing, purchases, freight, and inventory information of various brands.

The project invovles the following technical concepts:

- Python: Numpy, Pandas, Matplotlib, Seaborn, Scikit-Learn
- Hypothesis Testing

## Research Goal

The goal of the analysis is to:
- identify underperforming brands that require pricing readjustment or promotions
- determine top vendors contributing to sales and gross profit
- analyze the impact of bulk purchasing on unit costs
- assess inventory turnover to reduce holding costs and improve efficiency
- investigate the profitability variance between high-performing and low-performing vendors

## Data

This dataset is a collection of records related to a vendor performance analysis project, which aims to provide a holistic view of vendor profitability and efficiency. The data is compiled from several sources, including purchases, sales, and vendor invoice records. It is used to analyze various aspects of the business, such as vendor contribution to sales and profit, the impact of bulk purchasing, inventory turnover, and profitability variances.

The dataset contains the following key features:

- Vendor and Brand Information: VendorNumber, VendorName, Brand, and Description.

- Purchase Metrics: PurchasePrice, TotalPurchaseQuantity, TotalPurchaseDollars, FreightCost, and Volume.

- Sales Metrics: ActualPrice, TotalSalesQuantity, TotalSalesDollars, and TotalSalesPrice.

- Profitability and Performance Indicators: GrossProfit, ProfitMargin, StockTurnover, and SalestoPurchaseRatio.

## Approach

The following tasks are completed in this project:
- SQL Data Analysis & Cleaning
- EDA with Python
- Hypothesis Testing & Confidence Interval
- PowerBI Dashboard
- Report

## Project Organization

├── LICENSE            <- Open-source license if one is chosen
├── Makefile           <- Makefile with convenience commands like `make data` or `make train`
├── README.md          <- The top-level README for developers using this project.
├── data
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│
├── docs               <- A default mkdocs project; see www.mkdocs.org for details
│
├── models             <- Trained and serialized models, model predictions, or model summaries
│
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering) and a
│                         short `-` delimited description, e.g.`1.0-jqp-initial-data-exploration`.
│                           0 - Data exploration 
│                           1 - Data cleaning and feature creation
│                           2 - Visualizations
│                           3 - Modeling (training and evaluating machine learning models)
│                               3.0X – Baseline Model
│                               3.1X – GPA Predictor 
│                               3.2X – Optimizer for study habits
│                               3.3X – KNN sxample students finder
│                               3.4X – Text generation (GPT-4)
│                               3.5X – Final integrated model
│
├── pyproject.toml     <- Project configuration file with package metadata for 
│                         smartstudy and configuration for tools like black
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures        <- Generated graphics and figures to be used in reporting
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
│
├── setup.cfg          <- Configuration file for flake8
│
└── smartstudy   <- Source code for use in this project.
    │
    ├── __init__.py             <- Makes smartstudy a Python module
    │
    ├── config.py               <- Store useful variables and configuration
    │
    ├── dataset.py              <- Scripts to download or generate data
    │
    ├── generate_scaler.py      <- Code to scale data for modeling
    │
    ├── features.py             <- Code to create features for modeling
    │
    ├── modeling                
    │   ├── __init__.py 
    │   ├── train_tabpfn.py      <- Code to train tabpfn model into serialized model     
    │   ├── optimizer.py         <- Code to run optimization with tabpfn model  
    │   ├── knn_matching.py      <- Code to run knn matching using user input       
    │   └── gpt_utils.py         <- Code to run gpt-4 model for text generation
    │
    ├── app.py                  <- Code to run the GUI and call relevant scripts
    │
    └── plots.py                <- Code to create visualizations
    
