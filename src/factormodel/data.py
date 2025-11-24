"""
Tools for pulling and processing data used for factor modeling.
"""

import pandas as pd
import yfinance as yf

from utils import get_logger

logger = get_logger(__name__)

def fetch_raw_data(tickers: str | list, interval: str = '1d', start: str = None, end: str = None) -> pd.DataFrame:
    """
    Pull data from Yahoo! Finance's API

    Args:
        tickers (str | list): List of tickers to download if multiple tickers. Else the ticker as a string.
        start (str): Start date of data, formatted 'yyyy-mm-dd'
        end (str): End date of data, formatted' yyyy-mm-dd'
        interval (str): Time between data points, eg '1m', '5m', '1d'.
    
    Returns:
        pd.DataFrame: OHLC and volume data
    """
    data = yf.download(tickers=tickers, interval=interval, start=start, end=end)
    
    if _verify_yf_data(data):
        return data
    
    return pd.DataFrame()
    
def clean_data():
    pass

def _verify_yf_data(data: pd.DataFrame) -> bool:

    if not data.equals(data.dropna(inplace=False)):
        logger.warning("NaN rows detected in YFinance data.")
    
    if data.empty:
        logger.error("YFinance data is empty.")
        return False
    
    return True

if __name__ == "__main__":
    print(fetch_raw_data(['TSLA', 'CRWV'], start='2022-01-01'))
