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
        self.output_dir = Path("output")
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.df = None

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



    def detect_trend(self) -> None:
        """
        Detect market trend based on the 20-period SMA.
        """
        self._ensure_data_loaded()

        conditions = [
            self.df["close"] > self.df["SMA20"],
            self.df["close"] < self.df["SMA20"],
        ]

        choices = [
            "uptrend",
            "downtrend",
        ]

        self.df["trend"] = np.select(
            conditions,
            choices,
            default="neutral",
        )

        print("\n Trend detection completed.")


    def trend_summary(self) -> None:
        """
        Display trend counts and percentages.
        """
        self._ensure_data_loaded()

        print("\n" + "=" * 50)
        print("TREND SUMMARY")
        print("=" * 50)

        counts = self.df["trend"].value_counts()

        percentages = (
            self.df["trend"]
            .value_counts(normalize=True)
            .mul(100)
            .round(2)
        )

        summary = pd.DataFrame({
            "Count": counts,
            "Percentage": percentages
        })

        print(summary)



    def analyze(self) -> None:
        """
        Perform basic statistical analysis on the OHLCV data.
        """
        self._ensure_data_loaded()

        analysis = {
            "Largest Single-Period Gain (%)": self.df["Return"].max(),
            "Largest Single-Period Loss (%)": self.df["Return"].min(),
            "Highest Closing Price": self.df["close"].max(),
            "Lowest Closing Price": self.df["close"].min(),
            "Average Volume": self.df["volume"].mean(),
        }

        print("\n" + "=" * 50)
        print("BASIC ANALYSIS")
        print("=" * 50)

        for metric, value in analysis.items():
            if isinstance(value, float):
                print(f"{metric:<35}: {value:.2f}")
            else:
                print(f"{metric:<35}: {value}")



    def plot(self) -> None:
        """
        Plot the closing price with SMA10 and SMA20.
        """
        self._ensure_data_loaded()

        plt.figure(figsize=(15, 7))

        plt.plot(
            self.df["timestamp"],
            self.df["close"],
            label="Close Price",
            linewidth=1.5,
        )

        plt.plot(
            self.df["timestamp"],
            self.df["SMA10"],
            label="SMA 10",
            linewidth=2,
        )

        plt.plot(
            self.df["timestamp"],
            self.df["SMA20"],
            label="SMA 20",
            linewidth=2,
        )

        plt.title("OHLCV Closing Price with Moving Averages")
        plt.xlabel("Timestamp")
        plt.ylabel("Price")

        plt.grid(True)

        plt.legend()

        plt.tight_layout()

        plt.savefig(self.output_dir / "chart.png", dpi=300)
        plt.show()
        print("\n Chart saved to output/chart.png")

    def save(self) -> None:
        """
        Save the processed dataset.
        """
        self._ensure_data_loaded()

        self.df.to_csv(
        self.output_dir / "processed_data.csv",
        index=False
    )

        print("Processed dataset saved to output/processed_data.csv")