# _*_ coding: UTF-8 _*_
# @Time     : 2020/9/17 下午 02:45
# @Author   : Li Jie
# @Site     : http://www.cdtest.cn/
# @File     : run.py
# @Software : PyCharm

import unittest
from common.HTMLTestRunner import HTMLTestRunner

# 1.生成测试套件：以文件扫描的方式添加用例到测试套件
# unittest.defaultTestLoader.discover(扫描的文件夹路径, pattern='扫描的文件格式')
suite = unittest.defaultTestLoader.discover('./case/', pattern='*.py')

# 2.生成HTML运行器
file = open('./report/report.html', mode='wb')
runner = HTMLTestRunner(file, title='测试报告', description='汇智动力')

# 3.运行器执行测试套件
runner.run(suite)

# 4.关闭文件
file.close()
