# !/usr/bin/python3


import random
import matplotlib.pyplot as plt
import pandas as pd

x, y = [], []
for _ in range(1000):
    x.append(random.random())
    y.append(random.random())
df = pd.DataFrame({'x': x, 'y': y})
plt.scatter(df['x'], df['y'])
plt.show()
