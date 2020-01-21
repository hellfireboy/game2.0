# import sys
#
# f = [x for x in range(1, 11)]
# print(f)
#
# f = [x + y for x in "ABCDEF" for y in "123"]
# print(f)
#
# f = [x ** 2 for x in range(1, 10000)]
# print(f.__sizeof__())
# print(sys.getsizeof(f))
# print(f)
#
# f = (x ** 2 for x in range(1, 10000))
# print(sys.getsizeof(f))
# print(f)
#
# for i in f:
#     print(i ,end="\t")
#


def feibonaqi(n):
    # a = 0
    # b = 1
    # for i in range(n):
    #     # a = b
    #     # b = a + b
    #     a, b = b, a + b
    #     yield a

    a = 0
    b = 1
    temp = 0
    for i in range(n):
        temp = a + b
        yield a
        a = b
        b = temp
    # return b
    # global c
    # c = 2


#
#
# c = 1
# print(feibonaqi(22))
# print(c)


def main():
    # for i in feibonaqi(x):
    # for i in feibonaqi(20):
    #     print(i)
    for i, j in enumerate(feibonaqi(x)):
        print(f"{i + 1}\t{j}")


if __name__ == '__main__':
    x = int(input("输入输出个数："))
# print("1\t1")
# print("2\t1")
main()


def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        yield a


def main():
    for val in fib(20):
        print(val)


if __name__ == '__main__':
    main()
