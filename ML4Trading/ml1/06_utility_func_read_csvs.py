import os
import pandas as pd

def symbol_to_path(symbol, base_dir="/media/mike/9016-4EF8/Python-MLTrading/Workspace/ml1"):
    """Return CSV file path given ticker symbol."""
    return os.path.join(base_dir, "{}.csv".format(str(symbol)))


def get_data(symbols, dates):
    """Read stock data (adjusted close) for given symbols from CSV files."""
    df = pd.DataFrame(index=dates)
    if 'spy' not in symbols:  # add SPY for reference, if absent
        symbols.insert(0, 'spy')

    for symbol in symbols:
        df_temp = pd.read_csv(symbol_to_path(symbol), index_col='Date',
                parse_dates=True, usecols=['Date', 'Adj Close'], na_values=['nan'])
        df_temp = df_temp.rename(columns={'Adj Close': symbol})
        df = df.join(df_temp)
        if symbol == 'spy':  # drop dates SPY did not trade
            df = df.dropna(subset=["spy"])

    return df

def test_run():
    # Define a date range
    dates = pd.date_range('2010-01-01', '2010-12-31')

    # Choose stock symbols to read
    symbols = ['goog', 'ibm', 'aapl']  # SPY will be added in get_data()
    
    # Get stock data
    df = get_data(symbols, dates)
    print df
    
if __name__ == '__main__':
    test_run()