#-*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import datetime

p_data = {}
with open('history.txt', 'r') as f:
    line = f.readline().split("=")
    p_data[line[0]]=int(line[1])
    line = f.readline().split("=")
    p_data[line[0]]=int(line[1])
print p_data
"""
df = pd.read_excel("Android_20161007.xls")
new = df[u"新增用户"].sum()
active = df[u"活跃用户"].mean()
total_num = df[u"累计用户"][0]
daystamp = datetime.datetime.today().strftime("%Y-%m-%d")

with open('report.txt', 'w') as f:
    f.write(daystamp + "\n")
    f.write(u"新增用户 : " + str(new) + "\n")
    f.write(u"活跃用户 :" + str(int(active)) + "\n")
    f.write(u"累计用户 : " + str(total_num))
"""