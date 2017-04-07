# coding=utf-8
'''
Created on 
@author: 
Project:登录百度测试用例
'''
from selenium import webdriver
import unittest, time, ddt, os
from Common.ExcelUtil import ExcelUtil
from gevent.hub import sleep

# 获取当前工程目录下的Excel文件，可根据实际情况进行调整
excel_path = os.path.abspath("E:\workspace\Web_UI_AutoTest\Data\Data.xls")
# 获取对应Excel文件中对应的Sheet，在测试编码过程中进行调整
excel = ExcelUtil(excel_path, 'Sheet2') 

@ddt.ddt
class BaiduTest(unittest.TestCase):
    u"""百度测试"""
    @classmethod
    def setUp(self):
        # drive_path = os.path.abspath(".\geckodriver.exe")
        # drive_path = os.path.abspath(".\geckodriver.exe")
        # self.driver.implicitly_wait(2)
        # self.addCleanup(self.driver.quit)

        self.driver = webdriver.Firefox()
        self.driver.maximize_window()        
        sleep (3)  # 隐性等待时间为30秒
        self.base_url = "https://www.baidu.com"
    @ddt.data(*excel.next()) 
    def test_baidu(self, data):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_xpath(".//*[@id='kw']").clear()
        driver.find_element_by_xpath(".//*[@id='kw']").send_keys(data['username'])
        driver.find_element_by_id("su").click()
        time.sleep(3)
        title = driver.title
        self.assertEqual(title, data['username'] + u"_百度搜索") 
    @classmethod
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
