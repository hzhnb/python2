"""
异常处理：
try:
    检测范围
except Exception[as reason]:
    出现异常（Exception)后的处理代码
finally:
    无论如何都会被执行的代码
"""
try:
    f = open('我为什么是一个文件')
    f.write('我存在了')
    sun = 1 + '1'

except OSError as reason:
    print('文件出错了'+str(reason))
except TypeError as reason:
    print('类型出错了，错误原因是：'+str(reason))
except OSError:
    print('文件出错了')
except:
    print('出错了')
#finally:
 #   f.close()
#raise():
#raise ZeroDivisionError
raise ZeroDivisionError('除数为0的异常')