# 生成斐波那契数列的前20个数
x = 1
y = 1
z = 0
print("1\t1", end='\t')
for i in range(18):
    z = x + y
    print(z, end='\t')
    x = y
    y = z
