# -*- coding:utf-8 -*-
# @Time      : 2020-09-14
# @Author    : xml

import random
from cal_time import *

# 列表中左侧值归位
def partition(li, left, right):
    temp = li[left]                                  # 默认开始提取最左侧的值
    while left < right:                              # 左右区间范围指针
        while li[right] >= temp and left < right:    # 从右往左找比temp小的数
            right -= 1                               # 范围向左侧缩小一步
        li[left] = li[right]                         # 把右侧的值写入到左侧空位

        while li[left] <= temp and left < right:     # 从左往右找比temp小的数
            left += 1                                # 范围向右侧缩小一步
        li[right] = li[left]                         # 把左侧的值写入到右侧空位
    # 将temp 数据列表归位
    li[left] = temp
    return left

def _quick_sort(li, left, right):
    '''时间复杂度：O(nlogn)'''
    if left < right:                       # 至少右两个元素
        mid = partition(li, left, right)   # 归位最左侧元素
        _quick_sort(li, left, mid-1)        # 归位元素 左侧区域
        _quick_sort(li, mid+1, right)       # 归位元素 右侧区域

@cal_time
def quick_sort(li, left, right):
    _quick_sort(li, left, right)

if __name__ == '__main__':
    li = list(range(10000))
    random.shuffle(li)

    quick_sort(li, 0, len(li)-1)

'''
---- quickSort ----
Running Time: 0.019521474838256836 secs.
'''