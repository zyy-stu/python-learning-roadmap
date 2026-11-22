"""验证仓库维护的独立示例及核心行为。"""

import runpy
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
EXPECTED = {
    "examples/basic/02-basic-syntax/variables.py": ("(7, 2)\n7\n'str'\n[8]\n(3, 10)\n"),
    "examples/basic/02-basic-syntax/data_types.py": ("'int'\n42\n3.0\nFalse\n'NoneType'\nTrue\n"),
    "examples/basic/02-basic-syntax/numbers.py": ("11\n(-3, 2)\n5.0\n(2, 4)\nTrue\n"),
    "examples/basic/02-basic-syntax/strings.py": ("('P', 'n')\n'bcd'\n'hi'\n(True, True)\n3\n'3.50'\n"),
    "examples/basic/05-data-structures/list/01-create.py": ("[0, 1, 2, 3]\n"),
    "examples/basic/05-data-structures/list/02-access.py": ("12\n"),
    "examples/basic/05-data-structures/list/03-modify.py": ("[1, 9, 3]\n"),
    "examples/basic/05-data-structures/list/04-delete.py": ("[2, 1]\n"),
    "examples/basic/05-data-structures/list/05-traversal.py": ("[91, 80, 62]\n"),
    "examples/basic/05-data-structures/list/06-comprehension.py": ("[0, 4, 16]\n"),
    "examples/basic/05-data-structures/tuple/01-create.py": ("(5,)\n"),
    "examples/basic/05-data-structures/tuple/02-access.py": ("(6, 7)\n"),
    "examples/basic/05-data-structures/tuple/03-unpacking.py": ("(1, [2, 3], 4)\n"),
    "examples/basic/05-data-structures/set/01-create.py": ("[1, 2]\n"),
    "examples/basic/05-data-structures/set/02-operations.py": ("[1, 2, 3]\n"),
    "examples/basic/05-data-structures/set/03-deduplication.py": ("['甲', '乙']\n"),
    "examples/basic/05-data-structures/dict/01-create.py": ("'小林'\n"),
    "examples/basic/05-data-structures/dict/02-access.py": ("0\n"),
    "examples/basic/05-data-structures/dict/03-update.py": ("{'a': 3, 'b': 2}\n"),
    "examples/basic/05-data-structures/dict/04-delete.py": ("(1, {'b': 2})\n"),
    "examples/basic/05-data-structures/dict/05-traversal.py": ("[('a', 1), ('b', 2)]\n"),
    "examples/basic/05-data-structures/dict/06-comprehension.py": ("{1: 1, 2: 4, 3: 9}\n"),
    "examples/basic/05-data-structures/dict/07-word-count.py": ("{'web': 2, 'ai': 1}\n"),
}


def test_example_inventory():
    """新示例必须显式加入运行和输出检查清单。"""
    actual = {p.relative_to(ROOT).as_posix() for p in (ROOT / "examples" / "basic").rglob("*.py")}
    assert actual == set(EXPECTED)


@pytest.mark.parametrize("relative, expected", EXPECTED.items(), ids=EXPECTED)
def test_example_output(relative, expected):
    """检查语法，再运行维护者列出的无交互脚本。"""
    path = ROOT / relative
    compile(path.read_text(encoding="utf-8"), str(path), "exec")
    result = subprocess.run(
        [sys.executable, "-X", "utf8", str(path)],
        cwd=ROOT,
        capture_output=True,
        encoding="utf-8",
        check=True,
        timeout=10,
    )
    assert result.stdout == expected
    assert result.stderr == ""


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("", {}),
        ("  \t\n", {}),
        ("甲 乙\n甲", {"甲": 2, "乙": 1}),
    ],
)
def test_count_words(text, expected):
    """验证空输入、空白文本和重复词。"""
    count_words = runpy.run_path(ROOT / "examples/basic/05-data-structures/dict/07-word-count.py")[
        "count_words"
    ]
    assert count_words(text) == expected
