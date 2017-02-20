import unittest

testDir='./case/'
discover=unittest.defaultTestLoader.discover(testDir,'test*.py')

if __name__ == '__main__':
    runner=unittest.TextTestRunner()
    runner.run(discover)