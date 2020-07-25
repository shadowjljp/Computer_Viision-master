import sys

import numpy as np
import pandas as pd
from numpy import NaN

raw_input = pd.read_csv("E:\\Target.csv")

x = raw_input.loc[:, 'x'].dropna()
y = raw_input.loc[:, 'y'].dropna()
x0 = raw_input.loc[:, 'x0'].dropna()
y0 = raw_input.loc[:, 'y0'].dropna()
print(x)
print(y0)

Record={}
for k in range(len(x0)):
    for u in range(len(y0)):
        Record[(x0[k], y0[u])]= 0
print(Record)
print("len of Record is ",len(Record))
for i in range(len(x)):
    for k in range(len(x0)):
        for u in range(len(y0)):
            if 2 <= ((x[i] - x0[k]) ** 2 + (y[i] - y0[u]) ** 2) <= 4:
                temp = Record.get((x0[k], y0[u]))
                temp += 1
                Record[x0[k], y0[u]] = temp

#get the most count
max=0
for k in range(len(x0)):
    for u in range(len(y0)):
        if max<int(Record.get((x0[k], y0[u])) or 0):
            max=int(Record[(x0[k], y0[u])] or 0)
            Xa =x0[k]
            Ya= y0[u]
print("max count is ",max," x0= ",Xa, " y0 = ",Ya)
print(Record)
