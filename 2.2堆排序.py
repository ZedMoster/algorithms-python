# -*- coding:utf-8 -*-
# @Time      : 2020-09-19
# @Author    : xml

import random
from cal_time import *

def shit(li, low, high):
    '''
    创建大根堆
    :param li:
    :param low:
    :param high:
    :return:
    '''
    i = low               # 堆节点指针
    j = 2 * i + 1         # 堆孩子左节点指针
    temp = li[i]          # 堆元素
    while j <= high:
        if j + 1 <= high and li[j] < li[j+1] : # 判断孩子节点的指针位置
            j += 1                             # 指针指向右孩子
        if temp < li[j]:                       # 判断对丁元素是否进行归位
            li[i] = li[j]                      # 孩子元素上去
            i = j                              # 节点指针 = 孩子节点指针
            j = 2 * i + 1                      # 左孩子节点 = 节点指针*2 +1
        else:
            break
    li[i] = temp                               # 堆元素进行归位

@cal_time
def heap_sort(li):
    '''时间复复杂度：O(nlogn)'''
    n = len(li) -1
    # 创建堆
    for i in range((n-1)//2, -1, -1):
        # i 表示对节点元素的指针
        shit(li, i, n)

    # 挨个出数
    for i in range(n, -1, -1):
        # 数放到末尾
        li[0], li[i] = li[i], li[0]
        # 范围重新归位
        shit(li, 0, i-1)

if __name__ == '__main__':
    li = list(range(10000))
    random.shuffle(li)

    heap_sort(li)
    # print(li)

'''
---- heap_sort ----
Running Time: 0.027005910873413086 secs.
'''
