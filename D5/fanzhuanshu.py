# 翻转数

x = int(input("请输入一串数字，将会输出翻转数字："))
l = int(len(str(x)))
y=0

for i in range(l - 1, -1, -1):
    print(str(x)[i], end="")
    y=int(str(x)[i])+y*10

print("")
print(y)


# """
# 正整数的反转
#
# Version: 0.1
# Author: 骆昊
# """
#
# num = int(input('num = '))
# reversed_num = 0
# while num > 0:
#     reversed_num = reversed_num * 10 + num % 10
#     num //= 10
# print(reversed_num)