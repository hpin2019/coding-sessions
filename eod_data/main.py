import yfinance as yf
import pandas as pd
from pathlib import Path

FILENAME="./data.csv"

#bank nifty : ^NSEBANK
#nifty : ^NSEI
def get_historical_data(symbol):
    ## If file exists, no need to read old data.
    filename = Path(FILENAME)
    if not filename.is_file():
        print("Reading historical data from 1st Jan 2022")
        stock = yf.Ticker(symbol)
        df = stock.history(start='2022-01-01',end='2022-08-14')

        print(df.tail())
        print(df.shape)
        #print(df.index)
        df.drop(['Dividends','Stock Splits'],axis=1,inplace=True)
        df.index.rename('date', inplace=True)
        df.columns = ["open","high","low","close","volume"]
        df.to_csv(FILENAME,float_format='%.2f',index=True)
        df = pd.DataFrame(None)  
    else:
        print(">>>>>  Historical data already available, not getting again <<<<<<")



def get_recent_data(symbol):
    stock = yf.Ticker(symbol)
    df = stock.history('5d')
    print("Received last 5 days data")
    
    df.drop(['Dividends','Stock Splits'],axis=1,inplace=True)
    
    #print(df.tail())
    #print(df.dtypes)
    filename = Path(FILENAME)
    if filename.is_file():
        df.reset_index(inplace=True)
        print(df.tail())
        df.columns = ["date","open","high","low","close","volume"]
        csv_df = pd.read_csv(FILENAME)
        print("Existing data from CSV file")
        print(csv_df.tail())
        csv_df['date'] = csv_df['date'].astype('datetime64[ns]')
        #print(csv_df.dtypes)

        #df = pd.concat( [df, csv_df], axis=1) 
        print("Merging latest data with CSV file data")
        df = pd.concat([csv_df,df],ignore_index=True)
        
        print(df.shape)
        #print(df.tail())
        # Must drop duplicate data.
        df = df.drop_duplicates(subset=["date"], keep='last',ignore_index=True)
        df.sort_values(by=["date"],ascending=True,ignore_index=True,inplace=True)
        print("After drop and sort")
        print(df.shape)
        #print(df.tail())

        #Store again.
        df.set_index("date", inplace=True)
        df.to_csv(FILENAME,float_format='%.2f',index=True)
    else:
        print("Historical data not available")
        df.index.rename('date', inplace=True)
        df.columns = ["open","high","low","close","volume"]
        df.to_csv(FILENAME,float_format='%.2f',index=True)



if __name__ == '__main__':
    symbol = 'TSLA'
    get_historical_data(symbol)
    get_recent_data(symbol)

