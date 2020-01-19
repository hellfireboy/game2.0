# 判断一个数是不是回文

def huiwen(num):
    temp = num
    total = 0
    while temp > 0:
        total = temp % 10 + total * 10
        temp = temp // 10

    return num == total


x = int(input("输入："))

if huiwen(x):
    print("YES")
else:
    print("NO")
