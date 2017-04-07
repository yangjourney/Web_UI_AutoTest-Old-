# -*- coding: utf-8 -*-

import unittest,time
from Common.Selenium_Webdriver import webutils

class Test(unittest.TestCase):


    def setUp(self):
        self.driver = webutils()
        self.driver.wait(20)
        

    def testName(self):
        driver = self.driver
        driver.get("http://www.baidu.com/")
        driver.send_keys("xpath,.//*[@id='kw']", "ceshi")
        driver.click("id,su")
        time.sleep(5)
        self.assertEqual(driver.get_title(), u"测试_百度搜索") 
    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":

    unittest.main()