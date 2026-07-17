# Day04 AM: E-commerce User Data Cleaning (Main Exercise)
from pathlib import Path
import pandas as pd
import numpy as np

pd.set_option("display.max_columns", None)
pd.set_option("display.float_format", lambda x: f"{x:.2f}")

candidates = [Path("../data/E Commerce Dataset.xlsx"), Path("data/E Commerce Dataset.xlsx")]
DATA_PATH = next((p for p in candidates if p.exists()), None)
assert DATA_PATH is not None

df = pd.read_excel(DATA_PATH, sheet_name="E Comm")
print(f"Data: {DATA_PATH}, shape={df.shape}")
df.head()

# Task 1: Understand data
df.info()
print("\n1. One row = one user (CustomerID)")
print("2. ID field: CustomerID")
print("3. Target: Churn (0/1)")

# Task 2: Missing value report
missing_report = pd.DataFrame({
    "缺失数量": df.isna().sum(),
    "缺失比例(%)": (df.isna().mean() * 100).round(2)
})
missing_report = missing_report[missing_report["缺失数量"] > 0].sort_values("缺失数量", ascending=False)
print("\n=== Missing Report ===")
print(missing_report.to_string())

# Task 3: Duplicate check
duplicate_rows = df.duplicated().sum()
duplicate_customer_ids = df.duplicated(subset=["CustomerID"]).sum()
print(f"\nDuplicate rows: {duplicate_rows}")
print(f"Duplicate CustomerID: {duplicate_customer_ids}")
print("Note: Cannot delete CustomerID dupes blindly - need to check reason first")

# Task 4: Fill numeric missing with median
numeric_missing_cols = [
    "Tenure", "WarehouseToHome", "HourSpendOnApp",
    "OrderAmountHikeFromlastYear", "CouponUsed",
    "OrderCount", "DaySinceLastOrder",
]
for col in numeric_missing_cols:
    med = df[col].median()
    df[col] = df[col].fillna(med)
    print(f"{col}: filled with median {med:.2f}")
print(f"\nRemaining missing:\n{df[numeric_missing_cols].isna().sum()}")
print("\nThink: When NOT to use median? Category fields - use mode or 'unknown' label instead")

# Task 5-6: Category standardization
category_cols = ["PreferredLoginDevice", "PreferredPaymentMode", "PreferedOrderCat"]
print("\n=== Before Standardization ===")
for col in category_cols:
    print(f"\n{col}:\n{df[col].value_counts()}")

df["PreferredLoginDevice"] = df["PreferredLoginDevice"].replace({"Phone": "Mobile Phone"})
df["PreferredPaymentMode"] = df["PreferredPaymentMode"].replace({"COD": "Cash on Delivery", "CC": "Credit Card"})
df["PreferedOrderCat"] = df["PreferedOrderCat"].replace({"Mobile": "Mobile Phone"})

print("\n=== After Standardization ===")
for col in category_cols:
    print(f"\n{col}:\n{df[col].value_counts()}")

# Task 7: IQR outlier check
def iqr_outlier_summary(series):
    s = series.dropna()
    q1, q3 = s.quantile(0.25), s.quantile(0.75)
    iqr = q3 - q1
    return pd.Series({"Q1": q1, "Q3": q3, "下限": q1-1.5*iqr, "上限": q3+1.5*iqr, "候选异常值数量": ((s < q1-1.5*iqr) | (s > q3+1.5*iqr)).sum()})

for f in ["WarehouseToHome", "OrderCount", "CashbackAmount"]:
    print(f"\n{f}:\n{iqr_outlier_summary(df[f])}")
print("\nConclusion: Outliers should NOT be deleted blindly - may be real extreme cases")

# Task 8: Business rules
rules = {
    "使用时长<0": int((df["HourSpendOnApp"] < 0).sum()),
    "仓库距离<0": int((df["WarehouseToHome"] < 0).sum()),
    "订单数<=0": int((df["OrderCount"] <= 0).sum()),
    "返现金额<0": int((df["CashbackAmount"] < 0).sum()),
}
print(f"\nBusiness rules:\n{pd.Series(rules)}")

# Verification & Export
assert df[numeric_missing_cols].isna().sum().sum() == 0, "Numeric fields still have missing"
assert "Phone" not in df["PreferredLoginDevice"].unique()
assert "COD" not in df["PreferredPaymentMode"].unique()
assert "CC" not in df["PreferredPaymentMode"].unique()

OUTPUT_PATH = Path("../output/ecommerce_customer_cleaned.csv")
OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(OUTPUT_PATH, index=False, encoding="utf-8-sig")
print(f"\nExported: {OUTPUT_PATH.resolve()}")
print(f"Rows: {len(df)}, Cols: {df.shape[1]}")



