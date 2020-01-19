# 投色子和加和
from random import randint


def shaizi(n=2):
    for i in range(n):
        a = randint(1, 6)
        print(a, end='\t')


def qiuhe(x=0, y=0, z=0):
    return x + y + z


shaizi()
print('')
shaizi(4)
print('')
print(qiuhe(3))
print(qiuhe(3, 4))
print(qiuhe(3, 4, 5))
# print(qiuhe(0, 4, 5))
