"""Python 元组 tuple的独立运行示例。"""


def example_1() -> None:
    """取 (5, 6, 7, 8) 中间两项。"""
    print(repr((5, 6, 7, 8)[1:3]))


if __name__ == "__main__":
    example_1()
