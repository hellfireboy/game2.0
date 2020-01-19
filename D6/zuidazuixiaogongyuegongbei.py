# 输入两个数，求最大公约数和最小公倍数

def zdgys(a, b):
    # zdgys = 0
    for i in range(1, a + 1):
        if a % i == 0 and b % i == 0:
            zdgys = i
    return zdgys


x = int(input("输入第一个数："))
y = int(input("输入第二个数："))

if x > y:
    x, y = y, x

print("最大公约数是：%d，最小公倍数是：%d" % (zdgys(x, y), (x * y) / zdgys(x, y)))
