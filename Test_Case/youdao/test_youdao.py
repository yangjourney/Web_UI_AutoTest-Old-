# coding=utf-8
'''
Created on 2016-7-22
@author: Jennifer
Project:使用有道翻译测试用例
'''
from selenium import webdriver
import unittest,time

class YoudaoTest(unittest.TestCase):
    u"""有道测试"""
    def setUp(self):
        # drive_path = os.path.abspath(".\geckodriver.exe")
        # self.driver = webdriver.Firefox(executable_path=drive_path)
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()   
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.youdao.com"
    
    def test_youdao(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_id("translateContent").clear()
        driver.find_element_by_id("translateContent").send_keys(u"你好")
        driver.find_element_by_id("translateContent").submit()
        time.sleep(3)
        page_source = driver.page_source
        self.assertIn("hello", page_source) 

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()