# -*- coding:utf-8 -*-
# @Time      : 2020-09-19
# @Author    : xml

import random
from cal_time import *

def merge(li, left, mid, right):
    i = left
    j = mid + 1
    lTemp = []
    while i <= mid and j <= right:
        if li[i] < li[j]:
            lTemp.append(li[i])
            i += 1
        else:
            lTemp.append(li[j])
            j += 1
    # 单边数据为空列表
    while i <= mid:
        lTemp.append(li[i])
        i += 1
    while j <= right:
        lTemp.append(li[j])
        j += 1
    # 列表写回
    li[left:right + 1] = lTemp

def _merge_sort(li, left ,right):
    # 列表分段中至少右两个元素
    if left < right:
        mid = (left + right) // 2
        _merge_sort(li, left, mid)
        _merge_sort(li, mid+1, right)
        merge(li, left, mid, right)

@cal_time
def merge_sort(li):
    '''时间复复杂度：O(nlogn)'''
    left = 0
    right = len(li) - 1
    _merge_sort(li, left , right)

if __name__ == '__main__':
    li = list(range(1000))
    random.shuffle(li)

    merge_sort(li)


'''
---- merge_sort ----
Running Time: 0.0020008087158203125 secs.
'''