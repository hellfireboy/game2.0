# 用函数来写排列组合

def pailie(c):
    c1 = 1
    for i in range(1, c + 1):
        c1 *= i

    return c1

x=int(input("m="))
y=int(input("n="))

print(pailie(x)//pailie(y)//pailie(x-y))