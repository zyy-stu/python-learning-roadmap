"""Python 列表 list的独立运行示例。"""


def example_1() -> None:
    """成绩 [62, 91, 48, 80] 筛出及格项并降序排列，空输入返回空列表。"""
    scores = [62, 91, 48, 80]
    print(repr(sorted((score for score in scores if score >= 60), reverse=True)))


if __name__ == "__main__":
    example_1()
