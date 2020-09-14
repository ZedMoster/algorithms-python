# -*- coding:utf-8 -*-
# @Time      : 2020-09-13
# @Author    : xml

import random

def bubble_sort(li):
    '''列表进行冒泡排序 时间复杂度：O(n2)'''
    for i in range(len(li) - 1):
        nochange = True
        for j in range(len(li)-i-1):
            if li[j] > li[j+1]:
                li[j],  li[j+1] = li[j+1], li[j]
                nochange = False
        # 本次冒泡未作交换 表示列表已经有序
        if nochange:
            break
        print(li)     # 打印本次排序后的列表结果


# li = [random.randint(0,11) for i in range(10)]
li = [9,8,7,1,2,3,4]

print(li) # 打印原始列表
print("-----")
bubble_sort(li)

'''
[9, 8, 7, 1, 2, 3, 4]
-----
[8, 7, 1, 2, 3, 4, 9]
[7, 1, 2, 3, 4, 8, 9]
[1, 2, 3, 4, 7, 8, 9]
'''