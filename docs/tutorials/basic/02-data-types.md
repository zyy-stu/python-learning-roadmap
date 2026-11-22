# Python 基本数据类型

**适用 Python 版本** Python 3.11+

**难度等级** 基础

## 学习目标

- 解释基本数据类型的基本概念与运行行为。
- 运行配套示例并独立完成本篇练习。

## 前置知识

能在终端运行 Python 脚本。建议先学习[变量](01-variables.md)。

## 基本概念

对象的类型决定支持的运算。整数、浮点数、复数、布尔值、字符串和 None 常用于表示单个值；列表、元组、集合和字典用来组织多个值。

## 语法讲解

`int` 表示整数，`float` 表示浮点数，`complex` 用 `j` 写虚部，`bool` 有 `True` 和 `False`。`str` 表示文本，`NoneType` 有唯一值 `None`。`[1]` 是列表，`(1,)` 是元组，`{1}` 是集合，`{'x': 1}` 是字典。

## 代码示例

先运行这段代码。它演示如何输出 7 的类型名称。

```python
print(repr(type(7).__name__))
```

## 运行结果

```text
'int'
```

这里使用 `repr()` 展示结果，便于识别字符串的引号和容器的边界。

## 常用方法

`int()`、`float()`、`str()`、`list()` 可按类型的规则转换。转换前明确输入格式。

## 工作原理

`type(x)` 返回实际类型，`isinstance(x, T)` 接受 T 的子类。`bool` 是 `int` 的子类。列表、集合和字典允许原地修改；数字、字符串、元组不可变。元组可引用可变成员。动态类型允许同一个变量在不同时间绑定不同类型。

## 实际应用

读取配置时，把文本端口转换为整数，再用 `None` 表示尚未提供的可选参数。 从单个输入开始运行，再改变输入检查结果是否符合预期。

## 常见问题

`None` 和空字符串一样吗？两者都可在条件中被视为假，含义和类型不同。用 `is None` 判断缺值。

## 易错点

`bool('False')` 为真，因为该字符串非空。`int('3.2')` 会抛出 `ValueError`。

## 练习题

完成[本篇十道练习](questions/02-data-types.md)，再查看[参考答案](solutions/02-data-types.md)。

## 本章总结

对象的类型决定支持的运算。整数、浮点数、复数、布尔值、字符串和 None 常用于表示单个值；列表、元组、集合和字典用来组织多个值。 复习时，试着先口头预测示例结果，再运行代码核对。

## 参考资料

[Python 3.11 官方文档](https://docs.python.org/zh-cn/3.11/library/stdtypes.html)

## 配套资源

- [data_types.py](https://github.com/zyy-stu/python-learning-roadmap/blob/main/examples/basic/02-basic-syntax/data_types.py)。运行命令为 `python examples/basic/02-basic-syntax/data_types.py`。
- [返回章节导航](index.md)

## 下一篇教程

上一篇 [变量](01-variables.md)

下一篇 [数字类型](03-numbers.md)
