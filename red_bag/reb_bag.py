#!/usr/bin/python
#-*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import datetime

"""
TRUENAME = 0
REGTIME = 11
REG_STATE  = 12
res = []
worker_old = []
worker = []
flag_time = datetime.datetime.strptime("2016-9-26 0:00",'%Y-%m-%d %H:%M')
#flag_time = "2016-9-26 0:00"
print type(flag_time)
"""
df = pd.read_excel("red_bag(1).xls")
print df.groupby("city_name").size()
#print df.groupby(["priceType", "price"]).sum()

"""
for arr in df.values:
    if arr[TRUENAME] not in worker:
        worker.append(arr[TRUENAME])
        #reg_time = datetime.datetime.strptime(arr[REGTIME],'%Y-%m-%d %H:%M')
        if arr[REGTIME] < flag_time and arr[TRUENAME] not in worker_old:
            worker_old.append({"name" : arr[TRUENAME].encode("UTF8"), "reg_time":arr[REGTIME]})

print len(worker)

res_df = pd.DataFrame(worker_old)
res_df.to_csv("/home/louis/python/red_bag/res2.csv",index=None, na_rep='None')
"""