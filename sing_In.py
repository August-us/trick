import pandas as pd
pd.set_option('display.width', 1000)  # 设置字符显示宽度
pd.set_option('display.max_rows', None)  # 设置显示最大行

data=pd.read_excel('E:\FileRecv\工学班信息终版.xlsx')
data2=pd.read_excel(r'C:\Users\Administrator\Downloads\关注名单.xls')
# print(data2['姓名'][0]=='何林')

# res=pd.merge(data2['姓名'].to_frame(),data['姓名'].to_frame(),how='left')
data=data['姓名'].append(data2['姓名'])
print(data.drop_duplicates(keep=False))
