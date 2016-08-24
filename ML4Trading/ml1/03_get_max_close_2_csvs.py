'''
Created on Feb 18, 2016

@author: mike
'''
import pandas as pd

def get_max_close(symbol):
    """ Return the mean volume for the stock indicated by symbol.
    
    Note:  Data for a stock is stored in the file: data/<symbol>.csv
    """
    df = pd.read_csv('/home/mike/Downloads/{}.csv'.format(symbol)) # read in data
    # TODO: Compute and return the mean volume for this stock
    return df['Close'].max() # compute and return max

def test_run():
    """Function called by Test Run."""
    for symbol in ['aapl','ibm']:
        print "Max Close"
        print symbol, get_max_close(symbol)
            
if __name__ == '__main__':
    test_run()