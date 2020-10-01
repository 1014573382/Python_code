import logging

# basicConfig部分参数：filename 指定日志文件名称
# filemode 指定打开文件的模式，如果指定了filename（如果文件模式未指定，则默认为'a）
# format 为处理程序使用指定的格式字符串。
# datefmt 使用指定的日期/时间格式。样式如果指定了格式字符串，则使用它来指定格式字符串的类型.
# level 将根记录器级别设置为指定级别。

# 输出dubug以上级别的所有信息
logging.basicConfig(level=logging.DEBUG, filename='runlog.log', filemode='a',
                    format = '%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s %(message)s')
# logging.basicConfig(level=logging.INFO)
# logging.basicConfig(level=logging.WARNING)
# logging.basicConfig(level=logging.ERROR)

logging.debug('debug info')
logging.info('hello guoxl')
logging.warning('warning info')
logging.error('error info')
logging.critical('critical info')