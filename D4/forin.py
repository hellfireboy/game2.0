# 1~100的各种求和

sum = int(0)
for a in range(100):  # a 初始值是 0
    sum += (a + 1)

print("1~100的和为%d" % sum)

sum = int(0)
for a in range(0, 101, 2):
    sum += a

print("1~100的偶数和为%d" % sum)
