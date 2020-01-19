# 写一个素数函数

def sushu(a):
    issushu = True
    for i in range(2, a):
        if a % i == 0:
            issushu = False
            break
    return issushu