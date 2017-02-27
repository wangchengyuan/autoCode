'''
from selenium import  webdriver
from selenium.webdriver.common.by import By

driver=webdriver.PhantomJS(executable_path='C:\\python\\phantomjs\\bin\\phantomjs.exe')
driver.get("http://www.baidu.com")
if driver.find_element(By.ID,"kw"):
    print("测试OK")
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest

class testPhantomJS(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_phantomJS(self):
        driver=webdriver.PhantomJS(executable_path='C:\\python\\phantomjs\\bin\\phantomjs.exe')
        driver.get("http://www.baidu.com")
        self.assertTrue(driver.find_element(By.ID,"kw"))

    def test_phantomJS1(self):
        driver=webdriver.PhantomJS(executable_path='C:\\python\\phantomjs\\bin\\phantomjs.exe')
        driver.get("http://www.baidu.com")
        self.assertTrue(driver.find_element(By.ID,"kw1"))

    if __name__ == '__main__':
        unittest
