"""用字典累计词频。"""


def count_words(text: str) -> dict[str, int]:
    """按空白切分文本并返回每个词的出现次数。"""
    counts: dict[str, int] = {}
    for word in text.split():
        counts[word] = counts.get(word, 0) + 1
    return counts


if __name__ == "__main__":
    print(repr(count_words("web ai web")))
