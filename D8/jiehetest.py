# 集合

set1 = {1, 2, 3, 7, 4, 5, 3, 2, 1, 2, 4, 6}
print(set1)
print(f"length = {len(set1)}")

set2 = set(range(1, 11))
print(set2)

set3 = set(range(10, 0, -1))
print(set3)

set4 = {"b", "c", "d", "1", "b", "a", "c", "ab", "a"}
print(set4)

# set5 = ((1, 2), (2, 3), [1, 2]) #集合里面不能有列表，会报错
# set6 = set(set5)
# print(set6)

set7 = [1, 2, 3, 4, 5, 4, 3]
set8 = set(set7)
print(set8)
#
# set9 = ([1, 2], [2, 3], [1, 2])
# set10 = set(set9)
# print(set10)

print(set2, set3)

set3 = set(range(10, 0, -1))
set3.update([91])
set3.add((91))

print(set3)

set2.update(range(11, 21))
print(set2)

set2 = {1, 2, 3, 2, 1}
set2.update("12", "13")
print(set2)

set2.update((12, 13))
print(set2)
