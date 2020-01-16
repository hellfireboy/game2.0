import random

a = random.randint(1, 100)
b = int(input("输入一个数字，1~100，第1次:"))
count = int(1)
while True:
    if b > a:
        count = count + 1
        b = int(input("大了，Go on，第" + str(count) + "次:"))
    elif b < a:
        count = count + 1
        b = int(input("小了，Go on:第" + str(count) + "次:"))
    else:
        count = count + 1
        print("Bingo!")
        break

print("你总共猜了%d次" % count)
