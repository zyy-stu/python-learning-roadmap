"""Python 基本数据类型的独立运行示例。"""


def example_1() -> None:
    """输出 7 的类型名称。"""
    print(repr(int.__name__))


def example_2() -> None:
    """将文本 '42' 转成整数。"""
    print(repr(int("42")))


def example_3() -> None:
    """输出 2+3j 的虚部。"""
    print(repr((2 + 3j).imag))


def example_4() -> None:
    """判断空列表的布尔值。"""
    print(repr(bool([])))


def example_5() -> None:
    """返回 None 的类型名。"""
    print(repr(type(None).__name__))


def example_6() -> None:
    """检查 True 是否是 int 的实例。"""
    print(repr(isinstance(True, int)))


if __name__ == "__main__":
    example_1()
    example_2()
    example_3()
    example_4()
    example_5()
    example_6()
