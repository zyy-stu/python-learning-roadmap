# 代码质量

上一轮远程快照的 97 个 Python 文件均通过 AST 解析。六代码仓 Ruff 与格式检查均通过，命令为 `python -m ruff check .`、`python -m ruff format --check .`。

这只能证明已启用的静态规则通过。完整 SQL、安全与兼容性人工复核仍待完成。
