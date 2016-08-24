'''
Created on Feb 19, 2016

@author: mike
'''
import pandas as pd

def test_run():
    start_date = '2009-01-22'
    end_date = '2010-01-26'
    dates = pd.date_range(start_date,end_date)
    
    # Create an empty dataframe
    df1=pd.DataFrame(index=dates)
    
    # Read SPY data into temporary dataframe
    dfSPY = pd.read_csv("/media/mike/9016-4EF8/Python-MLTrading/Workspace/ml1/spy.csv",index_col='Date',
                        parse_dates=True,usecols=['Date','Adj Close'],
                        na_values=['nan'])
    
    # Rename 'Adj Close' column to 'spy' to prevent clash
    dfSPY = dfSPY.rename(columns={'Adj Close':'spy'})
    # Join the two data frames using DataFrame.join() 
    
    # Note: This does a left join by default
    df1 = df1.join(dfSPY,how='inner')
    
    # Read in more stocks
    symbols = ['goog', 'ibm', 'aapl']
    
    for symbol in symbols:
        df_temp = pd.read_csv("/media/mike/9016-4EF8/Python-MLTrading/Workspace/ml1/{}.csv".format(symbol),
                              index_col = 'Date',parse_dates=True,
                              usecols=['Date','Adj Close'])
        # rename to avoid clash
        df_temp = df_temp.rename(columns={'Adj Close': symbol})
    
        # Drop NaN Values or do an inner join
        #df1 = df1.dropna()
        df1 = df1.join(df_temp) #use default left join
        df1 = df1.sort_index()
        
    # Slice by row range (dates) using DataFrame.ix[] selector
    print df1.ix['2010-01-01':'2010-01-20'] 
    
    # Slice by column (symbols)
    print df1['goog'] # Single column
    print df1[['ibm','aapl']] # List of labels selects multiple columns
    
    # Slice by row and column
    print df1.ix['2010-01-10':'2010-01-20',['spy','ibm']]
    
if __name__ == '__main__':
    test_run()