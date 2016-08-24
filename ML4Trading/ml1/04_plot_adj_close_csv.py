'''
Created on Feb 19, 2016

@author: mike
'''
import pandas as pd
import matplotlib.pyplot as plt

def test_run():
    df = pd.read_csv('/home/mike/Downloads/aapl.csv')
    """
    NOTE: The data frame is not sorted.
    """
    
    print df['Adj Close']
    df[['Close', 'Adj Close']].plot()
    plt.show()  # must be called to show plots
          
if __name__ == '__main__':
    test_run()