#-*- coding: utf-8 -*-
import sys
sys.path.append("/home/louis/python/")
import  sql
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

BEGIN = "'2016-10-1'"
END = "'2016-10-29'"
"""
conn = sql.connect_sql()
sql = "SELECT o.id,o.merchantname,o.eshopOrderRemark,o.state,o.amount,o.category"
sql +=" FROM `zzplatform`.`t_order` as o "
sql += "WHERE o.createTime>%s and o.createTime<%s;" % (BEGIN, END)

try:
    df = pd.io.sql.read_sql(sql, con=conn)
    writer = pd.ExcelWriter('/home/louis/python/order/res_%s.xlsx' % BEGIN)
    df.to_excel(writer, 'data')
    writer.save()
finally:
    conn.close()
"""
df = pd.read_excel("res_'2016-10-1'.xlsx")
alist = ['complete','waitconfirm']
tab1 = df[df['state'].isin(alist)].groupby(['category'])['id'].count().reset_index()
tab2 = df.groupby(['category'])['id'].count().reset_index()
print type(tab1)
print '=========='
print tab2['id']
#add coloum
tab1['all'] = tab2['id']
print tab1
#tab2 = df['id'].isin(alist).groupby(['category','state'])['id'].count().reset_index()
#print tab[tab['state'].isin(alist)].sort_values(by=['id'], ascending=False)
#print tab.sort_values(by=['id'], ascending=False)