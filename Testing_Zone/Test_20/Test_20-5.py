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
print(df)
df.to_excel('test2.xlsx')
