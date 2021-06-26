import pandas as pd


nameList = '''胡洁  罗赛男  何林  曾锡祥  黎桥飞  白莉婷  刘平  田少卿  董泽乾  武红昌  袁航  于子勇'''.split('  ')

# applicationForm = pd.read_excel('毕业典礼报名.xls')
applicationForm = pd.read_excel('23号学校毕业典礼参加情况变动统计.xls')
for name in nameList:
    if name in applicationForm['姓名'].values:
        print(name)