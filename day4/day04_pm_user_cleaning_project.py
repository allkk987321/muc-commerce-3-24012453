# Day04 PM: E-commerce User Data Cleaning Project
from pathlib import Path
import numpy as np
import pandas as pd

pd.set_option("display.max_columns", None)
pd.set_option("display.float_format", lambda x: f"{x:.2f}")

# 1. Read data
candidates = [Path("../data/E Commerce Dataset.xlsx"), Path("data/E Commerce Dataset.xlsx")]
DATA_PATH = next((p for p in candidates if p.exists()), None)
assert DATA_PATH is not None, "Data file not found"

PROJECT_ROOT = Path.cwd().parent
OUTPUT_DIR = PROJECT_ROOT / "output" / "day04_project"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

raw_df = pd.read_excel(DATA_PATH, sheet_name="E Comm")
print(f"Loaded: {DATA_PATH}, shape={raw_df.shape}")

# 2. Quality report
def build_quality_report(data):
    return pd.DataFrame({
        "数据类型": data.dtypes,
        "缺失数量": data.isna().sum(),
        "缺失比例(%)": (data.isna().mean() * 100).round(2),
        "唯一值数量": data.nunique()
    })

quality_before = build_quality_report(raw_df)
print("\n=== Quality Before ===")
print(quality_before.to_string())

# 3. Initial audit
print(f"\nDuplicate rows: {raw_df.duplicated().sum()}")
print(f"Duplicate CustomerID: {raw_df.duplicated(subset=['CustomerID']).sum()}")
print(f"\nChurn:\n{raw_df['Churn'].value_counts()}")
print(f"Churn rate: {raw_df['Churn'].value_counts().get(1, 0) / len(raw_df) * 100:.2f}%")

for col in ["PreferredLoginDevice", "PreferredPaymentMode", "PreferedOrderCat"]:
    print(f"\n{col}:\n{raw_df[col].value_counts()}")

# 4. Cleaning config
NUMERIC_MISSING_COLS = [
    "Tenure", "WarehouseToHome", "HourSpendOnApp",
    "OrderAmountHikeFromlastYear", "CouponUsed",
    "OrderCount", "DaySinceLastOrder",
]

CATEGORY_MAPPINGS = {
    "PreferredLoginDevice": {"Phone": "Mobile Phone"},
    "PreferredPaymentMode": {"COD": "Cash on Delivery", "CC": "Credit Card"},
    "PreferedOrderCat": {"Mobile": "Mobile Phone"}
}

# 5. Reusable cleaning function
def clean_ecommerce_data(data):
    df = data.copy()
    logs = []

    rows_before = len(df)
    df = df.drop_duplicates()
    logs.append({"step": "drop_duplicates", "before": rows_before, "after": len(df), "affected": rows_before - len(df)})

    for col in NUMERIC_MISSING_COLS:
        missing = df[col].isna().sum()
        if missing > 0:
            med = df[col].median()
            df[col] = df[col].fillna(med)
            logs.append({"step": f"fillna({col})", "before": len(df), "after": len(df), "affected": missing, "value": med})

    for col, mapping in CATEGORY_MAPPINGS.items():
        for old, new in mapping.items():
            cnt = (df[col] == old).sum()
            if cnt > 0:
                df[col] = df[col].replace({old: new})
                logs.append({"step": f"replace({col})", "before": len(df), "after": len(df), "affected": cnt, "rule": f"{old} -> {new}"})

    df["Churn"] = df["Churn"].astype(int)
    df["Complain"] = df["Complain"].astype(int)
    return df, pd.DataFrame(logs)

cleaned_df, cleaning_log = clean_ecommerce_data(raw_df)
print("\n=== Cleaning Log ===")
print(cleaning_log.to_string(index=False))

# 6. Feature engineering
tenure_bins = [0, 5, 10, 15, 20, 25, 30, np.inf]
tenure_labels = ["0-5年", "5-10年", "10-15年", "15-20年", "20-25年", "25-30年", "30年以上"]
cleaned_df["TenureGroup"] = pd.cut(cleaned_df["Tenure"], bins=tenure_bins, labels=tenure_labels, right=False)
cleaned_df["IsMobileLogin"] = (cleaned_df["PreferredLoginDevice"] == "Mobile Phone").astype(int)
print(f"\nTenureGroup:\n{cleaned_df['TenureGroup'].value_counts().sort_index()}")

# 7. Outlier check
def iqr_check(series):
    s = series.dropna()
    q1, q3 = s.quantile(0.25), s.quantile(0.75)
    iqr = q3 - q1
    return {"Q1": q1, "Q3": q3, "lower": q1 - 1.5 * iqr, "upper": q3 + 1.5 * iqr, "outliers": int(((s < q1 - 1.5 * iqr) | (s > q3 + 1.5 * iqr)).sum())}

for f in ["WarehouseToHome", "OrderCount", "CashbackAmount"]:
    print(f"\n{f} outliers: {iqr_check(cleaned_df[f])}")

# 8. Business rules
rules = {"HourSpendOnApp<0": (cleaned_df["HourSpendOnApp"] < 0).sum(),
         "WarehouseToHome<0": (cleaned_df["WarehouseToHome"] < 0).sum(),
         "OrderCount<=0": (cleaned_df["OrderCount"] <= 0).sum(),
         "CashbackAmount<0": (cleaned_df["CashbackAmount"] < 0).sum()}
print(f"\nBusiness rules: {rules}")

# 9. Export
assert cleaned_df[NUMERIC_MISSING_COLS].isna().sum().sum() == 0
assert "Phone" not in cleaned_df["PreferredLoginDevice"].unique()
assert "COD" not in cleaned_df["PreferredPaymentMode"].unique()
assert "CC" not in cleaned_df["PreferredPaymentMode"].unique()
assert {"TenureGroup", "IsMobileLogin"}.issubset(cleaned_df.columns)

quality_after = build_quality_report(cleaned_df)
quality_before.to_csv(OUTPUT_DIR / "data_quality_before.csv", index=True, encoding="utf-8-sig")
quality_after.to_csv(OUTPUT_DIR / "data_quality_after.csv", index=True, encoding="utf-8-sig")
cleaning_log.to_csv(OUTPUT_DIR / "cleaning_log.csv", index=False, encoding="utf-8-sig")
cleaned_df.to_csv(OUTPUT_DIR / "ecommerce_customer_cleaned.csv", index=False, encoding="utf-8-sig")

print(f"\n=== Exported to {OUTPUT_DIR} ===")
for f in sorted(OUTPUT_DIR.glob("*")):
    print(f"  {f.name} ({f.stat().st_size/1024:.1f}KB)")

print("\n=== Project Complete ===")
print("1. Missing values filled with median")
print("2. Categories standardized (Phone->Mobile Phone, COD/CC unified)")
print("3. TenureGroup, IsMobileLogin created")
print("4. Outliers recorded, not deleted")
print("5. Ready for Day5 analysis")
