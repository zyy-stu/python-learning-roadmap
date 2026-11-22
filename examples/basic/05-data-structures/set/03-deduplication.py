"""Python 集合 set的独立运行示例。"""


def example_1() -> None:
    """对 ['甲', '乙', '甲'] 去重并保留第一次出现的顺序。"""
    names = ["甲", "乙", "甲"]
    print(repr(list(dict.fromkeys(names))))


if __name__ == "__main__":
    example_1()
