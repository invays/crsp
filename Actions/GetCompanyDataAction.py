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
        datas = self.change_points(datas)
        segmets = self.segmentation(datas)
        print(segmets)

        for x, i in enumerate(datas.index):
            hp, op, cp, lp = datas[['High', 'Open', 'Close', 'Low']].loc[i]
            CandlestickEncoder(hp, op, cp, lp).cs_visualize(x=x)

    def df_encoder(self, data: DataFrame) -> DataFrame:
        encoder_list = []
        for i in data.index:
            hp, op, cp, lp = data[['High', 'Open', 'Close', 'Low']].loc[i]
            encoder_list.append(CandlestickEncoder(high_price=hp, open_price=op, close_price=cp, low_price=lp).encoder())

        # print(encoder_list)

        data['code'] = encoder_list
        return data

    def change_points(self, data: DataFrame) -> DataFrame:
        change_pts, change_types = [True], ['Start']

        left_change = np.sign(data['Close'] - data['Close'].shift(1))
        right_change = np.sign(data['Close'].shift(-1) - data['Close'])
        # print(left_change, right_change)


        # for i in range(1, len(data) - 1):
        #
        #     left_change = int(np.sign(data['Close'][i] - data['Close'][i - 1]))
        #     right_change = int(np.sign(data['Close'][i + 1] - data['Close'][i]))
        #
        #     if left_change != right_change:
        #         change_pts.append(True)
        #     else:
        #         change_pts.append(False)
        #
        #     change_types.append((left_change, right_change))
        #
        # change_pts.append(False)
        # change_types.append('End')

        data['change_points'] = (left_change != right_change)

        data['prev_direction'] = left_change
        data['next_direction'] = right_change

        data.dropna(subset=['prev_direction', 'next_direction'], inplace=True)
        data.reset_index(drop=True, inplace=True)
        # data['change_types'] = change_types

        return data

    def segmentation(self, data: DataFrame) -> DataFrame:
        segment_list, trend_list = [], []
        pattern = ''

        for i in range(len(data) - 1):
            pattern += data.code[i]

            if data.change_points.loc[i]:
                segment_list.append(pattern)
                j = i
                while j < len(data):
                    direction = data['prev_direction'].iloc[j]

                    if direction != 0:
                        trend_list.append(direction)
                        break

                    j += 1

                pattern = ''

        df_seg = pd.DataFrame()
        df_seg['kts'] = segment_list
        df_seg['trend'] = trend_list

        df_seg_unique = pd.DataFrame(df_seg.value_counts()).reset_index()

        return df_seg_unique