from Actions.GetCompanyDataAction import GetCompanyDataAction
from Enums.CompanyEnum import Company
import matplotlib.pyplot as plt
from Helpers.CandlestickHelper import CandlestickEncoder
import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

def main():
    GetCompanyDataAction(Company.AMAZON.value).execute()
    # print(f"pattern: {CandlestickEncoder(10, 4, 6, 1).encoder()}")
    # CandlestickEncoder(10, 3, 7, 1).cs_visualize(details=True)

if __name__ == "__main__":
    main()