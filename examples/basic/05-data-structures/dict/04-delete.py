"""Python 字典 dict的独立运行示例。"""


def example_1() -> None:
    """用 pop 取出 a，返回旧值和剩余字典。"""
    record = {"a": 1, "b": 2}
    removed = record.pop("a")
    print(repr((removed, record)))


if __name__ == "__main__":
    example_1()
