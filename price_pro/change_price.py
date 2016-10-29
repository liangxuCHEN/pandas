#-*- coding: utf-8 -*-
import pandas as pd
import numpy as np

REASON = 3

def check(x):
    if (u"车费" in reason) or (u"远" in reason) or (u"路费" in reason):
        return True
    return False

res = []
df = pd.read_csv("price_change.csv")
for arr in df.values:
    
