# Solar Challenge Dashboard

## Project Overview
This project is a Streamlit dashboard for visualizing and analyzing solar data for Benin, Togo, and Sierra Leone. The dashboard allows users to select a country, view cleaned data, visualize GHI (Global Horizontal Irradiance) distributions, and see top regions by GHI.

## Features
- Sidebar navigation with country selection
- Data loading and display for Benin, Togo, and Sierra Leone
- GHI boxplot visualization

## Development Process
1. **Project Setup:**
    - Created a Python virtual environment and installed dependencies (`streamlit`, `pandas`, `matplotlib`, `seaborn`).
    - Set up the project structure with an `app` directory and data files in `data/`.
2. **Initial Streamlit App:**
    - Built a minimal Streamlit app in `app/main.py` with a title, sidebar, and sample data table.
3. **Data Integration:**
    - Loaded cleaned CSV data for each country.
    - Implemented country selection in the sidebar.
4. **Visualization:**
    - Added a boxplot for the GHI column using Seaborn and Matplotlib.
5. **Documentation:**
    - Documented the development process and usage instructions in this README.

## Usage Instructions

### 1. Clone the Repository
```bash
git clone <repository-url>
cd solar-challenge-week1
```

### 2. Install Dependencies
It is recommended to use a virtual environment:
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Add Data Files
Place the cleaned CSV files (`benin_clean.csv`, `togo_clean.csv`, `sierraleone_clean.csv`) in the `data/` directory.

### 4. Run the Streamlit App
```bash
streamlit run app/main.py
```

### 5. Using the Dashboard
- Use the sidebar to select a country.
- View the cleaned data table for the selected country.
- See the GHI boxplot

## Project Structure
```
solar-challenge-week1/
│
├── app/
│   ├── main.py
│   └── __init__.py (optional)
├── data/
│   ├── benin_clean.csv
│   ├── togo_clean.csv
│   └── sierraleone_clean.csv
├── requirements.txt
└── README.md
```

## Notes
- Ensure your data files have the required columns ( `GHI`).