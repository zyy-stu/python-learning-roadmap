# Python 基本数据类型参考答案

每段 Python 代码可独立运行。

## 基础题

### 第 1 题

```python
print(repr(type(7).__name__))
```

```text
'int'
```

### 第 2 题

```python
print(repr(int('42')))
```

```text
42
```

### 第 3 题

```python
print(repr((2 + 3j).imag))
```

```text
3.0
```

### 第 4 题

```python
print(repr(bool([])))
```

```text
False
```

### 第 5 题

```python
print(repr(type(None).__name__))
```

```text
'NoneType'
```

## 进阶题

### 第 6 题

```python
print(repr(isinstance(True, int)))
```

```text
True
```

### 第 7 题

```python
values = list((2, 4))
values.append(6)
print(repr(values))
```

```text
[2, 4, 6]
```

### 第 8 题

```python
print(repr(float('3.50') * 2))
```

```text
7.0
```

## 综合题

### 第 9 题

先根据题意组织输入，再计算结果。任务是解析端口 '8080' 和开关 'false'，输出 (端口整数, 开关布尔值)。

```python
port_text, enabled_text = '8080', 'false'
print(repr((int(port_text), enabled_text.lower() == 'true')))
```

```text
(8080, False)
```

### 第 10 题

先根据题意组织输入，再计算结果。任务是缺失用户昵称以访客代替，已有空字符串保留，输出两种结果。

```python
names = (None, '')
print(repr(tuple('访客' if name is None else name for name in names)))
```

```text
('访客', '')
```

[返回练习](../questions/02-data-types.md)
