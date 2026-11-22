"""Python 列表 list的独立运行示例。"""


def example_1() -> None:
    """把 [1, 2, 3] 的第二项改为 9。"""
    items = [1, 2, 3]
    items[1] = 9
    print(repr(items))


if __name__ == "__main__":
    example_1()
