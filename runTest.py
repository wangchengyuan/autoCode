import unittest
from bin.sendMail import sendMail
from bin.configRead import configRead
import os
from HTMLTestRunner import HTMLTestRunner


testDir='./case/'
discover=unittest.defaultTestLoader.discover(testDir,'case*.py')

if __name__ == '__main__':
   # mail=sendMail()
    #mail.send_mail()
   '''
   filename="test"
   fp=open(filename,"wb")
   runner=HTMLTestRunner(stream=fp,title='测试报告',description='用例执行情况：')
   runner.run(discover)
   fp.close()

   #提取最新的测试报告

   #发送测试报告
   '''
   runner=unittest.TextTestRunner()
   runner.run(discover)