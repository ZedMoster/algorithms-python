# -*- coding:utf-8 -*-
# @Time      : 2020-09-13
# @Author    : xml

import random
from cal_time import *

@cal_time
def bubble_sort(li):
    '''时间复杂度：O(n2)'''
    for i in range(len(li) - 1):
        nochange = True
        for j in range(len(li)-i-1):
            if li[j] > li[j+1]:
                li[j],  li[j+1] = li[j+1], li[j]
                nochange = False
        # 本次冒泡未作交换 表示列表已经有序
        if nochange:
            break
        # print(li)

if __name__ == '__main__':
    li = list(range(10000))
    random.shuffle(li)

    bubble_sort(li)

'''
---- bubble_sort ----
Running Time: 7.220380783081055 secs.
'''