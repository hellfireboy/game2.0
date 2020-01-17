# 水仙花数

a = int(input('输入一个3位数：'))

while a <= 100 or a > 1000:
    a = int(input('请重新输入，一个三位数：'))

x = str(a)[0]
y = str(a)[1]
z = str(a)[2]

if int(x) ** 3 + int(y) ** 3 + int(z) ** 3 == a:
    print('%d是一个水仙花数！' % a)
else:
    print('%d不是一个水仙花数~~~~~~' % a)

print('打印所有水仙花数：',end="\t")
for i in range(100, 1001):
    x = str(i)[0]
    y = str(i)[1]
    z = str(i)[2]
    if int(x) ** 3 + int(y) ** 3 + int(z) ** 3 == i:
        print(i, end="\t")

# 教程
# for num in range(100, 1000):
#     low = num % 10
#     mid = num // 10 % 10
#     high = num // 100
#     if num == low ** 3 + mid ** 3 + high ** 3:
#         print(num)