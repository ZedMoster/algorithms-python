# -*- coding:utf-8 -*-
# @Time      : 2020-09-13
# @Author    : xml

from cal_time import *

@cal_time
def linear_search(val, data):
    '''顺序查找 时间复杂度：O(n)'''
    for key,value in enumerate(data):
        if value == val:
            return key
    else:
        return None

@cal_time
def binary_search(val, data):
    '''二分查找候选值 data有序列表 时间复杂度：O(logn)'''
    left = 0                        # 列表左侧定位
    right = len(data) - 1           # 列表右侧定位
    while left <= right:            # 列表区间有值
        mid = (left + right) // 2   # 列表中间值的定位
        if data[mid] == val:        # 列表 mid值 == val
            return mid              # 返回定位 mid
        elif data[mid] > val:       # 如果 mid值 大于 val
            right = mid - 1         # 列表右侧区间定位 == mid-1
        else:                       # 如果 mid值 小于 val
            left = mid + 1          # 列表左侧区间定位 == mid+1
    else:
        return None                 # 列表不包含指定值


# 创建列表
li = list(range(100000))

print(linear_search(37778, li))
print(binary_search(37778, li))

'''
linear_search running time: 0.017011165618896484 secs.
377777
binary_search running time: 0.0 secs.
377777
'''


