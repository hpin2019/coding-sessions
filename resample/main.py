import pandas as pd
from pathlib import Path
import traceback


FILENAME="./data.csv"
df = None
ohlc_dict = {
    'open':'first',
    'high':'max',
    'low':'min',
    'close':'last',
    'volume':'sum'
    }



def check_file():
    try:
        filename = Path(FILENAME)
        if filename.is_file():
            return True
        else:
            print("File not found "+filepath)
            return False
    except Exception as e:
        print("Error reading data fromx CSV")
        print(e)
    return False


def read_eod_data():
    global df
    try:
        df = pd.read_csv(FILENAME,parse_dates=['date'])
        df.set_index("date", inplace=True)
        print("==== EOD Data ====")
        print(df.tail(10))
        return True
    except Exception as e:
        print("Error reading data fromx CSV")
        print(e)
        print(traceback.format_exc())
        err_msg = "Internal error"
    return False


def resample_last7days():
    global df, ohlc_dict
    last_date = df.index.to_pydatetime()[-1]
    #print(str(last_date))
    last_day = get_weekday(last_date)
    if not last_day:
        print("Cannot get correct day for weekly calc")
        return
    print("last day is "+last_day)
    
    re_df = pd.DataFrame(None)
    print("\n===========Resampling for Last 7 days===========")
    
    re_df = df.resample(last_day).agg(ohlc_dict)

    re_df.dropna(subset = ['close'],inplace=True)
    print(re_df.tail())


def resample_weekly():
    global df, ohlc_dict
    re_df = pd.DataFrame(None)
    print("\n===========Resampling for Weekly===========")
    
    re_df = df.resample("W").agg(ohlc_dict)

    re_df.dropna(subset = ['close'],inplace=True)
    print(re_df.tail())


def resample_monthly():
    global df, ohlc_dict
    re_df = pd.DataFrame(None)
    print("\n===========Resampling for Monthly===========")
    
    re_df = df.resample("M").agg(ohlc_dict)

    re_df.dropna(subset = ['close'],inplace=True)
    print(re_df.tail())


def get_weekday(last_date):
    weekday_map = ['W-Mon','W-Tue','W-Wed','W-Thu','W-Fri','W-Sat','W-Sun']
    if last_date:
        #print("last day is "+str(last_date.weekday()))
        return weekday_map[last_date.weekday()]
    return None

if __name__ == '__main__':
    if not check_file():
        print("File not found")
    if not read_eod_data():
        print("Error reading data")
    resample_weekly()
    resample_last7days()
    resample_monthly()