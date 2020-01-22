# 跑马灯
import os
import time

def main():
    list1 = "今天天气不错，挺风和日丽的。"
    while True:
        os.system("clear")
        print(list1)
        list1 = list1[1:] + list1[0]
        # os.system("clear")
        time.sleep(0.2)


if __name__ == '__main__':
    main()
