# 10000以内的完美数
a = 0
for i in range(2, 10001):
    for j in range(1, i):
        if i % j == 0:
            a += j
    if a == i:
        print(a, end='\t')
    a = 0
