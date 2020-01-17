# 输出100以内所有的素数
from math import sqrt

for i in range(2, 100):
    flag = True
    for j in range(2, int(sqrt(i))+2):
        if i % j == 0 and i != j:
            flag = False
            break
        if j == int(sqrt(i))+1 and flag == True:
            print(i, end='\t')
