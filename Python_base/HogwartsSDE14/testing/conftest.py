#-*- coding:utf-8 -*-
# @Author : guonian
# @Time : 2020/10/14 22:16
from typing import List
import pytest
import yaml
from _pytest.python import Metafunc


# fixture的可选参数scope，默认是function级别的
# @pytest.fixture(scope='session')
# scope='session' 整个项目只执行一次
# scope='module' 每个模块，也就是每个.py文件 只执行一次
# 每个情况下，可整体运行testing目录查看test_login 和test_search中的执行情况

# autouse参数：令autouse=True  即@pytest.fixture(autouse=True)，则不用在具体的方法中
#      传入相应函数（ 如：def test_case3(login): ），所有用例都会自动去调用装饰器


# 方法加上pytest的装饰器，可以将此函数传入想要调用此函数得位置

# 参数化结合fixture使用：
# 情况一：传入值和数据
# 情况二：传入一个fixture方法，将数据传入到fixture方法中，
#         fixture方法使用request参数来接收这组数据，在方法体里面使用
#             '''request.param'''来使用这个数据

@pytest.fixture(params=['user1', 'user2', 'user3'])
def login(request):
    print("登录方法")
    print(request.param)
    # yield 激活fixture teardown方法
    yield ['username', 'password'] # 相当于return
    print("teardown")

#  对收集上来的测试用例实现定制化功能
def pytest_collection_modifyitems(
    session: "Session", config: "Config", items: List["Item"]
) -> None:
    print(items)
    print(len(items))
    # 倒序执行 items里面的测试用例
    items.reverse()
    # 含有中文的测试用例名称，改写编码格式（nodeid是用例名称）：
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')
        # 如果测试用例名带有add,则给测试用例加上add标签
        # 在命令行用 ‘pytest test_calculator.py -m add’ 执行测试用例，将只执行带有add标签的测试用例
        if 'add' in item.nodeid:
            item.add_marker(pytest.mark.add)

        # 如果测试用例名带有sub,则给测试用例加上sub标签
        if 'sub' in item.nodeid:
            item.add_marker(pytest.mark.sub)


# hook函数：命令行去添加一个参数,运行时获取default=''设置的值
# parser: 用户命令行参数与ini文件值的解析器
def pytest_addoption(parser):
    mygroup = parser.getgroup("hogwarts")     #group 将下面所有的 option都展示在这个group下。
    mygroup.addoption("--env",    #注册一个命令行选项
                      default='test',
                      dest='env',
                      help='set your run env'
                      )
    mygroup.addoption("--env1",#注册一个命令行选项
                      default='test',
                      dest='env1',
                      help='set your run env'
                      )

# 处理命令行传来的参数，设置成fixture,将test环境和dev环境或者其他环境分别处理，获取想要的不同环境下的测试数据
@pytest.fixture(scope='session')
def cmdoption(request):
    myenv = request.config.getoption("--env", default='test')
    # 命令行运行传入--env=test，即： pytest test_env.py --env test，则读取测试数据
    if myenv == 'test':
        datapath = 'datas/test/data.yml'

    # 命令行运行传入--env=dev，即： pytest test_env.py --env dev，则读取dev数据
    if myenv == 'dev':
        datapath = 'datas/dev/data.yml'

    with open(datapath)as f:
        datas = yaml.safe_load(f)

    return  myenv,datas

# 可以实现自定义动态参数化方案或者扩展，对参数化进行简化，test_param.py文件中是引用
def pytest_generate_tests(metafunc: "Metafunc") -> None:
    if 'param' in metafunc.fixturenames:
        metafunc.parametrize("param",
                             metafunc.module.mydatas,
                             ids=metafunc.module.myids,
                             scope='function')