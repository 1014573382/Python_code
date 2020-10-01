import socket
import os

def check_port(host, port):
    """检测指定的端口是否被占用"""
    # 创建socket对象
    """    
    socket函数的参数：socket(int domain, int type, int protocol)；
    domain：即协议域，又称为协议族。也就是说，利用它来分辨地址的类型。UNIX支持的协议族有：UNIXDomain（AF_UNIX）、
    In-temet（AF_INET）、XeroxNS（AF_NS）等。而Dos和Windows仅支持AF_INET。
    type参数指定所需的通信类型。包括数据流（SOCK_STREAM）、数据报（SOCK - DGRAM）和原始类型（S0CK_RAW）。
    参数protocol说明该套接字使用的协议族中的特定协议。如果调用者不希望特别指定使用的协议，则置为0，使用默认的连接模式。
    """
    # socket.AF_INET 表示使用IPV4

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        s.connect((host, port))
        s.shutdown(2)  # 关闭socket连接
        # shutdown(self, flag)：禁止在一个Socket上进行数据的接收与发送。
        # 利用shutdown()函数使socket双向数据传输变为单向数据传输。
        # shutdown()需要一个单独的参数， 该参数表示了如何关闭socket
            # 0 表示禁止将来读；
            # 1 表示禁止将来写
            # 2 表示禁止将来读和写。
    # 如果连接不成功，表示端口未启动，即端口可用
    except OSError as msg:
        print('port %s is available!' %port)
        # print(msg)
        return True
    else:
        # 如果连接成功，表示端口已经启动
        print('port %s already be in use!' %port)
        return False


def release_port(port):
    cmd_find = 'netstat -ano |findstr %s' %port
    print(cmd_find)

    result = os.popen(cmd_find).read()
    print(result)

    if str(port) and 'LISTENING' in result:
        # 获取端口对应的pid进程
        i = result.index('LISTENING')  #获取字符串‘LISTENING’的索引下标
        start = i + len('LISTENING') + 7
        end = result.index('\n')   # PID结束于换行符
        pid = result[start: end]   # 字符串切片操作

        # 通过PID关闭被占用的端口
        cmd_kill = 'taskkill -f -pid %s' %pid
        print(cmd_kill)
        os.popen(cmd_kill)

    else:
        print('Port %s is available!' %port)


if __name__ == '__main__':
    host = '127.0.0.1'
    port = 4725
    # check_port(host,port)
    release_port(port)