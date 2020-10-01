import os
import socket
import logging
import logging.config
import subprocess
from time import ctime
from time import sleep


CONF_LOG = '../config/log.conf'
logging.config.fileConfig(CONF_LOG)
logging = logging.getLogger()


def check_port(host, port):
    """检测指定的端口是否被占用"""
    # 创建socket对象
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    try:
        s.connect((host, port))
        s.shutdown(2)
        # shutdown(self, flag)：禁止在一个Socket上进行数据的接收与发送。
        # 利用shutdown()函数使socket双向数据传输变为单向数据传输。
        # shutdown()需要一个单独的参数， 该参数表示了如何关闭socket
        # 0 表示禁止将来读； 1 表示禁止将来写  2 表示禁止将来读和写。
    # 如果连接不成功，表示端口未启动，即端口可用
    except OSError as msg:
        logging.info('port %s is avaiable' %port)
        return True

    else:
        # 如果连接成功，表示端口已经启动
        print('port %s already be in use!' % port)
        return False


def release_port(port):
    cmd_find = 'netstat -ano |findstr %s' % port
    print(cmd_find)

    result = os.popen(cmd_find).read()
    print(result)

    if str(port) and 'LISTENING' in result:
        # 获取端口对应的pid进程
        i = result.index('LISTENING')  # 获取字符串‘LISTENING’的索引下标
        start = i + len('LISTENING') + 7
        end = result.index('\n')  # PID结束于换行符
        pid = result[start: end]  # 字符串切片操作

        # 通过PID关闭被占用的端口
        cmd_kill = 'taskkill -f -pid %s' % pid
        print(cmd_kill)
        os.popen(cmd_kill)

    else:
        print('Port %s is available!' % port)


def appium_start(host, port):
    bootstrap_port = str(port + 1)
    appium_cmd = 'start /b appium -a ' + host + ' -p ' + str(port) + ' -bp ' + str(bootstrap_port)
    logging.info('%s at %s' %(appium_cmd, ctime()))
    # 用subprocess这个模块来产生子进程, 并连接到子进程的标准输入 / 输出 / 错误中去，还可以得到子进程的返回值。
    # subprocess.Popen(args, bufsize=0, executable=None, stdin=None, stdout=None, stderr=None, preexec_fn=None,
    #                  close_fds=False, shell=False, cwd=None, env=None, universal_newlines=False, startupinfo=None,
    #                  creationflags=0)
    # args：表示要执行的命令。必须是一个字符串，字符串参数列表。
    # shell：如果该参数为True，将通过操作系统的shell执行指定的命令。
    # stdin：指定子进程的标准输入；
    # stdout：指定子进程的标准输出；
    # stderr：指定子进程的标准错误输出；
    # stderr的值还可以是STDOUT，表示子进程的标准错误也输出到标准输出。
    subprocess.Popen(appium_cmd, shell=True, stdout=open('../log/' + str(port) + '.log', 'a'), stderr=subprocess.STDOUT)


def start_appium_action(host, port):
    # 检测端口是否被占用，没被占用则启动appium服务
    if check_port(host, port):
        appium_start(host, port)
        sleep(5)
        return True
    else:
        logging.info('The appium server has already started!')



if __name__ == '__main__':
    host = '127.0.0.1'
    port = 4723
    start_appium_action(host, port)
    check_port(host, port)