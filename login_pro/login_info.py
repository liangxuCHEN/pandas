#-*- coding: utf-8 -*-
import pandas as pd
import numpy as np

USERID = 0
PLATFORM = 1
CREATEDATE = 3
STATE = 4
df = pd.read_csv("plateform.csv")
res = []
res.append({
    "userid" : 14, 
    "state": "normal",
    "first_platform": "ios",
    "last_platform": "None",
    "weixin" : 0,
    "android" : 1,
    "ios": 0,
    "change" : False, })
i = 0
for arr in df.values:
    if res[i]["userid"] == arr[USERID]:
        res[i]["last_platform"] = arr[PLATFORM]
        res[i][arr[PLATFORM]] = res[i][arr[PLATFORM]] + 1
        if res[i]["last_platform"] != res[i]["first_platform"]:
            res[i]["change"] = True
    else:
         i =  i + 1
         res.append({
             "userid" : arr[USERID],
             "state": arr[STATE],
             "first_platform": arr[PLATFORM],
              "last_platform": "None",
              "weixin" : 0,
              "android" : 0,
              "ios": 0,
              "change" : False})
         res[i][arr[PLATFORM]] = res[i][arr[PLATFORM]] + 1

res_df = pd.DataFrame(res)
res_df.to_csv("/home/louis/python/login_pro/res_3.csv",index=None, na_rep='None')
print res_df.groupby("change",).size()
print res_df.groupby("first_platform").size()
print res_df.groupby("last_platform").size()