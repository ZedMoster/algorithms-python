# -*- coding:utf-8 -*-
# @Time      : 2020-09-19
# @Author    : xml

import random
from cal_time import *


class HeapSort():

    def __init__(self):
        pass

    def shitDown(self, li, low, high):
        '''创建大根堆 向下调整'''
        i = low                                    # 堆节点指针
        j = 2 * i + 1                              # 堆孩子左节点指针
        temp = li[i]                               # 堆元素
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

    def shitUp(self, li, low, high):
        '''创建小根堆 向下调整'''
        i = low                                    # 堆节点指针
        j = 2 * i + 1                              # 堆孩子左节点指针
        temp = li[i]                               # 堆元素
        while j <= high:
            if j + 1 <= high and li[j] > li[j+1] : # 判断孩子节点的指针位置
                j += 1                             # 指针指向右孩子
            if temp > li[j]:                       # 判断对丁元素是否进行归位
                li[i] = li[j]                      # 孩子元素上去
                i = j                              # 节点指针 = 孩子节点指针
                j = 2 * i + 1                      # 左孩子节点 = 节点指针*2 +1
            else:
                break
        li[i] = temp                               # 堆元素进行归位

    @cal_time
    def heap_shitDown(self, li, sort = False):
        '''
        创建大根堆
            时间复复杂度：O(nlogn)
        :param li: 列表
        :param sort: 是否排序除数
        :return: None
        '''
        n = len(li) -1
        # 创建堆
        for i in range((n-1)//2, -1, -1):
            # i 表示对节点元素的指针
            self.shitDown(li, i, n)

        if sort:
            # 挨个出数
            for i in range(n, -1, -1):
                # 数放到末尾
                li[0], li[i] = li[i], li[0]
                # 范围重新归位
                self.shitDown(li, 0, i-1)

    @cal_time
    def heap_shitUp(self, li, sort = False):
        '''
        创建小根堆
            时间复复杂度：O(nlogn)
        :param li: 列表
        :param sort: 是否排序除数
        :return: None
        '''
        n = len(li) - 1
        # 创建堆
        for i in range((n - 1) // 2, -1, -1):
            # i 表示对节点元素的指针
            self.shitUp(li, i, n)

        if sort:
            # 挨个出数
            for i in range(n, -1, -1):
                # 数放到末尾
                li[0], li[i] = li[i], li[0]
                # 范围重新归位
                self.shitUp(li, 0, i - 1)

    @cal_time
    def topKing(self, li, k):
        n = k - 1
        heap = li[0:k]
        # 创建 k个元素的 K堆
        for i in range((n - 1) // 2, -1, -1):
            # i 表示对节点元素的指针
            self.shitUp(heap, i, n)

        # 遍历列表维护 K堆 heap
        for i in range(k, len(li)-1):
            if li[i] > heap[0]:
                heap[0] = li[i]
                self.shitUp(heap, 0 , n)
        # 挨个出数 K堆 heap
        for i in range(k-1, -1, -1):
            heap[0], heap[i] = heap[i], heap[0]
            self.shitUp(heap, 0, i-1)
        return heap

if __name__ == '__main__':
    li = list(range(1000))
    random.shuffle(li)

    heap = HeapSort()

    # 创建堆
    heap.heap_shitDown(li)
    print(li)
    heap.heap_shitUp(li)
    print(li)

    # 排序
    heap.heap_shitDown(li, True)
    print(li)
    heap.heap_shitUp(li, True)
    print(li)

    # topKing
    a = heap.topKing(li, 10)
    print(a)


'''
---- heap_sort ----
Running Time: 0.027005910873413086 secs.

创建的大根堆
[9, 6, 8, 4, 3, 7, 5, 0, 2, 1]
      9
   6     8
 4   3 7   5
0 2 1
'''
