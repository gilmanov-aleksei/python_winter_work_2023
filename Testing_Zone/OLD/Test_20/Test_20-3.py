#! /usr/bin/python

# import pandas as pd

# df1 = pd.DataFrame([[1, 'Bob', 'Builder'],
#                     [2, 'Sally', 'Baker'],
#                     [3, 'Scott', 'Candle Stick Maker']],
#                    columns=['id', 'name', 'occupation'])
# print(df1)
# df2 = pd.DataFrame({'country': [10, 20, 30],
#                     'popul': [10000, 20000, 30000],
#                     'sq': [13213213, 5465465465, 8798798798]})
# print(df2)
#
# dct = {'country': [10, 20, 30],
#        'popul': [10000, 20000, 30000],
#        'sq': [13213213, 54654465, 87987798]}
# df = pd.DataFrame(dct)
# print(df)
# df['Subj'] = ['Java', 'Python', 'Pandas']
# df['new'] = df['Dept'] + df['Subj']
# print(df)

# import pandas as pd
#
# dct = {'Год': [2001, 2002, 2003, 2004, 2005],
#        'Товар': ['A', 'B', 'C', 'D', 'E'],
#        'шт': [10, 20, 30, 40, 50],
#        'Цена': [100, 200, 300, 400, 500]}
# df = pd.DataFrame(dct)
# df['Итого'] = df['Цена'] * df['шт']
# print(df)
# df.to_excel('test.xlsx')
# df1 = pd.read_excel('test.xlsx')
# df1.columns = ['Год', 'Товар', 'шт', 'Цена']
# df1 = df1.set_index('Год')
# df1['Товар', 'Цена']
# df1.loc[2002]
# df1.loc[2003, 'шт'] = 123
# print(df1)
# cond = df1['Цена'] > 25
# df1[cond]
# # df1[df1['Цена'] == 25]
# print(df1[df1['Цена'] == 50])

import pandas as pd
df1 = pd.read_excel('test.xlsx')
for i in df1.index:
       print(i, end=':')
       for j in df1.columns:
              print(i, j, df1.loc[i, j], end=' ')
       print()