"""Python 列表 list的独立运行示例。"""


def example_1() -> None:
    """从 [1, 2, 1] 删除首个 1。"""
    items = [1, 2, 1]
    items.remove(1)
    print(repr(items))


if __name__ == "__main__":
    example_1()
