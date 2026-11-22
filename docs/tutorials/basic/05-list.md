# Python 列表 list

**适用 Python 版本** Python 3.11+

**难度等级** 基础

## 学习目标

- 解释列表 list的基本概念与运行行为。
- 运行配套示例并独立完成本篇练习。

## 前置知识

能在终端运行 Python 脚本。建议先学习[字符串 str](04-strings.md)。

## 基本概念

列表是可变的有序序列，允许重复元素，也可以存放不同类型的对象。

## 语法讲解

使用 `[]` 或 `list(iterable)` 创建。索引从 0 开始，也可从 -1 倒数。切片 `items[a:b]` 产生新列表。`items[i] = value` 替换一项，`items[a:b] = values` 替换一段。`for item in items` 遍历，`[x * x for x in items if x > 0]` 生成筛选后的新列表。

## 代码示例

先运行这段代码。它演示如何创建从 0 到 3 的列表。

```python
print(repr(list(range(4))))
```

## 运行结果

```text
[0, 1, 2, 3]
```

这里使用 `repr()` 展示结果，便于识别字符串的引号和容器的边界。

## 常用方法

`append()` 添加单项，`extend()` 添加多项，`insert()` 指定位置，`remove()` 删除首个匹配，`pop()` 删除并返回，`del` 可删除切片。`reverse()` 原地反转，`index()` 查询位置，`count()` 计数，`copy()` 浅拷贝。

## 工作原理

列表存放对象引用。`copy()` 和切片是浅拷贝，嵌套成员仍共享，用 `copy.deepcopy()` 复制一般的嵌套数据。以 CPython 为例，末尾追加均摊 O(1)，头部插入和线性查找通常 O(n)。

## 实际应用

保存一批订单金额，使用列表推导式筛选正数，按金额从高到低生成报表。 从单个输入开始运行，再改变输入检查结果是否符合预期。

## 常见问题

`sort()` 与 `sorted()` 有什么区别？前者原地排序并返回 None，后者返回新列表。

## 易错点

`[[0] * 2] * 2` 共享内层行；构造二维列表应逐行生成。遍历时删除元素可能跳过相邻项。

## 练习题

完成[本篇十道练习](questions/05-list.md)，再查看[参考答案](solutions/05-list.md)。

## 本章总结

列表是可变的有序序列，允许重复元素，也可以存放不同类型的对象。 复习时，试着先口头预测示例结果，再运行代码核对。

## 参考资料

[Python 3.11 官方文档](https://docs.python.org/zh-cn/3.11/tutorial/datastructures.html)

## 配套资源

- [01-create.py](https://github.com/zyy-stu/python-learning-roadmap/blob/main/examples/basic/05-data-structures/list/01-create.py)。运行命令为 `python examples/basic/05-data-structures/list/01-create.py`。
- [02-access.py](https://github.com/zyy-stu/python-learning-roadmap/blob/main/examples/basic/05-data-structures/list/02-access.py)。运行命令为 `python examples/basic/05-data-structures/list/02-access.py`。
- [03-modify.py](https://github.com/zyy-stu/python-learning-roadmap/blob/main/examples/basic/05-data-structures/list/03-modify.py)。运行命令为 `python examples/basic/05-data-structures/list/03-modify.py`。
- [04-delete.py](https://github.com/zyy-stu/python-learning-roadmap/blob/main/examples/basic/05-data-structures/list/04-delete.py)。运行命令为 `python examples/basic/05-data-structures/list/04-delete.py`。
- [05-traversal.py](https://github.com/zyy-stu/python-learning-roadmap/blob/main/examples/basic/05-data-structures/list/05-traversal.py)。运行命令为 `python examples/basic/05-data-structures/list/05-traversal.py`。
- [06-comprehension.py](https://github.com/zyy-stu/python-learning-roadmap/blob/main/examples/basic/05-data-structures/list/06-comprehension.py)。运行命令为 `python examples/basic/05-data-structures/list/06-comprehension.py`。
- [返回章节导航](index.md)

## 下一篇教程

上一篇 [字符串 str](04-strings.md)

下一篇 [元组 tuple](06-tuple.md)
