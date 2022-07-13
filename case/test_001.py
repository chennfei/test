# _*_ coding: UTF-8 _*_
# @Time     : 2021/4/29 下午 05:36
# @Author   : Li Jie
# @Site     : http://www.hzdledu.com/
# @File     : mainPage_001_enter_mall.py
# @Software : PyCharm

from selenium import webdriver
import unittest
import time
import os

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class Test(unittest.TestCase):
    def setUp(self) -> None:
        # 获取当前文件目录和上层目录绝对路径
        cur_dir = os.path.dirname(os.path.abspath(__file__))
        parent_dir = os.path.dirname(cur_dir)

        self.driver = webdriver.Chrome(os.path.join(parent_dir, "common/chromedriver.exe"))  # chromedriver版本为103.114
        self.url = "http://127.0.0.1:8080/shouan_insurance/shouan_index"
        # 设置显式等待
        self.wait = WebDriverWait(self.driver, 15)

        # 最大化浏览器
        self.driver.maximize_window()

    def test(self):
        # 打开网址
        self.driver.get(r"https://www.jd.com/")

        # 等待搜索输入框
        self.wait.until(ec.visibility_of_element_located((By.ID, "key")))
        # 搜索产品
        self.driver.find_element(By.ID, "key").send_keys('T恤')

        self.wait.until(ec.visibility_of_element_located((By.XPATH, '//*[@id="search"]/div/div[2]/button')))
        # 点击搜索按键
        self.driver.find_element(By.XPATH, '//*[@id="search"]/div/div[2]/button').click()

        # 点击销量
        self.wait.until(ec.visibility_of_element_located((By.XPATH, '//*[@id="J_filter"]/div[1]/div[1]/a[2]')))
        self.driver.find_element(By.XPATH, '//*[@id="J_filter"]/div[1]/div[1]/a[2]').click()

        # 循环打开销量前5
        for i in range(1, 6):
            self.wait.until(
                ec.visibility_of_element_located((By.XPATH, f'//*[@id="J_goodsList"]/ul/li[{i}]/div/div[1]')))
            self.driver.find_element(By.XPATH, f'//*[@id="J_goodsList"]/ul/li[{i}]/div/div[1]').click()

    def tearDown(self) -> None:
        # 关闭浏览器
        self.driver.close()
