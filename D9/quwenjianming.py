# 输入一个文本，取文件名

def main():
    filename = str(input("输入文件名："))
    pos = filename.rfind(".")
    if pos >= 0 and pos < len(filename) - 1:
        print(f"文件名是:{filename[pos + 1:]}")
    else:
        print("没找到")


def get_suffix(filename="123.421", has_dot=False):
    """
    获取文件名的后缀名

    :param filename: 文件名
    :param has_dot: 返回的后缀名是否需要带点
    :return: 文件的后缀名
    """
    pos = filename.rfind('.')
    if 0 < pos < len(filename) - 1:
        index = pos if has_dot else pos + 1
        return filename[index:]
    else:
        return ''


if __name__ == '__main__':
    print(get_suffix())
    main()
