#! /usr/bin/python

# import matplotlib.pyplot as plt
# import pandas as pd
#
# x, y = [], []
# for i in range(99):
#     x.append(i)
#     y.append(i * i)
# df = pd.DataFrame({'x': x, 'y': y})
# df.plot('x','y', kind = "scatter")
#
# plt.show()

# SELECT title, price, (price*18/100)/(1+18/100) AS tax, price/(1+18/100) AS price_tax FROM book1


# SELECT title, amount,
#        CASE
#            WHEN amount < 4 THEN price*0.5
#            ELSE price
#        END AS new_price
# FROM book1;

# SELECT author, SUM(price * amount) AS total
# FROM book1 GROUP BY author ORDER BY total

# SELECT author,
# MIN(price) AS Минимальная,
# MAX(price) AS Максимальная
# FROM book1
# GROUP BY author
# HAVING SUM(price*amount)>5000
# ORDER BY Минимальная DESC

# SELECT author,
# MIN(price) AS Минимальная,
# MAX(price) AS Максимальная
# FROM book1
# WHERE author <> 'Конфуций'
# GROUP BY author
# HAVING SUM(price*amount)>5000
# ORDER BY Минимальная DESC

# SELECT title, author, price, amount
# FROM book1
# WHERE price <=
# (SELECT AVG(price) FROM book1)
# ORDER BY price