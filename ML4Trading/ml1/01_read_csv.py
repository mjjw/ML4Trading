'''
Created on Feb 18, 2016

@author: mike
'''
import pandas as pd

def test_run():
    df = pd.read_csv('/home/mike/Downloads/aapl.csv')
    print df[10:21] #print entire dataframe
    
if __name__ == '__main__':
    test_run()