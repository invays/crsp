import numpy as np
import yfinance as yf
from pandas import DataFrame



class YahooFinanceProvider:
    # Pandas documentation
    # https://pandas.pydata.org/docs/reference/general_functions.html

    def __init__(self, code: str, start_date:str, end_date:str):
        self.code = code
        self.start_date = start_date
        self.end_date = end_date
        self.df_train = None|DataFrame

    def fetch(self) -> DataFrame:
        data_frame = yf.Ticker(self.code).history(start=self.start_date, end=self.end_date)

        self.df_train = self.df_filter(data_frame)
        self.df_train['fcc'] = np.sign(self.df_train['Close'].shift(-1)-self.df_train['Close'])


        # self.df_train['fcc_old'] = [
        #                     np.sign(self.df_train.Close.loc[i + 1] - self.df_train.Close.loc[i])
        #                            for i in range(len(self.df_train) - 1)
        #             ] + [np.nan]

        print(self.df_train)

        return self.df_train.head().round(2)

    def df_filter(self, df: DataFrame) -> DataFrame:
        #df = df.iloc[:,:-3] # remove last 3 columns
        df.drop(columns=['Stock Splits', 'Volume', 'Dividends'], inplace=True)
        df.reset_index(inplace=True) # reset indexes to numerical values move date to column
        # df['Date'] = [i.date() for i in df.Date]
        df['Date'] = df['Date'].dt.date # only date allows
        return df