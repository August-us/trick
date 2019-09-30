import os
import pandas as pd

def mergeTable():
    # for file in os.listdir('dmt'):
    #     data=pd.read_excel(os.path.join('dmt',file),header=0)
    pass

def insert():
    data = pd.read_excel('dmt/act.xlsx', header=0)
    res=pd.read_excel('dmt/res.xlsx', header=0)
    act=None
    print(data.notnull())
    for row in data.itertuples():
        if isinstance(getattr(row, '活动名称'),str):
            act=getattr(row, '活动名称')
        res.loc[res['姓名'] == row[2],[act]]=3
        # print(res[res['姓名'] == row[2]][act])
    res['学号 ']=res['学号 '].astype(str)
    res.to_excel('dmt/res1.xlsx', header=True,index=False)

def Total():
    res = pd.read_excel('dmt/score.xlsx', header=0)
    res.fillna(value=0,inplace=True)
    print(res.columns)
    res['总计']=0
    for col in ['学生干部', '安全联络员2分', '高分辨率论坛5分', '一带一路青年创新大会5分',
       '高新前沿技术座谈会5分', '科学道德与学风代表3分', '消防演练3分', '扫黑除恶3分', '5月31日校内专家讲座3分',
       '迎新服务活动3分', '毕业班服务活动3分','院庆得分小计','校趣味运动会3分+n*1', '知识竞赛(组织5分，参加3分)',
        '中兴趣味运动会（组织5分，参加3分）', '篮球联赛', '足球联赛','2018.10.10报告会', '2018.10.12报告会', '2018年10.13报告会', '研会成员']:
        res['总计']+=res[col]
    # res['总计']=res['总计'].astype(int)
    print(res['总计'])
    res.to_excel('dmt/score.xlsx',index=False,header=True)


if __name__ == '__main__':
    Total()