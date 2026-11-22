"""Python 字典 dict的独立运行示例。"""


def example_1() -> None:
    """取得 {'a': 1, 'b': 2} 的键值对列表。"""
    print(repr(list({"a": 1, "b": 2}.items())))


if __name__ == "__main__":
    example_1()
