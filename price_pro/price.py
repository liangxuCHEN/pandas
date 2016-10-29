#-*- coding: utf-8 -*-
import pandas as pd
import numpy as np

AMOUNT = 0
INITAMOUT = 1
CUSTOM = 2
res = []
df = pd.read_csv("order_price.csv")
for arr in df.values:
    if arr[AMOUNT] == arr[INITAMOUT]:
        res.append({"change":False, "percent":0})
    elif arr[AMOUNT] > arr[INITAMOUT]:
         percent = (arr[AMOUNT] - arr[INITAMOUT]) / arr[INITAMOUT] * 100
         res.append({"change":"up", "percent":int(percent)})
    else:
         percent = (arr[INITAMOUT] - arr[AMOUNT]) / arr[INITAMOUT] * 100
         res.append({"change":"down", "percent":int(percent)})

res_df = pd.DataFrame(res)
res_df.to_csv("/home/louis/python/price_pro/res.csv",index=None, na_rep='None')
print res_df.groupby("change",).size()