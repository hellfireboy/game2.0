# 测试yield
def f12():
    return 1
    # return 2


# for item in f12():
    # print(item)
print(f12())


def f123():
    yield 1
    yield 2
    yield 3


for item in f123():  # 1, 2, and 3, will be printed
    print(item)


def f13():
    yield 1
    while False:
        yield 2
    yield 3


for item in f13():  # 1 and 3, will be printed
    print(item)
