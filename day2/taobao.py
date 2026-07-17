import pandas as pd
import numpy as np


csv_path = r"C:\Users\a1098\Desktop\firstgame\shixi\muc-commerce-3-24012453\data\淘宝全品类全国数据.csv"
excel_path = r"C:\Users\a1098\Desktop\firstgame\shixi\muc-commerce-3-24012453\data\淘宝全品类全国数据.xlsx"


df_csv = pd.read_csv(csv_path)
df_excel = pd.read_excel(excel_path)

target_col = "商品价格"
prices = df_csv[target_col].to_numpy()
prices1 = df_excel[target_col].to_numpy()

print('商品价格低于500：', np.sum(prices < 500), np.sum(prices1 < 500))
print('商品价格高于500小于1000：', np.sum((prices >= 500) & (prices < 1000)), np.sum((prices1 >= 500) & (prices1 < 1000)))