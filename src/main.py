from analyzer import OHLCVAnalyzer


def main():
    analyzer = OHLCVAnalyzer("../data/sample_ohlcv_data.csv")

    analyzer.load_data()
    analyzer.validate_data()
    analyzer.calculate_indicators()
    analyzer.detect_trend()

    analyzer.trend_summary()
    analyzer.analyze()


    # analyzer.plot()
    # analyzer.save()


if __name__ == "__main__":
    main()