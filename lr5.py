import pandas as pd from openpyx1 import load_workbook
import matplotlib.pyplot as plt
wb = pd.read_csv("data.csv")
#print(wb['days_employed'][0])
otsut_empl = wb.count()['children'] - wb.count()['days_employed']
otsut_ttl = wb.count()['children'] - wb.count()['total_income']
all_count = wb.count()['children']
medi.an_empl = wb['days_employed'].sum()/wb.count()['days_employed'] median_ttl = wb['total_income'].sum()/wb.count()['total_income']
print("B ", otsut_empl, " из ", wb.count()['children'], 'отсутствуют значения в столбце days_employed') print("B ", wb.count()['children'] - wb.count()['total_income'], " из ", wb.count()['children'], 'отсутствуют значения
в столбце total_income")
for i in range(wb.count()['children']):
if pd. isnull(wb['days_employed'][i]): wb.iat[i,1] = median_empl
if pd.isnull(wb['total_income'][i]):
wb.iat[i, 10] = median_ttl print(wb['total_income'][i])
labels = 'days_employed', "Other"
sizes = [otsut_empl, all_count]
fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='X1.1fXX')
labels = 'total_income', 'Other"
sizes = [otsut_ttl, all_count]
fig1, ax2 = plt.subplots()
ax2.pie(sizes, labels=labels, autopct='X1.1fXX')
plt. show()
wb.to_csv("data1.csv',index=False)
wb= pd.read_csv("data1.csv")
median_empl = wb['days_employed'].sum()/wb.count()['days_employed']
#замена отрицательных часов работы на положительное #замена стажа с отрицательного на положительное и >70 заменяется на 70 for i in range(wb.count()['children']): if wb['days_employed'][i] < 0: wb.iat[i,1] *= -1
if wb['dob_years'][i] < 0: wb.iat[i,2] *= -1
elif wb['dob_years'][i] > 70:
wb.iat[i,2] = 70
wb.to_csv('data1.csv',index=False)
wb = pd.read_csv("data1.csv")
wb["total_income"] = wb["total_income"].astype(int)
wb.to_csv('data1.csv',index=False)
wb = pd.read_csv("data1.csv")
#замена всех символов на нижний регистр for i in range(wb.count()['children']):
wb["education"][i] = wb["education"][i].lower()
wb.to csv('data1.csv',index=False)
wb = pd.read_csv("data1.csv")
new_df_education = pd.DataFrame({"name': ["высшее", "среднее", "неоконченное высшее", "начальное' ]})
new_df_family = pd.DataFrame({"name': ['женат / замужем', "гражданский брак", "вдовец / вдова", "в разводе", "Не женат / не замужем"]})
del wb['family_status']
del wb['education']
wb.to_csv('data1.csv',index=False)
list_categ=[]
for i in range(wb.count()['children']):
if int(wb['total_income'][i]) < 30000:
list_categ.append('E')
elif int(wb['total_income'][i]) < 50000: list_categ.append("D')
elif int(wb['total_income'][i]) < 200000: list_categ.append('C')
elif int(wb['total_income'][i]) < 1000000:
list_categ.append('B')
else:
list_categ.append('A')
wb['total_income_category'] = list_categ
wb.to_csv('data1.csv', index=False)
list_categ=[]
for i in range(wb.count()['children']):
if 'автомобил' in wb['purpose'][i]:
list_categ.append('операции с автомобилем')
elif 'жиль' in wb['purpose'][i] or 'недвижимост' in wb['purpose'][i]: list_categ.append('операции с недвижимостью")
elif 'свадьб' in wb['purpose'][i]:
list_categ.append("проведение свадьбы")
elif 'образовани' in wb['purpose'][i]:
list_categ.append('получение образования')
else:
list_categ.append("другое")
wb['purpose_category'] = list_categ
wb.to_csv('data1.csv',index=False)
