# Day04 AM Extension: Taobao Product Data Cleaning
from pathlib import Path
import pandas as pd
import numpy as np

pd.set_option("display.max_columns", None)
pd.set_option("display.float_format", lambda x: f"{x:.2f}")

candidates = [Path("../data/淘宝全品类全国数据.csv"), Path("data/淘宝全品类全国数据.csv")]
DATA_PATH = next((p for p in candidates if p.exists()), None)
assert DATA_PATH is not None

taobao = pd.read_csv(DATA_PATH)
print(f"Data: {DATA_PATH}, shape={taobao.shape}")
taobao.head()

# Task 1: Data quality check
taobao.info()
missing_report = pd.DataFrame({
    "缺失数量": taobao.isna().sum(),
    "缺失比例(%)": (taobao.isna().mean() * 100).round(2)
})
missing_report = missing_report[missing_report["缺失数量"] > 0].sort_values("缺失数量", ascending=False)
print(f"\nMissing:\n{missing_report.to_string()}")
print(f"\nDuplicate rows: {taobao.duplicated().sum()}")
print(f"\nSales values:\n{taobao['商品销量'].value_counts()}")

# Task 2: Clean product ID whitespace
print(f"\nBefore: {repr(taobao.loc[0, '商品id'])}")
taobao["商品id"] = taobao["商品id"].astype(str).str.strip()
print(f"After: {repr(taobao.loc[0, '商品id'])}")

# Task 3: Fill missing by business meaning
service_cols = ["先用后付", "退货宝"]
attribute_cols = ["风格", "面料", "版型", "适用季节"]
for col in service_cols:
    taobao[col] = taobao[col].fillna("未提供")
for col in attribute_cols:
    taobao[col] = taobao[col].fillna("未标注")
print(f"\nAfter fill:\n{taobao[service_cols + attribute_cols].isna().sum()}")

# Task 4: Sales text to number
def sales_lower_bound(value):
    value = str(value).replace("+人付款", "")
    if "万" in value:
        return float(value.replace("万", "")) * 10000
    return float(value)

taobao["销量下限"] = taobao["商品销量"].apply(sales_lower_bound)
print(f"\nSales conversion:\n{taobao[['商品销量', '销量下限']].drop_duplicates().sort_values('销量下限').to_string()}")

# Task 5: Price tiers and outlier check
def iqr_outlier_summary(series):
    s = series.dropna()
    q1, q3 = s.quantile(0.25), s.quantile(0.75)
    iqr = q3 - q1
    return pd.Series({"Q1": q1, "Q3": q3, "下限": q1-1.5*iqr, "上限": q3+1.5*iqr, "候选异常值数量": ((s < q1-1.5*iqr) | (s > q3+1.5*iqr)).sum()})

print(f"\nPrice outliers:\n{iqr_outlier_summary(taobao['商品价格'])}")

bins = [0, 100, 500, 1000, 3000, np.inf]
labels = ["0-100元", "100-500元", "500-1000元", "1000-3000元", "3000元以上"]
taobao["价格区间"] = pd.cut(taobao["商品价格"], bins=bins, labels=labels, right=True)
print(f"\nPrice tiers:\n{taobao['价格区间'].value_counts().sort_index()}")
print("Note: High-price items may be normal - don't delete based on IQR alone")

# Verification & Export
assert taobao[service_cols + attribute_cols].isna().sum().sum() == 0
assert "销量下限" in taobao.columns
assert "价格区间" in taobao.columns

OUTPUT_PATH = Path("../output/taobao_product_cleaned.csv")
OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
taobao.to_csv(OUTPUT_PATH, index=False, encoding="utf-8-sig")
print(f"\nExported: {OUTPUT_PATH.resolve()}")
print(f"Rows: {len(taobao)}, Cols: {taobao.shape[1]}")


