"""Python 列表 list的独立运行示例。"""


def example_1() -> None:
    """从 [0, 1, 2, 3, 4] 取偶数的平方。"""
    items = [0, 1, 2, 3, 4]
    print(repr([value * value for value in items if value % 2 == 0]))


if __name__ == "__main__":
    example_1()
