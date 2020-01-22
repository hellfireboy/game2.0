# 字典测试
# import os

scores = {"Ethan": 10, "Fiona": 20, "Emanon": 30}
print(scores)
dict1 = dict(a=1, b=2, c=3)
print(dict1)
dict2 = dict(zip(["x", "y", "z"], {10, 20, 30}))
print(dict2)
dict3 = {i: i ** 2 for i in range(10)}
# dict3 = {num: num ** 2 for num in range(1, 10)}
print(dict3)

print(scores["Ethan"])
# print(scores["Yao"])

# 字典遍历的话是key
for i in scores:
    print(f"{i}:{scores[i]}")

print(scores.keys())
print(scores.values())

# os.system("clear")

scores["Yao"] = 40
print(scores)

scores.update(Wang=50, He=60)
print(scores)

if "Li" in scores:
    print(scores["Li"])

print(scores.get("Li"))
print(scores.get("Li", 70))

print(scores.popitem())
print(scores.popitem())
scores.popitem()
print(scores.popitem())
print(scores)
print(scores.pop("Ethan"))
print(scores.pop("Ethan", "没找到"))
print(scores)
print(scores.clear())
print(scores)
