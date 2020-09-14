# -*- coding:utf-8 -*-
# @Time      : 2020-09-14
# @Author    : xml

def select_sort(li):
    for i in range(len(li)):
        temp = i
        for j in range(temp, len(li)):
            if li[j] < li[i]:
                li[i], li[j] = li[j], li[i]


li = [1,12,584,6,4]

select_sort(li)
print(li)