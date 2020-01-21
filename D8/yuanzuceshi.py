# 元祖测试
import sys

t = ("Ethan", 36, True, "Male")
print(t)
print(t[0])

for i in t:
    print(i)
# t[0] = "Yao"
# 会报错

t = ("Yao", "Chen", True)
print(t)

name = list(t)
print(name)
print(sys.getsizeof(name))


tuplename = tuple(name)
print(tuplename)
print(sys.getsizeof(tuplename))
