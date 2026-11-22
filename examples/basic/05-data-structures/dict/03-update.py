"""Python 字典 dict的独立运行示例。"""


def example_1() -> None:
    """把 {'a': 1} 中 a 改为 3 并添加 b=2。"""
    record = {"a": 1}
    record.update(a=3, b=2)
    print(repr(record))


if __name__ == "__main__":
    example_1()
