# stock_chart_tools
Python module for calculating stock charts using yfinance and pandas

NAME
    stock_chart_tools

DESCRIPTION
    Functions to create data series for some technical indicators,
    which could be charted using various charting tools
    
        SMA  - Simple moving average
        EMA  - Exponential moving average
        MACD - Moving average convergence divergence
        OBV  - On balance volume
        SSO  - Slow stochastic Oscillator

FUNCTIONS
    EMA(data_series, periods)
        Calculate the exponential moving average 
        
        data_series -> pandas Series
        periods     -> the number of periods used to calculate
        
        Example:
            stock_data = get_historical_data(symbol)
            three_day_ema = EMA(stock_data['Close'],3)

    MACD(data_series, long_period=26, short_period=12, signal=9)
        Calculates the MACD (Moving Average Convergence Divergence)

        long_period  -> the number of periods for the long window
        short_period -> the number of periods for the short window
        signal       -> the number of periods to use for the signal line
        
        Example:
            stock_data = get_historical_data(symbol)
            macd = MACD(stock_data['Adj Close'])
    
    OBV(close_series, volume_series, days=60)
        Calculates the On Balance Volume
        
        close_series  -> pandas Series with the closing price data
        volume_series -> pandas Series with the volume data
        days          -> number of days to use to calculate
        
        Example:
            stock_data = get_historical_data(symbol)
            obv_data = OBV(stock_data['Adj Close'],stock_data['Volume'])
    
    SMA(data_series, periods)
        Calculate the simple moving average

        data_series -> pandas Series
        periods     -> the number of periods used to calculate
        
        Example:
            stock_data = get_historical_data(symbol)
            three_day_sma = SMA(stock_data['Volume'],3)
    
    SSO(close_series, high_series, low_series, period=14, k=3, d=3)
        Calculates the Slow Stochastic Oscillator
        
        period -> the number of periods for fast %K 
        k      -> the number of periods for %K
        d      -> the number of periods for %D
        
        Example:
            stock_data = get_historical_data(symbol)
            slow_stochastics = SSO(stock_data['Close'])
    
    get_historical_data(symbol, days=365)
        Get historical stock data using the yfinance module

        symbol -> ticker symbol
        days   -> number of *calendar* days of data to fetch

        The end date is the current date.

        Example:
            stock_data = get_historical_data(symbol)
            quarter_data = get_historical_data(symbol,90)
    
    get_historical_data_range(symbol, start_date, end_date)
        Get historical stock data using the yfinance module
        
        symbol     -> ticker symbol
        start_date -> python datetime object for the start of the series
        end_date   -> python datetime object for the end of the series
        
        Example:
            stock_data = get_historical_data_range(symbol,start_date,end_date)


