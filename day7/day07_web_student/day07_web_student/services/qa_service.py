from pathlib import Path

import pandas as pd


def answer_question(base_dir: Path, question: str) -> str:
    data_dir = base_dir / "data"
    metrics_df = pd.read_csv(data_dir / "overall_metrics.csv", encoding="utf-8-sig")
    metrics = dict(zip(metrics_df["指标"], metrics_df["数值"]))
    normalized = question.replace(" ", "").lower()

    if any(word in normalized for word in ["多少用户", "用户数", "总用户"]):
        return f"数据集中共有{int(metrics['用户数']):,}名用户。"
    
    if any(word in normalized for word in ["流失率", "churn"]):
        return f"总体流失率为 {metrics['流失率']:.1%}，即 {int(metrics['流失人数'])} 名用户已流失。"
    
    if any(word in normalized for word in ["订单", "order"]):
        return f"用户平均订单数为 {metrics['平均订单数']:.2f} 单/人，订单数中位数为 {int(metrics['订单数中位数'])} 单。"
    
    category_df = pd.read_csv(data_dir / "category_analysis.csv", encoding="utf-8-sig")
    if any(word in normalized for word in ["品类", "category", "偏好"]):
        top_cat = category_df.loc[category_df["用户数"].idxmax()]
        return f"偏好品类中「{top_cat['PreferedOrderCat']}」用户最多，共 {int(top_cat['用户数'])} 人，流失率为 {top_cat['流失率']:.1%}。"
    
    segment_df = pd.read_csv(data_dir / "segment_analysis.csv", encoding="utf-8-sig")
    if any(word in normalized for word in ["生命周期", "风险", "阶段"]):
        highest = segment_df.loc[segment_df["流失率"].idxmax()]
        lowest = segment_df.loc[segment_df["流失率"].idxmin()]
        return (
            f"生命周期「{highest['TenureGroup']}」阶段流失风险最高（{highest['流失率']:.1%}），"
            f"「{lowest['TenureGroup']}」阶段流失风险最低（{lowest['流失率']:.1%}）。"
        )
    
    return "请换一种更具体的问法，例如：总体流失率是多少？哪个偏好品类用户最多？"
