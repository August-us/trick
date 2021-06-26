import pandas as pd
from collections import defaultdict

data = pd.read_excel('gongxue.xls')
res = pd.read_excel('计算机学院毕业照订购统计.xlsx')

statis = defaultdict(lambda : 0)

def add(i):
    statis[i] += 1
for i in data['预购照片编号'].values:
    if isinstance(i, int):
        add(i)
    else:
        for i in i.split('，'):
            add(int(i))
statis['总计'] = sum(statis.values())
statis['班级名'] = '工学班'
# statis['班级名'] = '计算机非全'
# statis['班级名'] = '计算机非全'
print(statis)


# print(pd.DataFrame.from_dict(statis, orient='columns'))
# col = ['班级名', 1,2,3,4,5,6,7,8,9,10,11,12, '总计']

res = res.append(pd.DataFrame(statis, index=['6']))
# res = res[col]
print(res)
# res.to_excel('计算机学院毕业照订购统计.xlsx', header=True, index=False)


