import numpy as np
import pandas as pd
from pandas import DataFrame

from Helpers.CandlestickHelper import CandlestickEncoder
from Providers.YahooFinanceProvider import YahooFinanceProvider


class GetCompanyDataAction:
    def __init__(self, code: str, name: str = '', start_date: str = '2020-1-1', end_date: str = '2020-1-31'):
        self.name = name
        self.code = code
        self.start_date = start_date
        self.end_date = end_date

    def execute(self):
        datas = YahooFinanceProvider(self.code, self.start_date, self.end_date).fetch()
        # self.df_encoder(datas)
        datas = self.df_encoder(datas)

        for x, i in enumerate(datas.index):
            hp, op, cp, lp = datas[['High', 'Open', 'Close', 'Low']].loc[i]
            CandlestickEncoder(hp, op, cp, lp).cs_visualize(x=x)

    def df_encoder(self, df: DataFrame) -> DataFrame:
        data_ = df.copy()
        encoder_list = []
        for i in data_.index:
            hp, op, cp, lp = data_[['High', 'Open', 'Close', 'Low']].loc[i]
            encoder_list.append(CandlestickEncoder(high_price=hp, open_price=op, close_price=cp, low_price=lp).encoder())

        # print(encoder_list)

        data_['code'] = encoder_list
        return data_
