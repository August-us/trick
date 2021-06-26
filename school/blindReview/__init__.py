# import pandas as pd
#
# score = pd.read_excel('工学班.xlsx')
# idMap = pd.read_excel('工学班毕设论文盲审编号.xlsx')
#
# # print(score[score['分数1']<75])
# del idMap['篇名'], idMap['导师'], idMap['班级']
# print(idMap.head())
# res = pd.merge(left=score, right=idMap, on=['盲审编号'])
# reBilnd = res[res['分数2']< 75]
# print(reBilnd)
# reBilnd.to_excel('工学班毕设论文二次盲审名单.xlsx', index=False, header=True)


# res.to_excel('工学班毕设论文盲审结果.xlsx', index=False, header=True)

#
# import matplotlib.pyplot as plt
# import seaborn as sns
#
# help(sns.lmplot)
#
# # 数据集
# data = sns.load_dataset("fmri")
# print(data.head())
# # 绘画折线图
# sns.barplot(x="timepoint", y="signal", kind="line", data=data, ci=None)
# # 显示
# plt.show()

print((154+66+94+114+133)*12- 132)

