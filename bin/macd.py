#! /usr/bin/python3
import argparse
from stock_chart_tools.utils import get_historical_data, COLUMN_CLOSE, MACD

def main(symbol):
    stock_data = get_historical_data(symbol)
    print(MACD(stock_data[COLUMN_CLOSE]))

if __name__ == "__main__":
    # Setup the argument parsing
    parser = argparse.ArgumentParser()
    parser.add_argument('-s','--symbol', dest='symbol', required=True,help="Stock ticker symbol")
    args = parser.parse_args()
    main(args.symbol)

