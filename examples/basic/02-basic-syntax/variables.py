"""Python 变量的独立运行示例。"""


def example_1() -> None:
    """交换 a=2、b=7，输出两个新值。"""
    a, b = 2, 7
    a, b = b, a
    print(repr((a, b)))


def example_2() -> None:
    """同时绑定 x=3、y=4，输出和。"""
    x, y = 3, 4
    print(repr(x + y))


def example_3() -> None:
    """先绑定数量 2，再把数字改成字符串 '2 件'，输出类型名。"""
    quantity = 2
    quantity = "2 件"
    print(repr(type(quantity).__name__))


def example_4() -> None:
    """给同一个列表绑定两个名称，从第二个名称追加 8，输出第一个列表。"""
    original = []
    other = original
    other.append(8)
    print(repr(original))


def example_5() -> None:
    """模块变量 total=10，函数使用同名局部变量 3，返回两个值。"""
    total = 10

    def local_total():
        total = 3
        return total

    print(repr((local_total(), total)))


if __name__ == "__main__":
    example_1()
    example_2()
    example_3()
    example_4()
    example_5()
