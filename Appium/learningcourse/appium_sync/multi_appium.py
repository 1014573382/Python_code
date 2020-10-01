"""
 使用Python脚本启动单个(多个)appium服务：
 host：127.0.0.1
 port：4723
"""
import subprocess
from time import ctime


def appium_start(host, port):
    bootstrap_port = str(port + 1)
    cmd = 'start /b appium -a ' + host + ' -p ' + str(port) + ' -bp ' + str(bootstrap_port)

    print('%s at %s' %(cmd, ctime()))
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

    subprocess.Popen(cmd, shell = True, stdout=open('./appium_log/' + str(port) + '.log','a'), stderr=subprocess.STDOUT)


if __name__ == '__main__':
    host = '127.0.0.1'
    port = 4723
    appium_start(host, port)
    # for i in range(2):
    #     port = 4723 + 2 * i
    #     appium_start(host, port)
