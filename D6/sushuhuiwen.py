def sushu(a):
    issushu = True
    for i in range(2, a):
        if a % i == 0:
            issushu = False
            break
    return issushu


def huiwen(num):
    temp = num
    total = 0
    while temp > 0:
        total = temp % 10 + total * 10
        temp = temp // 10

    return num == total


if __name__ == "__main__":
    x = int(input("input:"))
    if sushu(x) and huiwen(x):
        print("YES")
    else:
        print("NO")


# def foo():
#     # global a
#     nonlocal a
#     a = 200
#     print(a)  # 200
#
#
# if __name__ == '__main__':
#     # nonlocal a
#     a = 100
#     foo()
#     print(a)  # 200
