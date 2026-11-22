# Python 字典 dict

**适用 Python 版本** Python 3.11+

**难度等级** 基础

## 学习目标

- 解释字典 dict的基本概念与运行行为。
- 运行配套示例并独立完成本篇练习。

## 前置知识

能在终端运行 Python 脚本。建议先学习[集合 set](07-set.md)。

## 基本概念

字典将可哈希的键映射到值。键唯一，值可重复，Python 3.11+ 保留键的插入顺序。

## 语法讲解

`{'name': '小林'}`、`dict(name='小林')` 或 `dict([('name', '小林')])` 可创建字典。`d[key]` 读取，`d[key] = value` 新增或修改，`del d[key]` 删除。`for k, v in d.items()` 同时访问键和值；`{k: v for k, v in d.items() if v > 0}` 构造过滤结果。嵌套结构按层读取，例如 `records['001']['score']`。

## 代码示例

先运行这段代码。它演示如何创建 name='小林' 的字典并读取 name。

```python
record = {'name': '小林'}
print(repr(record['name']))
```

## 运行结果

```text
'小林'
```

这里使用 `repr()` 展示结果，便于识别字符串的引号和容器的边界。

## 常用方法

`update()` 合并并覆盖同名键，`pop()` 移除并返回值，`popitem()` 移除最后插入的项，空字典会报错。`keys()`、`values()`、`items()` 返回动态视图。`setdefault()` 只在缺键时插入默认值；`fromkeys()` 以共享默认值创建字典。

## 工作原理

以 CPython 为例，字典用哈希定位一组候选位置，碰撞时进一步探测并比较键。通常查询、更新和删除平均 O(1)，最坏可能退化；遍历与条目数相关。改写已有键的值保留顺序，删除后重新插入会排到末尾。

## 实际应用

用字典存储词频，将每个词的计数更新为 `counts.get(word, 0) + 1`，最后按词或次数显式排序。 从单个输入开始运行，再改变输入检查结果是否符合预期。

## 常见问题

缺键用 `get()` 还是下标？需要默认值时用 `get()`，缺键代表数据错误时用下标让 `KeyError` 暴露。

## 易错点

`dict.fromkeys(names, [])` 会让所有键共享同一列表。用 `{name: [] for name in names}` 创建独立列表。遍历视图时，避免改变键集合。

## 练习题

完成[本篇十道练习](questions/08-dict.md)，再查看[参考答案](solutions/08-dict.md)。

## 本章总结

字典将可哈希的键映射到值。键唯一，值可重复，Python 3.11+ 保留键的插入顺序。 复习时，试着先口头预测示例结果，再运行代码核对。

## 参考资料

[Python 3.11 官方文档](https://docs.python.org/zh-cn/3.11/tutorial/datastructures.html#dictionaries)

## 配套资源

- [01-create.py](https://github.com/zyy-stu/python-learning-roadmap/blob/main/examples/basic/05-data-structures/dict/01-create.py)。运行命令为 `python examples/basic/05-data-structures/dict/01-create.py`。
- [02-access.py](https://github.com/zyy-stu/python-learning-roadmap/blob/main/examples/basic/05-data-structures/dict/02-access.py)。运行命令为 `python examples/basic/05-data-structures/dict/02-access.py`。
- [03-update.py](https://github.com/zyy-stu/python-learning-roadmap/blob/main/examples/basic/05-data-structures/dict/03-update.py)。运行命令为 `python examples/basic/05-data-structures/dict/03-update.py`。
- [04-delete.py](https://github.com/zyy-stu/python-learning-roadmap/blob/main/examples/basic/05-data-structures/dict/04-delete.py)。运行命令为 `python examples/basic/05-data-structures/dict/04-delete.py`。
- [05-traversal.py](https://github.com/zyy-stu/python-learning-roadmap/blob/main/examples/basic/05-data-structures/dict/05-traversal.py)。运行命令为 `python examples/basic/05-data-structures/dict/05-traversal.py`。
- [06-comprehension.py](https://github.com/zyy-stu/python-learning-roadmap/blob/main/examples/basic/05-data-structures/dict/06-comprehension.py)。运行命令为 `python examples/basic/05-data-structures/dict/06-comprehension.py`。
- [07-word-count.py](https://github.com/zyy-stu/python-learning-roadmap/blob/main/examples/basic/05-data-structures/dict/07-word-count.py)。运行命令为 `python examples/basic/05-data-structures/dict/07-word-count.py`。
- [返回章节导航](index.md)

## 下一篇教程

上一篇 [集合 set](07-set.md)

下一篇 [流程控制章节导读](index.md)
