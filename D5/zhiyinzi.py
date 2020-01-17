# 输入任意一个大于2的数，对该数进行分解质因数。
from math import sqrt

from math import sqrt

x = int(input('输入一个大于2的数：'))
for i in range(2, x + 1):
    flag = True
    for j in range(2, i + 1):
        if i % j == 0 and i != j:
            print(i, end='\t')
            x /= j
            flag = False
            break
        if j == i and flag == True:
            print(i, end='\t')

# flag = False
# x = int(input("输入一个大于2的数，下面会显示它的质因数:"))
# print('[', end=' ')
# for i in range(2, x):
#     if x % i == 0:
#         print(i, end=" ")
#         flag = True
#     elif i == (x - 1) and flag == False:
#         print('%d是个素数，没有质因子' % x, end=' ')
# print(']')
#
# flag = False
# x = int(input("输入一个大于2的数，下面会显示它的质因数:"))
# print('[', end=' ')
# for i in range(2, x):
#     if x % i == 0:
#         x /= i
#         print(i, end=" ")
#         flag = True
#     elif i == (x - 1) and flag == False:
#         print('%d是个素数，没有质因子' % x, end=' ')
# print(']')
#
