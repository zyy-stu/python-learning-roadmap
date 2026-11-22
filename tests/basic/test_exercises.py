"""逐题运行仓库内明确登记的参考代码。"""

import re
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
EXERCISES = ROOT / "docs" / "tutorials" / "basic"
CHAPTERS = (
    "01-variables.md",
    "02-data-types.md",
    "03-numbers.md",
    "04-strings.md",
    "05-list.md",
    "06-tuple.md",
    "07-set.md",
    "08-dict.md",
)
ANSWER = re.compile(
    r"^### 第 (\d+) 题\s+.*?^```python\n(.*?)\n```\s+```text\n(.*?)\n```$", re.M | re.S
)


def load_answers(chapter):
    """读取已登记答案文档中的代码块与预期终端输出。"""
    source = (EXERCISES / "solutions" / chapter).read_text(encoding="utf-8")
    return [(int(number), code, output) for number, code, output in ANSWER.findall(source)]


@pytest.mark.parametrize("chapter", CHAPTERS)
def test_exercise_coverage(chapter):
    """核对三档题量、题目编号和答案编号。"""
    questions = (EXERCISES / "questions" / chapter).read_text(encoding="utf-8")
    levels = re.split(r"^## (?:基础题|进阶题|综合题)$", questions, flags=re.M)[1:]
    assert [len(re.findall(r"^\d+\. ", level, re.M)) for level in levels] == [5, 3, 2]
    assert [int(n) for n in re.findall(r"^(\d+)\. ", questions, re.M)] == list(range(1, 11))
    assert [number for number, _, _ in load_answers(chapter)] == list(range(1, 11))


ANSWER_CASES = [
    pytest.param(code, output, id=f"{chapter}-{number:02}")
    for chapter in CHAPTERS
    for number, code, output in load_answers(chapter)
]


@pytest.mark.parametrize(("code", "expected"), ANSWER_CASES)
def test_reference_output(code, expected, tmp_path):
    """隔离运行参考片段，检查退出状态和输出。"""
    compile(code, "<参考答案>", "exec")
    script = tmp_path / "answer.py"
    script.write_text(code, encoding="utf-8")
    result = subprocess.run(
        [sys.executable, "-I", "-X", "utf8", str(script)],
        cwd=tmp_path,
        capture_output=True,
        encoding="utf-8",
        check=True,
        timeout=10,
    )
    assert result.stdout.rstrip("\n") == expected
    assert result.stderr == ""
