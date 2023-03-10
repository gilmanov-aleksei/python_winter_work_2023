#! /usr/bin/python

import pandas as pd
import random

df = pd.DataFrame(columns=['Год', 'Товар', 'Шт', 'Цена'], index=range(20))

x = 0
for i in range(2001, 2006):
    for j in ['A', 'B', 'C']:
        k = [10, 20, 30, 40, 50][random.randint(0, 4)]
        m = [100, 50, 30, 20, 5][random.randint(0, 4)]
        df.iloc[x] = [i, j, k, m]
        x += 1
df['Итого'] = df['Шт']*df['Цена']
# print(df)
# df.to_excel('test2.xlsx')
# df1 = df[['Год', 'Итого', 'Товар']]
# df1 = df.loc[10:15]
# df1 = df.head(5)
# df1 = df.tail(5)
# df1 = df[(df['Итого'] > 1000) & (df['Цена'] < 100)]
# df1 = df.iloc[10:20]
# print(df.columns)
# print(df.index)
# df.set_index()
# print(df[df['Товар'].isin(['A', 'B'])][['Год', 'Итого']])
# print(df.sort_values('Итого', ascending=False).head(4))
# df1 = df.groupby('Товар').Итого.sum()
# df1 = df['Итого'].max()
# print(df1)
# print(df[df['Итого'] == df['Итого'].max()])
# for i in range(len(df)):
#     for j in df.columns:
#         print(df.loc[i, j], end=' ')
#     print()
# me = df['Цена'].mean()
# print(df[df['Цена'] < me])
# mi = []
# for i in df.columns:
#     mi.append(df[i].min)
# mi_nu
print(df.groupby('Год').Итого.sum().max())
