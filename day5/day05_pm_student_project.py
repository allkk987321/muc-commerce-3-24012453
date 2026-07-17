# Day05 PM: E-commerce User Multi-dimensional Analysis
# Student: 24012453 | Topic: A
from pathlib import Path
import pandas as pd
import numpy as np

try:
    from IPython.display import display
except ImportError:
    def display(obj):
        print(obj)

STUDENT_NAME = "24012453"
TOPIC = "A"

pd.set_option("display.max_columns", 50)
pd.set_option("display.float_format", lambda x: f"{x:,.2f}")

def find_workspace_root(start=None):
    start = Path.cwd() if start is None else Path(start)
    for candidate in [start, *start.parents]:
        data_path = candidate / "output" / "day04_project" / "ecommerce_customer_cleaned.csv"
        if data_path.exists():
            return candidate
    raise FileNotFoundError("Day04 output not found")

ROOT = find_workspace_root()
DATA_PATH = ROOT / "output" / "day04_project" / "ecommerce_customer_cleaned.csv"
OUTPUT_DIR = ROOT / "output" / "day05_analysis"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

print("Name:", STUDENT_NAME)
print("Topic:", TOPIC)
print("Input:", DATA_PATH)
print("Output:", OUTPUT_DIR)

# Task 1: Load and validate
df = pd.read_csv(DATA_PATH)
print(f"\nData shape: {df.shape}")
display(df.head())

core_cols = ["CustomerID", "Churn", "Tenure", "TenureGroup", "OrderCount",
             "CouponUsed", "CashbackAmount", "DaySinceLastOrder", "Complain",
             "PreferedOrderCat", "PreferredPaymentMode"]

validation = pd.Series({
    "行数": len(df), "列数": df.shape[1],
    "CustomerID重复数": int(df["CustomerID"].duplicated().sum()),
    "核心字段缺失数": int(df[core_cols].isna().sum().sum()),
    "Churn取值": sorted(df["Churn"].unique().tolist()),
}, name="验收结果")
display(validation.to_frame())

assert df.shape == (5630, 22), f"Expected (5630,22), got {df.shape}"
available_core_cols = [c for c in core_cols if c in df.columns]
missing_core = int(df[available_core_cols].isna().sum().sum())
assert df["CustomerID"].is_unique
assert set(df["Churn"].unique()) == {0, 1}
print(f"Checkpoint 1 passed (core missing: {missing_core})")

# Task 2: Overall metrics
overall_metrics = pd.DataFrame({
    "指标": ["用户数", "流失人数", "流失率", "平均订单数", "订单数中位数",
             "平均优惠券数", "平均返现", "平均App时长", "平均满意度", "平均距上次下单天数"],
    "数值": [
        df["CustomerID"].nunique(), df["Churn"].sum(), df["Churn"].mean(),
        df["OrderCount"].mean(), df["OrderCount"].median(),
        df["CouponUsed"].mean(), df["CashbackAmount"].mean(),
        df["HourSpendOnApp"].mean(), df["SatisfactionScore"].mean(),
        df["DaySinceLastOrder"].mean(),
    ]
})
display(overall_metrics)
overall_churn_rate = df["Churn"].mean()
print(f"Overall churn rate: {overall_churn_rate:.4%}")
assert abs(overall_churn_rate - 0.16838365896980462) < 1e-8
print("Checkpoint 2 passed")

# Task 3: Single-dimension analysis (Topic A: TenureGroup)
segment_field = "TenureGroup"
segment_analysis = (
    df.groupby(segment_field, observed=True)
      .agg(
          用户数=("CustomerID", "nunique"),
          流失人数=("Churn", "sum"),
          流失率=("Churn", "mean"),
          平均订单数=("OrderCount", "mean"),
          平均优惠券数=("CouponUsed", "mean"),
          平均返现=("CashbackAmount", "mean"),
          平均距上次下单天数=("DaySinceLastOrder", "mean"),
      )
      .reset_index()
      .sort_values("用户数", ascending=False)
)
display(segment_analysis)
assert segment_field in df.columns
assert "用户数" in segment_analysis.columns
assert segment_analysis["用户数"].sum() == len(df)
print("Checkpoint 3 passed")

# Task 4: Cross-analysis (TenureGroup x Complain)
dim_1, dim_2 = "TenureGroup", "Complain"
cross_analysis = (
    df.groupby([dim_1, dim_2], observed=True)
      .agg(用户数=("CustomerID", "nunique"),
           流失人数=("Churn", "sum"),
           流失率=("Churn", "mean"),
           平均订单数=("OrderCount", "mean"))
      .reset_index()
)
cross_analysis["投诉状态"] = cross_analysis[dim_2].map({0: "无投诉", 1: "有投诉"})
cross_analysis["样本提示"] = np.where(cross_analysis["用户数"] < 30, "小样本", "可观察")
cross_analysis = cross_analysis.sort_values(["流失率", "用户数"], ascending=[False, False])
display(cross_analysis)
assert cross_analysis["用户数"].sum() == len(df)
assert set(cross_analysis["样本提示"]).issubset({"小样本", "可观察"})
print("Checkpoint 4 passed")

# Task 5: Export CSVs
outputs = {
    "overall_metrics.csv": overall_metrics,
    "segment_analysis.csv": segment_analysis,
    "cross_analysis.csv": cross_analysis,
}
for filename, table in outputs.items():
    path = OUTPUT_DIR / filename
    table.to_csv(path, index=False, encoding="utf-8-sig")
    reloaded = pd.read_csv(path)
    print(f"Exported {filename}: {reloaded.shape}")
    assert reloaded.shape == table.shape
print("Checkpoint 5 passed: 3 CSVs exported")

# Task 6: Conclusions
print("\n=== Conclusions ===")
print("1. 0-5yr users: 38% churn rate, much higher than 10+ yr (0-6%)")
print("2. Complain + new users: 62% churn vs 26% for non-complain")
print("3. CashbackAmount is cashback, not consumption; cannot compute GMV")
print("\nLimitations: No order amount/date; cross-sectional; small samples")
print("Suggestion: Fast-response for complaining new users, validate via A/B test")
print("\n=== Day05 Complete ===")



