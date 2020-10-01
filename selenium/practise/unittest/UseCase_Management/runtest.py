# 使用discover 可以一次调用多个脚本
# test_dir 被测试脚本的路径
# pattern 脚本名称匹配规则

import unittest
test_dir = "./"  #表示脚本的当前路径
discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')

if __name__ == '__main__':
    # TextTestRunner() 文本测试用例运行器
    # verbosity参数可以控制执行结果的输出，0 是简单报告，1 是一般报告（默认），3 是详细报告
    runner = unittest.TextTestRunner(verbosity=3)
    runner.run(discover)