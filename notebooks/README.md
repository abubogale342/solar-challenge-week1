# Solar Irradiance Data Analysis

This project involves cleaning, exploring, and analyzing solar irradiance sensor data to uncover patterns, correlations, and the impact of cleaning on sensor performance.

## 📊 Dataset Overview

- **Features:** GHI, DNI, DHI, ModA, ModB, Tamb, RH, WS, WSgust, WD, Timestamp, CleaningFlag, etc.
- **Source:** Provided CSV file
- **Target Tasks:**
  - Detect outliers
  - Handle missing values
  - Analyze time series
  - Study wind patterns and distributions
  - Correlation and scatter analysis
  - Evaluate sensor performance before and after cleaning

## 🧹 Data Cleaning

- Handled missing values (imputed with median).
- Removed outliers using **Z-score (|Z| > 3)** method for key numeric features.
- Exported cleaned data to: `data/<country>_clean.csv` _(excluded via `.gitignore`)_

## 📈 Analysis & Visualizations

- **Correlation Heatmap:** GHI, DNI, DHI, TModA, TModB
- **Scatter Plots:**
  - WS, WSgust, WD vs GHI
  - RH vs Tamb / GHI
- **Time Series Plots:**
  - Line chart of GHI, DNI, DHI, Tamb over Timestamp
- **Cleaning Impact:**
  - Bar chart of average ModA & ModB pre/post-cleaning
- **Wind Rose:** WS vs WD (via `windrose` library)
- **Distributions:** Histograms of GHI and WS

## 🛠 Tools Used

- Python (Pandas, NumPy, Matplotlib, Seaborn)
- Windrose (`pip install windrose`)
- Jupyter Notebook / Python script

## 🚫 .gitignore

- CSV files are excluded:
