"""Slice and plot"""

import os
import pandas as pd
import matplotlib.pyplot as plt


def plot_selected(df, columns, start_index, end_index):
    """Plot the desired columns over index values in the given range."""
    plot_data(df.ix[start_index:end_index,columns],title="Selected data")
    
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

def normalize_data(df):
    """Normalize stock prices by dividing the price by itself for 
    the first date for each stock"""
    return df/ df.ix[0,:] # Divide by first row 
    
def plot_data(df, title="Stock prices"):
    """Plot stock prices with a custom title and meaningful axis labels."""
    ax = df.plot(title=title, fontsize=12)
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    plt.show()


def test_run():
    # Define a date range
    dates = pd.date_range('2010-01-01', '2010-12-31')

    # Choose stock symbols to read
    symbols = ['goog', 'ibm', 'aapl']  # SPY will be added in get_data()
    
    # Get stock data
    df = get_data(symbols, dates)

    df = normalize_data(df)
    
    # Slice and plot
    plot_selected(df, ['spy', 'ibm'], '2010-03-01', '2010-04-01')


if __name__ == "__main__":
    test_run()
