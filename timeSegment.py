import pandas as pd
import numpy as np
import matplotlib
from datetime import datetime,timedelta
#指定默认字体
matplotlib.rcParams['font.sans-serif'] = ['FangSong']
matplotlib.rcParams['font.family']='sans-serif'
#解决负号'-'显示为方块的问题
matplotlib.rcParams['axes.unicode_minus'] = False
# from matplotlib.font_manager import FontProperties
# myfont = FontProperties(fname=r'C:/Windows/Fonts/simkai.ttf')

import matplotlib.pyplot as plt

labels = ['计算机专业', '语言能力', '视野广度', '健身和打理', '社交', '意识提升']

def data_pic(data,time='周'):
    # print(data)
    """
    技能点数的绘制
    :param data: 时间分配数据
    :return: 技能图
    """
    # 解析出类别标签和种类
    kinds = list(data.iloc[:, 0])

    # 由于在雷达图中，要保证数据闭合，这里就再添加'计算机专业'列，并转换为 np.ndarray
    data_ = pd.concat([data, data[['计算机专业']]], axis=1)

    centers = np.array(data_.iloc[:, 1:])

    # 分割圆周长，并让其闭合
    n = len(labels)


    angle = np.linspace(0, 2 * np.pi, n, endpoint=False)
    angle = np.concatenate((angle, [angle[0]]))

    # 绘图
    plt.figure(1,figsize=(18,18))
    ax = plt.subplot(221, polar=True)  # 参数polar, 以极坐标的形式绘制图形

    # 画线
    for i in range(len(kinds)):
        ax.plot(angle, centers[i], linewidth=2, label=kinds[i])
        # ax.fill(angle, centers[i])  # 填充底色

    # 添加属性标签
    ax.set_thetagrids(angle * 180 / np.pi, labels)
    plt.title('时间分配')
    plt.legend(loc='lower right')
    """
    折线图的绘制
    """
    ax=plt.subplot(222)
    x = np.arange(len(data.columns)-1)
    for row in data.values:
        # print(x, row)
        plt.plot(x, row[1:], 's-', label=int(row[0]))
    plt.xlabel('任务')
    plt.ylabel('时间')
    plt.legend()
    plt.xticks(x, data.columns[1:])
    '''
    柱状图
    '''
    plt.subplot(223)
    ytotal = data.sum().values
    if len(ytotal)==len(data.columns):
        ytotal=ytotal[1:]
    # print(x,ytotal)

    total_width, n = 0.3, 1  # 有多少个类型，只需更改n即可
    width = total_width / n
    # x = x +( width) / 2
    plt.bar(x, ytotal, color="#ff9999", edgecolor="k", width=width)  # edgecolor柱状边框颜色，hatch填充的内容
    for x_, y, in zip(x,ytotal):
        plt.text(x_, y + 0.05, '%.2f' % y, ha='center', va='bottom')
    # plt.bar(x + width, y, color="w", edgecolor="k", width=width, hatch="+", label='MATT-CNN')
    # plt.bar(x + 2 * width, y, color="w", edgecolor="k", width=width, hatch="*", label='ATT-RLSTM')
    # plt.bar(x + 3 * width, y, color="w", edgecolor="k", width=width, hatch="\\", label='CNN-RLSTM')
    plt.xlabel("任务")
    plt.ylabel("时间")
    # plt.legend(loc="best")
    plt.xticks(x, data.columns[1:])
    plt.title('一%s总任务时长   总时长：%.1f'%(time,ytotal.sum()))

    '''
    饼图
    '''
    plt.subplot(224)  # 调节图形大小
    colors = ['red', 'yellowgreen', 'lightskyblue', 'yellow']  # 每块颜色定义
    explode = [0.01]*len(x)  # 将某一块分割出来，值越大分割出的间隙越大
    patches, text1, text2 = plt.pie(ytotal,
                                    explode=explode,
                                    labels=labels,
                                    counterclock=False,
                                    # colors=colors,
                                    autopct='%3.2f%%',  # 数值保留固定小数位
                                    shadow=False,  # 无阴影设置
                                    startangle=90,  # 逆时针起始角度设置
                                    pctdistance=0.6)  # 数值距圆心半径倍数距离
    # patches饼图的返回值，texts1饼图外label的文本，texts2饼图内部的文本
    # x，y轴刻度设置一致，保证饼图为圆形
    plt.axis('equal')

    plt.show()


def report(data,type,year=2019,month=0,week=0,day=0):
    yearDict={2019:0}
    if type=='m':
        months1 = [0, 31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335, 366]  # 闰年
        months2 = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 365]  # 平年

        if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0):
            begin = months1[month - 1]
            end=months1[month]
        else:
            begin = months2[month - 1] + day
            end = months2[month]
        print(begin,end)
        start = str(data['时间'][0])
        start = datetime(int(start[:4]), int(start[4:6]), int(start[6:]))
        start=months1[start.month-1]+start.day-2
        begin=max(0,begin-start)
        end=min(end-start,len(data))
        print(data[begin:end])
        return data[begin:end]
    if type=='w':
        if month==0 or day==0:
            today=str(data['时间'][-1])
            today = datetime(int(today[:4]),int(today[4:6]),int(today[6:]))
        else:
            today=datetime(year,month,day)
        weekday = today.weekday()
        start = today + timedelta(0 - weekday)
        end = today + timedelta(6 - weekday)
        if week == 0:
            start = datetime(start.year, start.month, start.day)
            end = datetime(end.year, end.month, end.day)
        elif start.year==year:
            deltaWeek=int(start.isocalendar()[1])-week
            start = datetime(start.year, start.month, start.day)-7*deltaWeek
            end = datetime(end.year, end.month, end.day)-7*deltaWeek

        return date[start: end]
    if type=='y':
        begin,end=0,0
        if year in yearDict:
            begin=yearDict[year]
            return data
        if (year+1) in yearDict:
            end=yearDict[year+1]
            return data[begin:end]
        else:
            return data[begin:]
if __name__ == '__main__':
    data=pd.read_excel(r'D:\document\Dinary\2019\timeAllocation.xlsx')
    # ['计算机专业', '语言能力', '视野广度', '健身和打理', '社交', '意识提升']
    # data.loc[len(data)]=['20190927',6,0.,1,0,1.0,0.]
    # test(data)
    date=str(data.loc[len(data)-1]['时间'])
    date=list(map(int,[date[0:4],date[4:6],date[6:8]]))
    week=datetime(date[0],date[1],date[2]).isocalendar()[1]-22
    index=week*7
    # print(data[index:])
    # data_pic(report(data,type='m',month=8),'月')
    # print(data[index:])
    data_pic(data[index:])
    # data.to_excel(r'D:\document\Dinary\2019\timeAllocation.xlsx',index=False)
