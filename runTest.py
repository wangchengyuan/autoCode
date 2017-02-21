import unittest
from bin.sendMail import sendMail

testDir='./case/'
discover=unittest.defaultTestLoader.discover(testDir,'test*.py')

if __name__ == '__main__':
    mail=sendMail()
    mail.send_mail()