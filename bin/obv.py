#! /usr/bin/python3
import argparse
from stock_chart_tools import get_historical_data, COLUMN_CLOSE, COLUMN_VOLUME, OBV

def main(symbol):
    stock_data = get_historical_data(symbol)
    print(OBV(stock_data[COLUMN_CLOSE],stock_data[COLUMN_VOLUME]))

if __name__ == "__main__":
    # Setup the argument parsing
    parser = argparse.ArgumentParser()
    parser.add_argument('-s','--symbol', dest='symbol', required=True,help="Stock ticker symbol")
    args = parser.parse_args()
    main(args.symbol)

