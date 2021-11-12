# -*- coding: utf-8 -*-
# Author: DSN2002
# Date: 2021-11-12 15:10
# LastEditTime: 2021-11-12 19:09
# LastEditors: DSN2002
# Description:
# 仅供研究使用，请勿用于其他活动
#

import time
from ctypes import *
import os
os.add_dll_directory("D:\Program\code\git\lazycode\测试")
num = int(input("请输入整数值\n"))
url1 = str(input("请输入url\n"))
result = 0
start_time = time.time()
result = cdll.LoadLibrary("D:\Program\code\git\lazycode\测试\mymath.dll")
print(result.add(9,9))
print(result.sum(num))
url1 = url1.encode('ascii')
print(result.url(url1))

end_time = time.time()
print("总共用时%s"%(end_time-start_time))
