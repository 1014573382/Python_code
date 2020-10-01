import unittest
from BSTestRunner import BSTestRunner
from test_project.mysql_action import DB
import time
import yaml
import logging.config

# 引入日志配置文件
CON_LOG = 'log.conf'
logging.config.fileConfig(CON_LOG)
# 定义一个日志采集器
logging = logging.getLogger()


# 数据初始化操作
db = DB()
with open('datas.yaml','r')as f:
    datas = yaml.load(f)
    db.init_data(datas)

# 指定测试用例和测试报告的路径
test_path = '.'
report_path = './report'

#加载测试用例
discover = unittest.defaultTestLoader.discover(test_path, pattern='test_django_restful.py')

# 定义报告的文件格式
date = time.strftime('%Y-%m-%d_%H-%M-%S')
report_name = report_path + date + 'test_report.html'

# 运行测试用例并生成测试报告
with open(report_name, 'wb')as f:
    runner = BSTestRunner(stream=f,title="API Test Report.",description="Django Restful API Test Report")
    logging.info('============API Test====================')
    runner.run(discover)
