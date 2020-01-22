# 验证码生成，必须含有大写小写和数字
from random import randint
from random import sample


# import re


def value1():
    return list1[0][randint(0, 9)]


def value2():
    return list1[1][randint(0, 25)]


def value3():
    return list1[2][randint(0, 25)]


def main():
    # print("a" in list1[1])
    # value1 = list1[0][randint(0, 9)]
    # value2 = list1[1][randint(0, 25)]
    # value3 = list1[2][randint(0, 25)]
    list2 = [value1(), value2(), value3()]
    print(list2)

    dict1 = {0: value1(), 1: value2(), 2: value3()}
    print(dict1)
    dict2 = dict1

    x = int(input("输入生成个数："))
    while x <= 4:
        x = int(input("必须大于等于5个数字，："))

    for i in range(3, x):
        j = randint(1, 3)
        if j == 1:
            dict2[i] = value1()
        elif j == 2:
            dict2[i] = value2()
        elif j == 3:
            dict2[i] = value3()

    print(dict2)
    # print(dict2.values())

    # for i in dict2:
    #     dict2[i]

    list2 = sample(list(dict2.values()), len(dict2))
    print(list2)

    str1 = ''.join(list2)
    print(str1)


if __name__ == '__main__':
    global list1
    list1 = ["0123456789", "abcdefghijklmnopqrstuvwxyz", "ABCDEFGHIJKLMNOPQRSTUVWXYZ"]
    # list1 = [[0-9], [a-z], [A-Z]]
    main()
