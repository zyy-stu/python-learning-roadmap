"""Python 集合 set的独立运行示例。"""


def example_1() -> None:
    """把 [1, 1, 2] 转为升序去重列表。"""
    print(repr(sorted(set([1, 1, 2]))))


if __name__ == "__main__":
    example_1()
