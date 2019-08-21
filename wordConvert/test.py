import re

str='''16、  难易程度:较难   知识范围:基础2 03    答案 :Y  频度\n              \r
比起普通5类双绞线,超5类系统在100MHz的频率下运行时，为用户(  )提供8dB近端串扰的余量，用户的设备受到的干扰只有普通5类线系统的1/4。
'''

str1='常用的屏幕分辨率是（   ）'
str2='1.	难易程度:较难    答案: BC'
# print(re.sub(r'[\(,（]\s*[\),）]','( Y )',str,count=1))
# a=re.findall(r'\d\.|\d、|[A-DYN]',str)
print(re.findall(r'答案\s*?[:：]\s*?([A-H]+)',str2))
print(str.count('16'))


# part1, answer = str.split('答案:')
# index,analysis=part1.split('难易程度')
# print(answer)
import traceback
try:
    raise Exception('123')
except Exception as e:
    import sys
    exc_type,exc_value,traobj=sys.exc_info()
    # print(exc_type)
    # print(exc_value)
    # print(traobj)
    print(traceback.print_exc( ))

import os
from tkinter import filedialog




