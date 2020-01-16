x = int(input('Please input a number, len=3:'))

c = x // 100
b = x // 10 - c * 10
a = x % 10

if len(str(x)) != 3:
    print('Wrong number!')
elif (a + b + c) == 9:
    print('%d is a Great number!' % x)
else:
    print('%d just so so.' % x)
