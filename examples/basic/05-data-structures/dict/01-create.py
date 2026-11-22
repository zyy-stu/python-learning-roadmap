"""Python 字典 dict的独立运行示例。"""


def example_1() -> None:
    """创建 name='小林' 的字典并读取 name。"""
    record = {"name": "小林"}
    print(repr(record["name"]))


if __name__ == "__main__":
    example_1()
