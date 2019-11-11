#coding:utf-8
import unittest
import HTMLTestRunner
from LX import *
class Testxl(unittest.TestCase):
    # TestCase基类方法，所有case执行之前自动执行
    @classmethod
    def setUpClass(cls):
        print('测试用例前的准备工作')
    @classmethod
    def tearDownClass(cls):
        print('测试用例后的清理工作')
    # 测试前准备环境的搭建(setUp)
    def setUp(self):
        print('这是一个用例前的准备工作')
    # 测试后环境的还原(tearDown),相当于初始化
    def tearDown(self):
        print('这是一个用例后的清理工作')
    def test_add(self):
        self.assertEqual(3,add(1,2))
        print('执行完毕1')
        # self.assertEqual(4,add(2,3))
    def test_a(self):
        self.assertEqual(3,a(9,6))
        print('执行完毕2')
        # self.assertEqual(3, a(12, 6))
    def test_ad(self):
        # self.assertEqual(3, ad(9, 6))
        self.assertEqual(18, ad(3, 6))
        print('执行完毕3')
    def test_dd(self):
        self.assertEqual(3, dd(9, 3))
        print('执行完毕4')
        # self.assertEqual(3, dd(12, 6))

if __name__ == '__main__':
######## 第一种方法：
     # verbosity报告的详细程度
     # unittest.main(verbosity=2)
######## 第二种方法：
    # 实例化unittest对象
    # suite = unittest.TestSuite()
     # 调用TestSuite类中的addTest：suite.addTest(类名(‘类中的方法名’))
     # 执行顺序是按照添加的顺序执行，先添加的先执行
    # suite.addTest(Testxl('test_dd'))
    # suite.addTest(Testxl('test_a'))
    # runner = unittest.TextTestRunner()
    # runner.run(suite)
######## 第三种方法：
    # start_dir ：要测试的模块名或测试用例目录。（采用双斜线或目录前加r）
    # pattern='test*.py' ：表示用例文件名的匹配原则。星号“*”表示任意多个字符。
    # top_level_dir=None：测试模块的顶层目录。如果没顶层目录（也就是说测试用例不是在该目录下则需要分别指定），默认为 None。
    discover = unittest.defaultTestLoader.discover('F:\\test\\code\\vip3test\\unittest_lx',pattern='test*.py',top_level_dir=None)
    print('11111')
    filename = 'F:\\test\\code\\vip3test\\unittest_lx\\result.html'
    fp = open(filename,'wb')
    print('报告')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream =fp,
        title =u'测试报告',
        description = u'用例执行情况'
    )
    print('报告写入完毕')
    runner.run(discover)
    fp.close()