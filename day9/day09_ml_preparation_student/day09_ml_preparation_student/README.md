# 第9天学生项目：机器学习零基础数据准备

## 运行方法

```bash
python -m pip install -r requirements.txt
python validate_day09_environment.py
jupyter lab
```

打开`notebooks/day09_ml_preparation_student.ipynb`。Notebook已经提供完整处理骨架，你只需完成少量关键填空、运行检查点并撰写解释。

## 学生信息

- 姓名：24012453
- 学号：24012453
- 班级：muc-commerce-3

## 用自己的话回答

- 什么是特征，什么是标签：特征是模型判断时可以查看的用户信息（如Tenure、OrderCount），标签是希望预测的真实答案（Churn）。
- 为什么要保留测试集：测试集模拟未见过的新用户，用来检验模型是否真的学到了规律而非死记硬背训练数据。
- 为什么83%准确率仍可能没有用：因为最低参照线永远预测多数类（未流失），准确率虽高但流失召回率为0，完全无法识别需要挽留的流失用户。
