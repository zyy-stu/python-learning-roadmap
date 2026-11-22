"""Python 字典 dict的独立运行示例。"""


def example_1() -> None:
    """用字典推导式建立 1 到 3 的平方映射。"""
    print(repr({value: value**2 for value in range(1, 4)}))


if __name__ == "__main__":
    example_1()
