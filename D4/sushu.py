# 素数
#
# a = int(input("请输入一个数字："))
# for i in range(2, a):
#     if a % i == 0:
#         print("%d 不是一个素数" % a)
#         break
#     if i == (a - 1):
#         print("%d 是一个素数" % a)


from math import sqrt  # 如果import math ,调用需要math.sqrt

num = int(input('请输入一个正整数: '))
end = int(sqrt(num))  # 有意思的想法
is_prime = True  # 用布尔类型来进行最后统一的输出，不要在循环中输出
for x in range(2, end + 1):
    if num % x == 0:
        is_prime = False
        break
if is_prime and num != 1:
    print('%d是素数' % num)
else:
    print('%d不是素数' % num)
