# 输入任意一个大于2的数，对该数进行分解质因数。
over = False
x = int(input('输入一个大于2的数：'))
while over != True:
    for i in range(2, x + 1):
        if i == x:
            over = True
            print(i)
            break

        if x % i == 0:
            print(i, end="\t")
            x = x // i
            break
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
