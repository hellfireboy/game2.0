s1 = '''这个可以这行
折行'''

print(s1)

s2 = '\\\n\\n'
print(s2)

s3 = '\u9a86\u660a'
print(s3)

s4 = 'abcdef1234567890'

print(s4[1])
print(s4[1:5])
print(s4[::-1])
print(s4[6:][::-1])

l = [1, "str", 23, "bie"]
print(l)
l.reverse()
print(l)

s4 = list(s4[::-1])
print(list(s4))

a = list("0123456789")
# i = 0
# for item in a[i:]:
# for item in range(len(a)):
for index1, e1 in enumerate(a):
    a.remove(e1)
    # i = i + 1
print(a)

# 这个是可行的
# a = list("0123456789")
# i = 0
# for item in a[i:]:
#     a.remove(item)
#     i = i + 1
# print(a)
#

b = list("137347374783832837848383")
j = 0
for item1 in b[j:]:
    if item1 == '3':
        b.remove(item1)
    j = j + 1
print(b)

b = list("137347374783832837848383")
j = 0
for index1, e1 in enumerate(b):
    if e1 == '3':
        b.remove(e1)
    # j = j + 1
print(b)

b = list("137347374783832837848383")
while "3" in b:
    b.remove('3')
print(b)

c = "   1341   2123 "
print(c.strip())
print(c)
print(c.isalnum())
print(c.isdigit())
print(c.strip().isdigit())
d = c.split()
print(d)

c = "   1341   2123  "
print(c.split("1"))
d = c.split()

# e = list("137347374783832837848383")
o = 1
# x=int(input("有{0}个人，输入有几个人".format(o)))
# x = int(input(f"有 {o} 个人，输入有几个人："))
p = 1
q = 2
print(f"{p}+{q}={float(p + q)}")

list1 = [1, 3, 5, 7, 100]
for index in range(len(list1)):
    # print(list1[index])
    print(index)

for elem in list1:
    print(elem)

for ii, jj in enumerate(list1):
    print(list1[ii], jj)
