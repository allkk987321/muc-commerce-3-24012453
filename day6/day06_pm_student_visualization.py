# Day06 PM: E-commerce User Data Visualization
# Student: 24012453 | Topic: A
from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter

try:
    from IPython.display import display
except ImportError:
    def display(obj):
        print(obj)

STUDENT_ID = "24012453"
TOPIC = "A"

pd.set_option("display.max_columns", 50)
pd.set_option("display.float_format", lambda x: f"{x:,.2f}")
plt.rcParams["font.sans-serif"] = ["Microsoft YaHei", "SimHei", "DejaVu Sans"]
plt.rcParams["axes.unicode_minus"] = False

def find_workspace_root(start=None):
    start = Path.cwd() if start is None else Path(start)
    for candidate in [start, *start.parents]:
        if (candidate / "output" / "day04_project" / "ecommerce_customer_cleaned.csv").exists():
            return candidate
    raise FileNotFoundError("Day04 output not found")

ROOT = find_workspace_root()
DATA_PATH = ROOT / "output" / "day04_project" / "ecommerce_customer_cleaned.csv"
DAY05_DIR = ROOT / "output" / "day05_analysis"
OUTPUT_DIR = ROOT / "output" / "day06_visualization"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

print("Student:", STUDENT_ID, "| Topic:", TOPIC)
print("Output:", OUTPUT_DIR.relative_to(ROOT))

df = pd.read_csv(DATA_PATH)
ov = pd.read_csv(DAY05_DIR / "overall_metrics.csv")
sg = pd.read_csv(DAY05_DIR / "segment_analysis.csv")
cr = pd.read_csv(DAY05_DIR / "cross_analysis.csv")

assert df.shape[0] == 5630
assert set(df["Churn"].unique()).issubset({0, 1})
print("Checkpoint 1A passed")

# Task 1: Bar chart - TenureGroup churn rate
category_field = "TenureGroup"
category_summary = (df.groupby(category_field, observed=True)
    .agg(用户数=("CustomerID","nunique"), 流失率=("Churn","mean")).reset_index())

fig_bar, ax_bar = plt.subplots(figsize=(10,6))
bars = ax_bar.bar(category_summary[category_field], category_summary["流失率"]*100, color="steelblue", edgecolor="white")
ax_bar.set_title("TenureGroup Churn Rate", fontsize=14, fontweight="bold")
ax_bar.set_ylabel("Churn Rate (%)")
for bar, rate, cnt in zip(bars, category_summary["流失率"], category_summary["用户数"]):
    ax_bar.text(bar.get_x()+bar.get_width()/2, bar.get_height()+0.5, f"{rate*100:.1f}%\n(n={cnt})", ha="center", fontsize=9)
fig_bar.tight_layout()
fig_bar.savefig(OUTPUT_DIR/"01_category_bar.png", dpi=150, bbox_inches="tight")
plt.close(fig_bar)
print("Task1: 01_category_bar.png")

# Task 2: Scatter
x_field, y_field = "OrderCount", "CashbackAmount"
fig_scatter, ax_scatter = plt.subplots(figsize=(10,6))
for cv, lb, cl in [(0,"Not Churned","steelblue"),(1,"Churned","coral")]:
    s = df[df["Churn"]==cv]
    ax_scatter.scatter(s[x_field],s[y_field],alpha=0.3,c=cl,label=lb,s=10)
ax_scatter.set_title("OrderCount vs CashbackAmount by Churn", fontsize=14, fontweight="bold")
ax_scatter.set_xlabel("OrderCount")
ax_scatter.set_ylabel("CashbackAmount")
ax_scatter.legend()
fig_scatter.tight_layout()
fig_scatter.savefig(OUTPUT_DIR/"02_behavior_scatter.png", dpi=150, bbox_inches="tight")
plt.close(fig_scatter)
print("Task2: 02_behavior_scatter.png")

# Task 3: Line chart
ordered_field = "TenureGroup"
ordered_summary = (df.groupby(ordered_field, observed=True)
    .agg(用户数=("CustomerID","nunique"), 流失率=("Churn","mean"), 平均订单数=("OrderCount","mean")).reset_index())
fig_line, ax1 = plt.subplots(figsize=(10,6))
ax2 = ax1.twinx()
ln1,=ax1.plot(ordered_summary[ordered_field], ordered_summary["流失率"]*100, "o-", color="coral", lw=2, ms=8, label="Churn Rate(%)")
ln2,=ax2.plot(ordered_summary[ordered_field], ordered_summary["平均订单数"], "s--", color="steelblue", lw=2, ms=8, label="Avg Orders")
ax1.set_title("TenureGroup Ordered Analysis", fontsize=14, fontweight="bold")
ax1.set_ylabel("Churn Rate (%)")
ax2.set_ylabel("Avg Orders")
ax1.legend([ln1,ln2],[ln1.get_label(),ln2.get_label()],loc="upper left")
fig_line.tight_layout()
fig_line.savefig(OUTPUT_DIR/"03_ordered_line.png", dpi=150, bbox_inches="tight")
plt.close(fig_line)
print("Task3: 03_ordered_line.png")

# Task 4: Composition
composition_field = "PreferredPaymentMode"
composition_summary = df[composition_field].value_counts().reset_index()
composition_summary.columns = [composition_field, "用户数"]
composition_summary["占比"] = composition_summary["用户数"]/len(df)
n_cats = len(composition_summary)
fig_comp, ax_comp = plt.subplots(figsize=(10,6))
if n_cats <= 5:
    ax_comp.pie(composition_summary["用户数"], labels=composition_summary[composition_field], autopct="%1.1f%%", startangle=90)
else:
    ax_comp.bar(composition_summary[composition_field], composition_summary["占比"]*100, color="steelblue")
    ax_comp.set_ylabel("Share (%)")
ax_comp.set_title("Payment Mode Composition", fontsize=14, fontweight="bold")
fig_comp.tight_layout()
fig_comp.savefig(OUTPUT_DIR/"04_composition_chart.png", dpi=150, bbox_inches="tight")
plt.close(fig_comp)
print("Task4: 04_composition_chart.png")

# Task 5: 2x2 Dashboard
fig_summary, axes = plt.subplots(2,2,figsize=(14,10))
axes[0,0].bar(category_summary[category_field], category_summary["流失率"]*100, color="steelblue")
axes[0,0].set_title("Churn Rate by TenureGroup")
for cv,lb,cl in [(0,"Not Churned","steelblue"),(1,"Churned","coral")]:
    s=df[df["Churn"]==cv]
    axes[0,1].scatter(s[x_field],s[y_field],alpha=0.3,c=cl,label=lb,s=5)
axes[0,1].set_title("Orders vs Cashback")
axes[0,1].legend(fontsize=7)
axes[1,0].plot(ordered_summary[ordered_field], ordered_summary["流失率"]*100, "o-", color="coral")
axes[1,0].set_title("TenureGroup Churn Trend")
if n_cats<=5:
    axes[1,1].pie(composition_summary["用户数"], labels=composition_summary[composition_field], autopct="%1.0f%%")
else:
    axes[1,1].bar(composition_summary[composition_field], composition_summary["占比"]*100)
axes[1,1].set_title("Payment Mode")
fig_summary.suptitle("E-commerce User Analysis Dashboard", fontsize=16, fontweight="bold")
fig_summary.tight_layout(rect=[0,0,1,0.96])
fig_summary.savefig(OUTPUT_DIR/"day06_visualization_summary.png", dpi=150, bbox_inches="tight")
plt.close(fig_summary)
print("Task5: day06_visualization_summary.png")

# Task 6: Chart manifest
chart_manifest = pd.DataFrame([
    {"chart_id":"01","file_name":"01_category_bar.png","business_question":"Churn rate by tenure","chart_type":"bar","key_finding":"0-5yr:38% churn, decreasing with tenure","limitation":"Cross-sectional, not time series"},
    {"chart_id":"02","file_name":"02_behavior_scatter.png","business_question":"Orders vs cashback by churn","chart_type":"scatter","key_finding":"Churned users: lower orders & cashback","limitation":"Correlation != causation"},
    {"chart_id":"03","file_name":"03_ordered_line.png","business_question":"Ordered stage trends","chart_type":"line","key_finding":"Churn decreases, orders increase with tenure","limitation":"Stage comparison, not historical trend"},
    {"chart_id":"04","file_name":"04_composition_chart.png","business_question":"Payment mode composition","chart_type":"pie_or_bar","key_finding":"Debit+Credit Card dominate","limitation":"Snapshot, no time variation"},
    {"chart_id":"05","file_name":"day06_visualization_summary.png","business_question":"Overall dashboard","chart_type":"dashboard","key_finding":"Multi-dimensional view","limitation":"Needs Day05 tables for detail"},
])
chart_manifest.to_csv(OUTPUT_DIR/"chart_manifest.csv", index=False, encoding="utf-8-sig")

for img in ["01_category_bar.png","02_behavior_scatter.png","03_ordered_line.png","04_composition_chart.png","day06_visualization_summary.png"]:
    p = OUTPUT_DIR/img
    assert p.exists() and p.stat().st_size>5000, f"Missing: {img}"
print("\n=== Day06 Complete ===")
for f in sorted(OUTPUT_DIR.glob("*")):
    print(f"  {f.name}")




