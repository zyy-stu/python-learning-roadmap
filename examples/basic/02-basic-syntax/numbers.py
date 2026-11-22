"""Python 数字类型的独立运行示例。"""


def example_1() -> None:
    """把二进制文本 '1011' 转成整数。"""
    print(repr(int("1011", 2)))


def example_2() -> None:
    """求 -7 除以 3 的商与余数。"""
    print(repr(divmod(-7, 3)))


def example_3() -> None:
    """计算复数 3+4j 的模。"""
    print(repr(abs(3 + 4j)))


def example_4() -> None:
    """分别输出 round(2.5) 和 round(3.5)。"""
    print(repr((round(2.5), round(3.5))))


def example_5() -> None:
    """验证浮点数的近似比较。"""
    from math import isclose

    print(repr(isclose(0.1 + 0.2, 0.3)))


if __name__ == "__main__":
    example_1()
    example_2()
    example_3()
    example_4()
    example_5()
