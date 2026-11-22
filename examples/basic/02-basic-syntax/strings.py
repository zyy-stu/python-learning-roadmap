"""Python 字符串 str的独立运行示例。"""


def example_1() -> None:
    """从 'Python' 取首尾字符。"""
    print(repr(("Python"[0], "Python"[-1])))


def example_2() -> None:
    """提取 'abcdef' 的第 2 至第 4 个字符。"""
    print(repr("abcdef"[1:4]))


def example_3() -> None:
    """把 '  Hi  ' 去空格并转小写。"""
    print(repr("  Hi  ".strip().lower()))


def example_4() -> None:
    """检查 'report.csv' 后缀与 'report' 前缀。"""
    name = "report.csv"
    print(repr((name.endswith(".csv"), name.startswith("report"))))


def example_5() -> None:
    """把汉字 '中' 用 UTF-8 编码并计算其字节数。"""
    print(repr(len("中".encode())))


def example_6() -> None:
    """将 3.5 格式化为保留两位小数的文本。"""
    price = 3.5
    print(repr(f"{price:.2f}"))


if __name__ == "__main__":
    example_1()
    example_2()
    example_3()
    example_4()
    example_5()
    example_6()
