#! /usr/bin/python3
import argparse
from stock_chart_tools.utils import get_historical_data, COLUMN_CLOSE, EMA

def main(symbol):
    stock_data = get_historical_data(symbol)
    stock_data["3dayEMA"] = EMA(stock_data[COLUMN_CLOSE],3)
    print(stock_data)

if __name__ == "__main__":
    # Setup the argument parsing
    parser = argparse.ArgumentParser()
    parser.add_argument('-s','--symbol', dest='symbol', required=True,help="Stock ticker symbol")
    args = parser.parse_args()
    main(args.symbol)

