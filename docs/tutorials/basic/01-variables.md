# Python 变量

**适用 Python 版本** Python 3.11+

**难度等级** 基础

## 学习目标

- 解释变量的基本概念与运行行为。
- 运行配套示例并独立完成本篇练习。

## 前置知识

能在终端运行 Python 脚本。建议先学习[基础教程总览](index.md)。

## 基本概念

执行一条赋值语句时，先求右侧表达式，再将左侧名称绑定到结果对象。再次赋值可以改变名称的指向。

## 语法讲解

用 `name = value` 赋值。名称可含字母、数字和下划线，首字符不能是数字。Python 支持 Unicode 标识符，示例采用 `snake_case`。关键字如 `class`、`for` 不能当变量名。`x = y = []` 绑定同一对象，`x, y = 1, 2` 分别绑定，`x, y = y, x` 先取得右侧的两个旧值。

## 代码示例

先运行这段代码。它演示如何交换 a=2、b=7。

```python
a, b = 2, 7
a, b = b, a
print(repr((a, b)))
```

## 运行结果

```text
(7, 2)
```

这里使用 `repr()` 展示结果，便于识别字符串的引号和容器的边界。

## 常用方法

`keyword.iskeyword()` 检查关键字，`str.isidentifier()` 检查标识符形式。

## 工作原理

`id(obj)` 在对象存活期间标识对象，释放后标识可被复用。`is` 比较身份，`==` 比较值。动态类型指类型属于对象，名称可以重新绑定到不同类型。函数赋值默认建立局部变量，读取名称按局部、外层函数、模块、内置的顺序查找。

## 实际应用

给购物单使用 `unit_price`、`quantity` 和 `total`，每个名称表明值的用途。 从单个输入开始运行，再改变输入检查结果是否符合预期。

## 常见问题

`second = first` 会复制列表吗？不会。用 `first.copy()` 才会创建新列表，嵌套元素仍共享。

## 易错点

`2name` 非法。函数内若先读后给同名局部变量赋值，可能得到 `UnboundLocalError`。

## 练习题

完成[本篇十道练习](questions/01-variables.md)，再查看[参考答案](solutions/01-variables.md)。

## 本章总结

执行一条赋值语句时，先求右侧表达式，再将左侧名称绑定到结果对象。再次赋值可以改变名称的指向。 复习时，试着先口头预测示例结果，再运行代码核对。

## 参考资料

[Python 3.11 官方文档](https://docs.python.org/zh-cn/3.11/reference/executionmodel.html)

## 配套资源

- [variables.py](https://github.com/zyy-stu/python-learning-roadmap/blob/main/examples/basic/02-basic-syntax/variables.py)。运行命令为 `python examples/basic/02-basic-syntax/variables.py`。
- [返回章节导航](index.md)

## 下一篇教程

上一篇 [基础教程总览](index.md)

下一篇 [基本数据类型](02-data-types.md)
