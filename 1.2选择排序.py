# -*- coding:utf-8 -*-
# @Time      : 2020-09-14
# @Author    : xml
import random
from cal_time import *

@cal_time
def select_sort(li):
    '''时间复杂度：O(n2)'''
    for i in range(len(li) - 1):                  # 排序趟数 = 列表长度-1
        min_loc = i                               # 待排序区域 默认最小值为第一个数
        for j in range(min_loc + 1, len(li)):     # 排序区
            if li[j] < li[min_loc]:               # 判断当前值是否小于初始值
                min_loc = j                       # 初始值 == 当前值 定位
        li[i], li[min_loc] = li[min_loc], li[i]   # 最小值替换到无序区初始位置
        # print(li)

if __name__ == '__main__':
    li = list(range(10000))
    random.shuffle(li)

    select_sort(li)

'''
---- select_sort ----
Running Time: 2.0923352241516113 secs.
'''