from pathlib import Path
import pandas as pd
import numpy as np

'''
调用相关函数，其中from pathlib import Path用于导入路径处理模块，pd.read_csv用于读取CSV文件，encoding='utf-8-sig'用于指定文件编码格式为utf-8-sig。
'''

csv_file = Path("../data/淘宝全品类全国数据.csv")
df = pd.read_csv(csv_file, encoding='utf-8-sig')
print('数据规模：', df.shape)
print('数据前5行：', df.head())
print('数据字段名：', df.columns)
print('数据摘要信息：', df.info())

'''
确定相关的文件路径，初步了解数据结构，一行记录代表着一个商品，包含商品id、一级品类、商品价格、省份、商品销量等信息。
'''

print(df.dtypes)
missing_count = df.isna().sum().sort_values(ascending=False)
print(missing_count)
# 缺失率（百分比）
missing_rate = (df.isna().mean() * 100).round(1).sort_values(ascending=False)
print(missing_rate)

'''
查找出数据类型，单列：Series，并超出数据缺失率
'''

prices_series = df['商品价格']
print(type(prices_series))
# 多列：DataFrame
product_view = df[['商品id', '一级品类', '商品价格', '省份', '商品销量']]
print(type(product_view))
print(product_view.head())

print(df.loc[0:4, ['一级品类', '商品价格', '省份']])
print(df.iloc[0:5, 0:4])

'''
查找相关的数据，loc和iloc的区别在于loc是基于标签的索引，而iloc是基于位置的索引。就是说一个是闭区间一个是开区间
'''

guangdong_data = df[df['省份'] == '广东']
condition = (df['省份'] == '广东') & (df['商品价格'] > 1000)
selected = df.loc[condition, ['商品id', '一级品类', '商品价格', '省份', '商品销量']]
selected = selected.sort_values(by='商品价格', ascending=False)

zhejiang_or_jiangsu = df[(df['省份'] == '浙江') | (df['省份'] == '江苏')]
print('浙江或江苏商品数：', zhejiang_or_jiangsu.shape[0])

'''
具体到省份的数据，例如广东省的数据，后面还有浙江的，就是运用d[df['省份']=='广东']，运用双重df来具体查找并定义储存
'''


# 商品价格的描述性统计
print(df['商品价格'].describe().round(2))

# 一级品类商品数
print(df['一级品类'].value_counts())

# 一级品类汇总
category_summary = (
    df.groupby('一级品类')
      .agg(商品数=('商品id', 'size'),
           平均价格=('商品价格', 'mean'),
           中位价格=('商品价格', 'median'))
      .sort_values('平均价格', ascending=False)
      .round(2)
)
print(category_summary)

'''
运用describe()函数，可以快速获取数据的描述性统计信息，包括计数、均值、标准差、最小值、四分位数和最大值。
'''
