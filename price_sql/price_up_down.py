#-*- coding: utf-8 -*-
import sys
sys.path.append("/home/louis/python/")
import  sql
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

BEGIN = "'2016-8-1'"
END = "'2016-9-1'"

conn = sql.connect_sql()
sql_down = "SELECT o.id,o.amount,o.initamount,o.customamount,c.name "
sql_down +="FROM `zzplatform`.`t_order` as o INNER JOIN  `zzplatform`.`t_md_city` as c on c.id=o.cityid "
sql_down += "WHERE o.customamount < o.initamount and o.createTime>%s and o.createTime<%s and o.state<>'cancel' and o.state<>'none';" % (BEGIN, END)

sql_up = "SELECT o.id,o.amount,o.initamount,o.customamount,c.name "
sql_up +="FROM `zzplatform`.`t_order` as o INNER JOIN  `zzplatform`.`t_md_city` as c on c.id=o.cityid "
sql_up += "WHERE o.customamount > o.initamount and o.createTime>%s and o.createTime<%s and o.state<>'cancel' and o.state<>'none';" % (BEGIN, END)

try:
    df_down = pd.io.sql.read_sql(sql_down, con=conn)
    df_up = pd.io.sql.read_sql(sql_up, con=conn)
    writer = pd.ExcelWriter('/home/louis/python/price_sql/price_up_down_%s.xlsx' % BEGIN)
    df_down.to_excel(writer,'Sheet1')
    df_up.to_excel(writer, 'Sheet2')
    writer.save()
finally:
    conn.close()

res1 =  (df_down["initamount"]-df_down["customamount"]) / df_down["initamount"] * 100
df_down["down_precent"] = pd.Series(res1, index=df_down.index)
res2 =  (df_up["customamount"]-df_up["initamount"]) / df_up["initamount"] * 100
df_up["up_precent"] = pd.Series(res2, index=df_up.index)
#df_price = df["down_precent"].mean()
#print type(df_price)

result = u"统计从%s到%s排除没有接和取消订单，交易价格比平台定价低的订单：\n" % (BEGIN, END)
result += u"一共有%d订单 \n" % (df_down["down_precent"].count())
result += u"降价百分比平均值：%d \n" % (df_down["down_precent"].mean())
result += u"降价百分比最大值：%d \n" % (df_down["down_precent"].min())
result += u"降价百分比最小值：%d \n" % (df_down["down_precent"].max())
result += u"降价百分比方差：%d \n" % (df_down["down_precent"].std())
#print df["down_precent"].describe()
print result
#df_city.plot()
#plt.show()
result = u"统计从%s到%s排除没有接和取消订单，交易价格比平台定价高的订单：\n" % (BEGIN, END)
result += u"一共有%d订单 \n" % (df_up["up_precent"].count())
result += u"升价百分比平均值：%d \n" % (df_up["up_precent"].mean())
result += u"升价百分比最大值：%d \n" % (df_up["up_precent"].min())
result += u"升价百分比最小值：%d \n" % (df_up["up_precent"].max())
result += u"升价百分比方差：%d \n" % (df_up["up_precent"].std())
print result