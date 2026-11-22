"""Python 字典 dict的独立运行示例。"""


def example_1() -> None:
    """在 {'a': 1} 中读取缺失的 b，默认返回 0。"""
    print(repr({"a": 1}.get("b", 0)))


if __name__ == "__main__":
    example_1()
