# Python 元组 tuple

**适用 Python 版本** Python 3.11+

**难度等级** 基础

## 学习目标

- 解释元组 tuple的基本概念与运行行为。
- 运行配套示例并独立完成本篇练习。

## 前置知识

能在终端运行 Python 脚本。建议先学习[列表 list](05-list.md)。

## 基本概念

元组是有固定成员引用的有序序列，适合坐标、记录或多值返回。

## 语法讲解

`(1, 2)` 创建两项元组；单元素写 `(1,)`，`(1)` 只是括号表达式。`tuple(iterable)` 从可迭代对象创建。支持索引、切片和遍历。`x, y = point` 逐项解包，`first, *middle, last = values` 将剩余的中间项放到列表。

## 代码示例

先运行这段代码。它演示如何创建仅包含 5 的元组。

```python
print(repr((5,)))
```

## 运行结果

```text
(5,)
```

这里使用 `repr()` 展示结果，便于识别字符串的引号和容器的边界。

## 常用方法

`count()` 统计值，`index()` 返回首个匹配项的位置并在不存在时抛 `ValueError`。列表适合动态修改序列，元组适合固定结构。

## 工作原理

元组不可增删或替换槽位里的引用，槽位指向的列表仍可修改。元组元素均可哈希时，元组才可用作字典键。

## 实际应用

用 `(行, 列)` 表示棋盘坐标。需要反复添加棋子时，用列表保存多组元组。 从单个输入开始运行，再改变输入检查结果是否符合预期。

## 常见问题

函数返回 `return x, y` 是返回两个对象吗？它返回包含两个引用的一个元组，调用方可以解包。

## 易错点

未使用星号时，解包目标数须与元素数相等。带列表的元组不能用作字典键。

## 练习题

完成[本篇十道练习](questions/06-tuple.md)，再查看[参考答案](solutions/06-tuple.md)。

## 本章总结

元组是有固定成员引用的有序序列，适合坐标、记录或多值返回。 复习时，试着先口头预测示例结果，再运行代码核对。

## 参考资料

[Python 3.11 官方文档](https://docs.python.org/zh-cn/3.11/tutorial/datastructures.html)

## 配套资源

- [01-create.py](https://github.com/zyy-stu/python-learning-roadmap/blob/main/examples/basic/05-data-structures/tuple/01-create.py)。运行命令为 `python examples/basic/05-data-structures/tuple/01-create.py`。
- [02-access.py](https://github.com/zyy-stu/python-learning-roadmap/blob/main/examples/basic/05-data-structures/tuple/02-access.py)。运行命令为 `python examples/basic/05-data-structures/tuple/02-access.py`。
- [03-unpacking.py](https://github.com/zyy-stu/python-learning-roadmap/blob/main/examples/basic/05-data-structures/tuple/03-unpacking.py)。运行命令为 `python examples/basic/05-data-structures/tuple/03-unpacking.py`。
- [返回章节导航](index.md)

## 下一篇教程

上一篇 [列表 list](05-list.md)

下一篇 [集合 set](07-set.md)
