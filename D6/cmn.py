# 排列组合C(8,4)
# c(N,M) = M!/(N!(M-N)!)

x = int(input("输入一共几个数："))
y = int(input("抽出几个："))

while x <= y:
    x = int(input("重新输入一共几个数："))
    y = int(input("抽出几个，这个数要小于" + str(x)) + ":")

z = x - y

x1 = 1
for i in range(1, x + 1):
    x1 *= i

y1 = 1
for i in range(1, y + 1):
    y1 *= i

z1 = 1
for i in range(1, z + 1):
    z1 *= i

c = x1 / y1 / z1
print(int(c))
#
# m = int(input('m = '))
# n = int(input('n = '))
# fm = 1
# for num in range(1, m + 1):
#     fm *= num
# fn = 1
# for num in range(1, n + 1):
#     fn *= num
# fmn = 1
# for num in range(1, m - n + 1):
#     fmn *= num
# print(fm // fn // fmn, fm, fn, fmn)
