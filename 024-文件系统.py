# 必须引入random才能适用randint
import random

secret = random.randint(1, 10)
print(secret)
# OS:(操作系统模块）：适用此模块，不需要关心什么操作系统适用什么模块，od会选择正确的模块帮你调用
import os

print(os.getcwd())
os.system('calc')