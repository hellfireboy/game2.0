# 9*9
for i in range(1, 10):
    for j in range(1, 10):
        x = i * j
        if i >= j:
            print("%d × %d = %d" % (j, i, x), end=" \t ")
        else:
            # i = i + 100
            print("")
            break
print("")


for i in range(1, 10):
    for j in range(1, i + 1):
        print('%d × %d = %d' % (i, j, i * j), end=' \t ')
    print("")