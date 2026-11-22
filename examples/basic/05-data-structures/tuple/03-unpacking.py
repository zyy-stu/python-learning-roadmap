"""Python 元组 tuple的独立运行示例。"""


def example_1() -> None:
    """解包 1, 2, 3, 4，返回头、中间列表、尾。"""
    first, *middle, last = (1, 2, 3, 4)
    print(repr((first, middle, last)))


if __name__ == "__main__":
    example_1()
