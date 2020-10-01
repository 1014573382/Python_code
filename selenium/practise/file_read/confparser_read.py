import configparser

# 初始化,生成ConfigParser对象
config = configparser.ConfigParser()

filename = 'conf_user.ini'
config.read(filename,encoding='utf-8')

# 以列表形式获取所有节点
all_section = config.sections()
print('sections:',all_section)


# 获取指定节点的配置信息
# 以列表形式返回某个节点section对应的所有配置信息
items = config.items('connect')
print(items)


# 以列表形式返回某个节点section的option信息，即所有key值
options = config.options('user1')
print(options)


# 获取指定节点指定option的值，即value
name = config.get('user1', 'username1')
print(name, type(name))

password = config.get('user1', 'password1')
print(password, type(password))

port = config.getint('connect', 'port')
print(port, type(port))


# 检查section或option是否存在
result = config.has_section('user')
print(result)   # 结果False

result = config.has_section('user1')
print(result)   #结果True

result = config.has_option('user1','username')
print(result)   #结果False


# 如果section不存在，则添加节点section；
# 若section已存在，再执行add操作会报错configparser.DuplicateSectionError: Section XX already exists
# 添加section,并新增option的值
if not config.has_section('remark'):
    config.add_section('remark')
config.set('remark', 'info', 'ok')
config.write(open(filename, 'w'))


# 修改或添加指定节点下指定option的值
config.set('user2','password2','888888')
config.set('user2','testadd','success')  #此条为新增数据
# 对configparser对象执行的一些修改操作，必须重新写回到文件才可生效
config.write(open(filename,'w'))
# 重新查看修改后节点信息
items = config.items('user2')
print(items)


# 删除section
config.remove_section('remark')         # section存在
config.remove_section('no_section')     # section不存在

# 删除option
config.remove_option('remark1', 'test')  # option存在
config.remove_option('remark1', 'no_option')   # option不存在
config.write(open(filename, 'w'))

