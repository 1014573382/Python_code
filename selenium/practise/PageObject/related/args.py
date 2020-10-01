def fun_args1(args):
    print("args is %s" %args)

def fun_args2(args1, args2):
    print("args1 is %s, args2 is %s" %(args1,args2))

def fun_var_args(*args):
    for value in args:
        print("args: ", value)

#加了星号 * 的参数会以元组(tuple)的形式导入，存放所有未命名的变量参数。
def fun_var_args1(arg1, *args):
    print("fun_var_args1 的输出：")
    print(arg1)
    print(args)

#加了两个星号 ** 的参数会以字典的形式导入
def fun_var_args2(arg, **args):
    print("fun_var_args2 的输出：")
    print(arg)
    print(args)

fun_args1('guoguo')
fun_args2('gxl','ly')

# fun_var_args('1215')
# fun_var_args('1215', 'guo')
fun_var_args('1215', 'guo', 'gxl')

fun_var_args1('first','second','third')

fun_var_args2(1, a=2,b=3,c=4,)