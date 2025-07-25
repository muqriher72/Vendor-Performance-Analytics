# Vendor Performance Data Analytics

In the retail and wholesale industry, it is important to maintain effective inventory and sales management practices to optimize profit. This goal is achieved by companies through checking and ensuring they are not incurring losses due inefficient pricing, poor inventory turnover, or vendor dependency.
This project uses SQL, Python, PowerBI, and Jupyter Notebooks to analyze the sales, pricing, purchases, freight, and inventory information of various brands.

The project invovles the following technical concepts:

- Python: Numpy, Pandas, Matplotlib, Seaborn, Scikit-Learn
- SQL
- PowerBI
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

```
├── LICENSE                 <- Open-source license if one is chosen
├── README.md               <- The top-level README for developers using this project.
├── data
│   ├── begin_inventory.csv     <- A CSV file that contains information on the initial inventory of a vendor.
│   ├── end_inventory.csv       <- A CSV file that contains information on the final inventory of a vendor.
│   ├── purchase_prices.csv     <- A CSV file that contains information on the purchase prices of a vendor.
│   ├── purchases.7z            <- A CSV file that contains information on the purchases of a vendor.
│   ├── sales.7z                <- A CSV file that contains information on the sales of a vendor.
│   └── vendor_invoice.csv      <- A CSV file that contains information on the invoice for a vendor.
│
├── logs                
│   └── ingestion_db.log        <- A log file that maintains the time taken to ingest the data files into the database.
│
├── powerbi                 
│   ├── BrandPerformance.xls         <- A CSV file created in PowerBI using a query and information from the inventory file.
│   ├── LowTurnoverVendor.xls        <- A CSV file created in PowerBI using a query and information from the inventory file.
│   ├── inventory.xls                <- A CSV file containing information from the vendor_sales_summary table.
│   ├── purchase_contributions.xls   <- A CSV file created in PowerBI using a query and information from the inventory file.
│   ├── vendorperformance.pbix       <- A PowerBI that contains a dashboard of the overall analysis results.
│   └── vendorperformance.pdf        <- A PDF file of the PowerBI dashboard.
│
├── Vendor Performance Report.pdf       <- A PDF report summarizing insights and reccomendations based on data analysis. 
│
├── exploratory_data_analysis.ipynb     <- A Jupyter Notebook file that contains the initial EDA performed on the data using Python and SQL queries.
│                         
├── get_vendor_summary.ipynb            <- A Jupyter Notebook file that contains the vendor summary table made using Python and SQL.
│
├── ingest_db.ipynb                     <- A Jupyter Notebook file that contains a Python script to ingest the data into the database and maintain logs.
│
└── vendor_performance_analysis.ipynb   <- A Jupyter Notebook file that contains the initial EDA performed on the data.
    
```

--------
    
