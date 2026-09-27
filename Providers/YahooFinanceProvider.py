import numpy as np
import yfinance as yf
from pandas import DataFrame



class YahooFinanceProvider:

    def __init__(self, code: str, start_date:str, end_date:str):
        self.code = code
        self.start_date = start_date
        self.end_date = end_date
        self.df_train = None|DataFrame

    def fetch(self) -> DataFrame:
        data_frame = yf.Ticker(self.code).history(start=self.start_date, end=self.end_date)
        self.df_train = self.df_filter(data_frame)

        self.df_train['fcc'] = [np.sign(self.df_train.Close.loc[i + 1] - self.df_train.Close.loc[i]) for i in
                           range(len(self.df_train) - 1)] + [np.nan]

        return self.df_train.head().round(2)

    def df_filter(self, df: DataFrame) -> DataFrame:
        df = df.iloc[:,:-3] # remove last 3 colums
        df.reset_index(inplace=True) # reset indexes
        df['Date'] = [i.date() for i in df.Date] # remove time

        return df