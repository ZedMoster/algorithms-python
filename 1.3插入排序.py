# -*- coding:utf-8 -*-
# @Time      : 2020-09-14
# @Author    : xml
import random
from cal_time import *

@cal_time
def insert_sort(li):
    '''时间复杂度： O(n2)'''
    for i in range(1, len(li)):            # i 表示摸到的牌的下标
        j = i - 1                          # j 表示手里抓牌的下标
        temp = li[i]                       # 摸到的牌的临时变量
        while li[j] > temp and j >= 0:     # 判断已经排序好的牌是否需要移动位置(进行插入动作)
            li[j+1] = li[j]
            j -= 1
        li[j+1] = temp                     # 空位进行填值
        # print(li)

if __name__ == '__main__':
    li = list(range(10000))
    random.shuffle(li)

    insert_sort(li)

'''
---- insert_sort ----
Running Time: 2.9525856971740723 secs.
'''