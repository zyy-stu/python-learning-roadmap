# Python 集合 set

**适用 Python 版本** Python 3.11+

**难度等级** 基础

## 学习目标

- 解释集合 set的基本概念与运行行为。
- 运行配套示例并独立完成本篇练习。

## 前置知识

能在终端运行 Python 脚本。建议先学习[元组 tuple](06-tuple.md)。

## 基本概念

集合保存互不重复的可哈希元素。集合没有可依赖的遍历顺序，适合去重、成员判断和比较两个群体。

## 语法讲解

`{1, 2}` 或 `set(iterable)` 创建集合，空集合用 `set()`，`{}` 是字典。`a | b` 并集，`a & b` 交集，`a - b` 差集，`a ^ b` 对称差集。`a <= b` 判断子集，`a >= b` 判断超集，可用 `isdisjoint()` 判断无交集。

## 代码示例

先运行这段代码。它演示如何把 [1, 1, 2] 转为升序去重列表。

```python
print(repr(sorted(set([1, 1, 2]))))
```

## 运行结果

```text
[1, 2]
```

这里使用 `repr()` 展示结果，便于识别字符串的引号和容器的边界。

## 常用方法

`add()` 添加单项，`update()` 合并多个元素，`remove()` 在缺项时抛 `KeyError`，`discard()` 遇到缺项直接结束，`clear()` 清空集合。

## 工作原理

哈希用于定位候选槽位，碰撞时通过比较继续辨别。相等对象必须具有相同哈希。数字、字符串、多数由可哈希成员组成的元组可作为元素，列表和普通集合不可。`frozenset` 不可变且可哈希。

## 实际应用

比较已报名与已签到的学员编号。差集给出未签到学员，用 `sorted()` 输出稳定顺序。 从单个输入开始运行，再改变输入检查结果是否符合预期。

## 常见问题

`pop()` 会删除第一项吗？集合没有第一项的顺序语义。它移除任意一项，空集合会抛 `KeyError`。

## 易错点

使用 `set('12')` 会得到两个字符。使用 `set([1, True])` 得到一项，因为 `1 == True`。需要保留出现顺序可用 `list(dict.fromkeys(items))`。

## 练习题

完成[本篇十道练习](questions/07-set.md)，再查看[参考答案](solutions/07-set.md)。

## 本章总结

集合保存互不重复的可哈希元素。集合没有可依赖的遍历顺序，适合去重、成员判断和比较两个群体。 复习时，试着先口头预测示例结果，再运行代码核对。

## 参考资料

[Python 3.11 官方文档](https://docs.python.org/zh-cn/3.11/library/stdtypes.html#set-types-set-frozenset)

## 配套资源

- [01-create.py](https://github.com/zyy-stu/python-learning-roadmap/blob/main/examples/basic/05-data-structures/set/01-create.py)。运行命令为 `python examples/basic/05-data-structures/set/01-create.py`。
- [02-operations.py](https://github.com/zyy-stu/python-learning-roadmap/blob/main/examples/basic/05-data-structures/set/02-operations.py)。运行命令为 `python examples/basic/05-data-structures/set/02-operations.py`。
- [03-deduplication.py](https://github.com/zyy-stu/python-learning-roadmap/blob/main/examples/basic/05-data-structures/set/03-deduplication.py)。运行命令为 `python examples/basic/05-data-structures/set/03-deduplication.py`。
- [返回章节导航](index.md)

## 下一篇教程

上一篇 [元组 tuple](06-tuple.md)

下一篇 [字典 dict](08-dict.md)
