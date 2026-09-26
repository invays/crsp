import numpy as np
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from Enums.CompanyEnum import Company

# Global settings
# for pandas: fullscreen terminal parameters
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

def main():
    company_code = Company.AMAZON.value
    df_train = yf.Ticker(company_code).history(start='2020-1-1', end='2020-1-31')
    print(df_train.head().round(2))

if __name__ == "__main__":
    main()

# df = yf.Ticker('AAPL').history()


#
# print(df.head().round(2))


# for company in Enums().companies_list().values():
#     df = yf.Ticker(company).history()
#
#     print(df.head().round(2))
#
# def get_training_test_data(
#         stock='AMZN',
#         start='2019-1-1',
#         end='2021-1-31',
#         training_ratio=0.96):
#     df = yf.Ticker(stock).history(start=start, end=end)
#     df = df.iloc[:,:-3]
#     df.reset_index(inplace=True)
#     df['Date'] = [i.date() for i in df.Date]
#     df['fcc'] = [np.sign(df.Close.loc[i+1]-df.Close.loc[i]) for i in range(len(df)-1)]+[np.nan]
#     training_length = int(len(df)*training_ratio)
#     training_data = df.iloc[:training_length,:]
#     test_data = df.iloc[training_length:,:]
#     test_data.reset_index(inplace=True, drop=True)
#
#     return (training_data, test_data)
#
# print(get_training_test_data())


## github
# import os
# import sys

# if 'google.colab' in str(get_ipython()):
#
#     !git clone https://github.com
#
#     os.chdir('ваша_модель')
#     sys.path.append(os.getcwd())