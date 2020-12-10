# 국가별 코로나 바이러스 관련 일별 확진자 추이
# python bar chart race covid-19
# 1. csv 파일 읽기
# 2. 날짜별 필드명 - 오름차순 읽기 - 데이터 프레임
# 3. 그래프 그리기 - 주피터노트북 / 판다스

# import csv
import pandas as pd
# import numpy as np
import matplotlib.pyplot as plt
from datetime import date, timedelta

# f = open('owid-covid-data.csv', 'r')
# rdr = csv.reader(f)
#
# for line in rdr:
#     print(line)
# f.close()
from matplotlib import animation

data = pd.read_csv("owid-covid-data.csv", usecols=["date", 'location', 'total_cases'])
# print(data.dtypes)
# print(data)
# print(type(data))
# df = data.groupby(["date"])
# print(df)
# d = data.groupby(['date', 'location'])['total_cases'].mean()
# print(d)
# plt.bar(df['location'], df['total_cases'])
# plt.show()

data['date1'] = pd.to_datetime(data['date'])
data['year'] = data['date1'].dt.year
data['month'] = data['date1'].dt.month
data['day'] = data['date1'].dt.day
data['d'] = data['date1'].dt.strftime('20%y%m%d')
data['d'] = list(map(int, data['d']))

# print(data['d'].dtypes)
# print(data)
dd = list(set(data['d']))
dd.sort()
# print(dd)

# df = data[data['date'].eq('2020-11-15')].sort_values(by='total_cases', ascending=True).tail(30)
# print(df)

# plt.barh(df['location'], df['total_cases'])
# ax = plt.gca()
# ax.get_xaxis().get_major_formatter().set_scientific(False)
# plt.show()


# for i in range(10):
#     ax.clear()
#     plt.barh(df['location'], df['total_cases'])
#     ax = plt.gca()
#     plt.xlabel(i)
#     ax.get_xaxis().get_major_formatter().set_scientific(False)


d1 = date(2019, 12, 31)
d2 = date(2020, 11, 15)

delta = d2 - d1
datt = []

for i in range(delta.days + 1):
    a = d1 + timedelta(days=i)
    a = a.strftime("20%y%m%d")
    datt.append(a)

datt = list(map(int, datt))

# fig, ax = plt.subplots(figsize=(15, 8))

'''
def draw_barchart(day):
    df = data[data['d'].eq(day)].sort_values(by='total_cases', ascending=False).head(10)
    # dff = df[df['d'].eq(day)].sort_values(by='total_cases', ascending=True).tail(30)
    ax = plt.gca()
    ax.clear()
    ax.barh(df['location'], df['total_cases'], height=0.2)
    ax.get_xaxis().get_major_formatter().set_scientific(False)
    dx = df['total_cases'].max() / 200
    for i, (value, name) in enumerate(zip(df['total_cases'], df['location'])):
        ax.text(value - dx, i, name, size=14, weight=600, ha='right', va='bottom')
        ax.text(value + dx, i, f'{value:,.0f}', size=14, ha='left', va='center')
    ax.set_yticks([])


animator = animation.FuncAnimation(fig, draw_barchart, frames=datt)
'''

plt.rcParams["figure.figsize"] = (14, 8)
for i in dd:
    plt.clf()
    df = data[data['d'].eq(i)].sort_values(by='total_cases', ascending=False).head(10).fillna(0)

    loc_list = list(df['location'].values)
    total_list = list(df['total_cases'].values)
    loc_list.reverse()
    total_list.reverse()
    plt.barh(loc_list, total_list)
    plt.gca().get_xaxis().get_major_formatter().set_scientific(False)

    dx = df['total_cases'].max() / 200
    for j, (value, name) in enumerate(zip(total_list, loc_list)):
        plt.text(value - dx, j, name, size=12, weight=600, ha='right', va='bottom')
        # plt.text(value if value is None else 0 - dx, j, name, size=12, weight=600, ha='right', va='bottom')
        plt.text(value + dx, j, f'{value:,.0f}', size=12, ha='right', va='top')
        # plt.text(value if value is None else 0 + dx, j, f'{value:,.0f}', size=12, ha='right', va='top')

    plt.yticks([])
    plt.pause(0.1)

plt.show()
