# 用可变参数写函数

def qiuhe(*a):
    sum = 0
    for i in a:
        sum += i
    return sum


print(qiuhe())
print(qiuhe(1))
print(qiuhe(1, 2))
print(qiuhe(1, 2, 4, 6, 6, 3))

def foo():
    pass


def bar():
    pass


# __name__是Python中一个隐含的变量它代表了模块的名字
# 只有被Python解释器直接执行的模块的名字才是__main__
if __name__ == '__main__':
    print('call foo()')
    foo()
    print('call bar()')
    bar()