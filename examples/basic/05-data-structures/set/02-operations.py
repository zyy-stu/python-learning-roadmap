"""Python 集合 set的独立运行示例。"""


def example_1() -> None:
    """计算两组 {1, 2} 与 {2, 3} 的并集并排序。"""
    a, b = {1, 2}, {2, 3}
    print(repr(sorted(a | b)))


if __name__ == "__main__":
    example_1()
