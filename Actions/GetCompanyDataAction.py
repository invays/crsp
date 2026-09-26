import numpy as np
import yfinance as yf
import pandas as pd

class GetCompanyDataAction:
    def __init__(self, code: str, name: str = '', start_date: str = '2020-1-1', end_date: str = '2020-1-31'):
        self.name = name
        self.code = code
        self.start_date = start_date
        self.end_date = end_date

    def execute(self) -> None:
        df_train = yf.Ticker(self.code).history(start=self.start_date, end=self.end_date)
        print(df_train.head().round(2))