# Python OHLCV Time-Series Analysis

## Overview

This project is a Python-based time-series analysis tool developed as part of a Python Developer assignment. It loads and validates OHLCV (Open, High, Low, Close, Volume) market data, performs technical analysis using Pandas and NumPy, detects market trends, generates statistical insights, and visualizes the results using Matplotlib.

---

## Features

### Data Loading & Validation
- Load OHLCV data from a CSV file
- Parse timestamps into datetime objects
- Check for missing values
- Detect duplicate timestamps
- Display dataset summary and statistics

### Time-Series Analysis
- Calculate 10-period Simple Moving Average (SMA10)
- Calculate 20-period Simple Moving Average (SMA20)
- Calculate percentage return from the previous closing price
- Calculate 20-period rolling volatility

### Trend Detection
Each row is classified as:

- **Uptrend** → Close Price > SMA20
- **Downtrend** → Close Price < SMA20
- **Neutral** → Close Price = SMA20

The application also calculates:
- Total number of rows in each trend
- Percentage of time spent in each trend

### Basic Analysis
The following statistics are generated:

- Largest single-period gain
- Largest single-period loss
- Highest closing price
- Lowest closing price
- Average trading volume

### Visualization
A line chart is generated showing:

- Closing Price
- SMA10
- SMA20

The chart is automatically saved to the `output` folder.

---

## Project Structure

```
python_assignment/
│
├── data/
│   └── sample_ohlcv_data.csv
│
├── output/
│   ├── chart.png
│   └── processed_data.csv
│
├── src/
│   ├── analyzer.py
│   └── main.py
│
├── requirements.txt
└── README.md
```

---

## Technologies Used

- Python 3
- Pandas
- NumPy
- Matplotlib
- Pathlib

---

## Approach

The project follows an object-oriented design by encapsulating all analysis logic inside the `OHLCVAnalyzer` class.

The workflow consists of:

1. Loading the dataset
2. Validating the data
3. Calculating technical indicators
4. Detecting market trends
5. Performing statistical analysis
6. Generating visualization
7. Exporting the processed dataset

Vectorized Pandas and NumPy operations are used instead of explicit loops wherever possible for improved readability and performance.

---

## Assumptions

- The input dataset contains the required OHLCV columns.
- Timestamps represent chronological market data.
- Rolling calculations naturally produce `NaN` values until sufficient observations are available.
- Percentage returns are calculated from consecutive closing prices.

---

## Output

Running the application generates:

- `output/chart.png`
- `output/processed_data.csv`

It also prints:

- Data validation summary
- Trend summary
- Basic statistical analysis

---

## Possible Improvements

Given more development time, the following improvements could be added:

- Command-line interface (CLI) support
- Configurable moving-average periods
- Additional technical indicators (RSI, MACD, Bollinger Bands)
- Unit tests
- Logging instead of print statements
- Interactive charts using Plotly
- Configuration through YAML or JSON files

---

## Author

**Samjith Krishnan**
Python fullstack Developer