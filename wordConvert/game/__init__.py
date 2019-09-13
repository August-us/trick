import pandas as pd
from time import time

data = pd.read_excel(r'D:\document\Dinary\2019\timeAllocation.xlsx')
start=time()
# for idx,item in data.iterrows():
#     print(item)
# 0.10770773887634277

# for i in range(len(data)):
#     print(data.iloc[i])
#  0.11073756217956543

# data.apply(lambda x: x if print(x) or True else x)
# 0.03792858123779297

print(time()-start)