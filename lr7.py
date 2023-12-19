import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt

wb = pd.read_csv('games.csv')

#все названия столбцов в нижний регистр
column_names = wb.columns.values.tolist()
for column in column_names:
    wb = wb.rename(columns={column: column.lower()})

#замена типа float на int в столбце года релиза, если значение отсутсвует, заменяется на 0
#в случае если не заменять отсутствующие данные, год релиза не будет типа int
#год релиза не имеет данных после точки, так что не имеет смысла хранмить данные в типе float
for i in range(wb.count()['name']):
    year = wb.iat[i, 2]
    if math.isnan(year):
      wb.iat[i, 2] = 0
wb['year_of_release'] = wb['year_of_release'].astype(int)
#конец замены в столбце года

#подсчет продаж во всех регионах и выведение этого в отдельный столбец
list_all_sales = []
for i in range(wb.count()["year_of_release"]):
   all_sales = wb.iat[i, 4] + wb.iat[i, 5] + wb.iat[i, 6] + wb.iat[i, 7]
   list_all_sales.append(all_sales)
wb['all_sales'] = list_all_sales

print(wb)
wb.to_csv('games v2.csv', index=False)
