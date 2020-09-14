# -*- coding:utf-8 -*-
# @Time      : 2020-09-13
# @Author    : xml

def hanno(n, a, b, c):
    '''将 n 个盘子从 a 经过 b 移动到 c'''
    if n > 0:
        hanno(n-1, a, c, b)                    # 将 n-1 个盘子从 a, 经过 c, 移动到 b
        print("moving from %s to %s" %(a, c))  # 将第 n 个盘子从 a, 移动到 c
        hanno(n-1, b, a, c)                    # 将 n-1 个盘子从 b, 经过 a, 移动到 c

hanno(3, "A", "B", "C")

'''
moving from A to C
moving from A to B
moving from C to B
moving from A to C
moving from B to A
moving from B to C
moving from A to C
'''