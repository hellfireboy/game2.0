# 公鸡5元一只，母鸡3元一只，小鸡1元三只，用100块钱买一百只鸡，问公鸡、母鸡、小鸡各有多少只？

# flag = False
#
# for x in range(0, 100):
#     for y in range(0, 100):
#         z = 100 - x - y
#         if x * 5 + y * 3 + z / 3 == 100:
#             a = x
#             b = y
#             c = z
#             flag = True
#
# if flag == True:
#     print("公鸡%d只，母鸡%d只，小鸡%d只。" % (a, b, c))
# else:
#     print('不可能的事')

# print("公鸡%d只，母鸡%d只，小鸡%d只。" % (x, y, z))
# else:
#     print('不可能')

flag = False
for x in range(0, 22):
    for y in range(0, 51):
        z = 100 - x - y
        if x * 5 + y * 3 + z / 3 == 100:
            print("公鸡%d只，母鸡%d只，小鸡%d只。" % (x, y, z))
            flag = True
        elif x == 21 and flag == False:
            print("不可能")
            break
# else:
#     print('不可能')
