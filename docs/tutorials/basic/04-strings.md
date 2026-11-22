# Python 字符串 str

**适用 Python 版本** Python 3.11+

**难度等级** 基础

## 学习目标

- 解释字符串 str的基本概念与运行行为。
- 运行配套示例并独立完成本篇练习。

## 前置知识

能在终端运行 Python 脚本。建议先学习[数字类型](03-numbers.md)。

## 基本概念

字符串是由 Unicode 码位组成的不可变序列。文本和经过编码的字节序列是两种类型。

## 语法讲解

单引号和双引号都能定义字符串，三引号可跨行。`\n` 是换行，`r'\n'` 保留反斜杠。`text[0]` 读取首字符，`text[-1]` 读取末字符，`text[start:stop:step]` 不含停止位置。使用 `f'{price:.2f}'` 或 `'{:.2f}'.format(price)` 格式化。

## 代码示例

先运行这段代码。它演示如何从 'Python' 取首尾字符。

```python
print(repr(('Python'[0], 'Python'[-1])))
```

## 运行结果

```text
('P', 'n')
```

这里使用 `repr()` 展示结果，便于识别字符串的引号和容器的边界。

## 常用方法

`upper()`、`lower()` 转换大小写；`strip()` 清理边缘，`replace()` 替换，`find()` 定位，`count()` 统计非重叠匹配，`split()` 与 `join()` 拆分合并，`startswith()` 与 `endswith()` 判断边界。

## 工作原理

切片与文本变换返回结果，不修改原字符串。Unicode 定义字符码位，UTF-8 把码位转换成字节。`encode('utf-8')` 与 `decode('utf-8')` 分别完成两个方向的转换。用户看到的一个字形有时由多个码位组成。

## 实际应用

接收逗号连接的标签，用 `split()` 拆分，逐项去空白和统一大小写，再用 `join()` 输出报告。 从单个输入开始运行，再改变输入检查结果是否符合预期。

## 常见问题

`find()` 找不到返回 -1；如果只需判断是否包含，用 `in`。

## 易错点

不能给索引赋值。`strip('ab')` 清除两端属于指定字符集合的字符；它不会精确移除前缀 `ab`。原始字符串结尾不能只有奇数个反斜杠。

## 练习题

完成[本篇十道练习](questions/04-strings.md)，再查看[参考答案](solutions/04-strings.md)。

## 本章总结

字符串是由 Unicode 码位组成的不可变序列。文本和经过编码的字节序列是两种类型。 复习时，试着先口头预测示例结果，再运行代码核对。

## 参考资料

[Python 3.11 官方文档](https://docs.python.org/zh-cn/3.11/howto/unicode.html)

## 配套资源

- [strings.py](https://github.com/zyy-stu/python-learning-roadmap/blob/main/examples/basic/02-basic-syntax/strings.py)。运行命令为 `python examples/basic/02-basic-syntax/strings.py`。
- [返回章节导航](index.md)

## 下一篇教程

上一篇 [数字类型](03-numbers.md)

下一篇 [列表 list](05-list.md)
