# -*- coding:utf-8 -*-
# @Time      : 2020-09-13
# @Author    : xml

import time

# 装饰器
def cal_time(func):
    # 计算 func 函数运行时间
    def wrapper(*args, **kwargs):
        start_time = time.time()  # 这个是程序开始时间
        res = func(*args, **kwargs)
        end_time = time.time()  # 这个是程序结束时间
        print("---- %s Running Time ----\n%s secs." % (func.__name__, end_time - start_time))
        return res
    # 返回装饰器.函数名称
    return wrapper


