#! /usr/bin/python3
import argparse
from stock_chart_tools import get_historical_data, COLUMN_CLOSE, SMA

def main(symbol):
    stock_data = get_historical_data(symbol,30)
    stock_data["10daySMA"] = SMA(stock_data[COLUMN_CLOSE],10)
    print(stock_data)

if __name__ == "__main__":
    # Setup the argument parsing
    parser = argparse.ArgumentParser()
    parser.add_argument('-s','--symbol', dest='symbol', required=True,help="Stock ticker symbol")
    args = parser.parse_args()
    main(args.symbol)

