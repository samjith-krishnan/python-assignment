from pathlib import Path
from typing import Optional
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


class OHLCVAnalyzer:
    """
    Analyze OHLCV time-series data.
    """

    def __init__(self, file_path: str):
        self.file_path = Path(file_path)
        self.df:Optional[pd.DataFrame]=None

    def _ensure_data_loaded(self) -> None:
        """
        Ensure the dataset has been loaded.
        """
        if self.df is None:
            raise ValueError("Dataset not loaded")

    def load_data(self) -> None:
        """
        Load the OHLCV dataset and parse timestamps.
        """
        self.df = pd.read_csv(
            self.file_path,
            parse_dates=["timestamp"]
    )

        self.df.sort_values("timestamp", inplace=True)
        self.df.reset_index(drop=True, inplace=True)

        print(" Dataset loaded successfully.")



    def validate_data(self) -> None:
        """
        Validate the dataset by checking missing values,
        duplicate timestamps, and displaying a summary.
        """

        self._ensure_data_loaded()

        print("\n" + "=" * 50)
        print("DATA VALIDATION")
        print("=" * 50)


        print("\nMissing Values:")
        print(self.df.isnull().sum())

    
        duplicate_count = self.df["timestamp"].duplicated().sum()
        print(f"\nDuplicate timestamps: {duplicate_count}")

  
        print("\nDataset Info:")
        self.df.info()


        print("\nStatistical Summary:")
        print(self.df.describe())

        print("\nFirst 5 Rows:")
        print(self.df.head())

        

    def calculate_indicators(self) -> None:
        """
        Calculate moving averages, returns, and rolling volatility.
        """
        self._ensure_data_loaded()

     
        self.df["SMA10"] = (
            self.df["close"]
            .rolling(window=10)
            .mean()
        )

        self.df["SMA20"] = (
            self.df["close"]
            .rolling(window=20)
            .mean()
        )

        self.df["Return"] = (
            self.df["close"]
            .pct_change()
            * 100
        )

        self.df["Volatility"] = (
            self.df["Return"]
            .rolling(window=20)
            .std()
        )

        print("\n Technical indicators calculated successfully.")



    def detect_trend(self):
        """Detect market trend."""
        pass

    def analyze(self):
        """Generate statistical analysis."""
        pass

    def plot(self):
        """Plot closing prices with moving averages."""
        pass

    def save(self):
        """Save processed dataset."""
        pass