import numpy as np
import pandas as pd

from Providers.YahooFinanceProvider import YahooFinanceProvider


class GetCompanyDataAction:
    def __init__(self, code: str, name: str = '', start_date: str = '2020-1-1', end_date: str = '2020-1-31'):
        self.name = name
        self.code = code
        self.start_date = start_date
        self.end_date = end_date

    def info(self):
        datas = YahooFinanceProvider(self.code, self.start_date, self.end_date).fetch()
        print(datas)
