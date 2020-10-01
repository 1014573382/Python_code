from flask import session

from functools import wraps
"""从“function”（标准库的一部分）导入“wraps”函数（它本身是一个修饰符）"""

def check_logged_in(func):
      @wraps(func)   #用"wraps'修饰符修饰"wrapper" 函数（一定要传入“func”作为参数）
      def wrapper(*args, **kwargs):
            if 'logged_in' in session:
                  return func(*args, **kwargs)
            return 'You are NOT logged in.'
      return wrapper
