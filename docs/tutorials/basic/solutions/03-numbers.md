# Python 数字类型参考答案

每段 Python 代码可独立运行。

## 基础题

### 第 1 题

```python
print(repr(int('1011', 2)))
```

```text
11
```

### 第 2 题

```python
print(repr(divmod(-7, 3)))
```

```text
(-3, 2)
```

### 第 3 题

```python
print(repr(abs(3 + 4j)))
```

```text
5.0
```

### 第 4 题

```python
print(repr(pow(2, 5)))
```

```text
32
```

### 第 5 题

```python
print(repr((round(2.5), round(3.5))))
```

```text
(2, 4)
```

## 进阶题

### 第 6 题

```python
from math import isclose
print(repr(isclose(0.1 + 0.2, 0.3)))
```

```text
True
```

### 第 7 题

```python
print(repr(int(-3.9)))
```

```text
-3
```

### 第 8 题

```python
print(repr(pow(2, 10, 7)))
```

```text
2
```

## 综合题

### 第 9 题

先根据题意组织输入，再计算结果。任务是每件 2.35 元购买 3 件，用 Decimal 计算总价。

```python
from decimal import Decimal
print(repr(Decimal('2.35') * 3))
```

```text
Decimal('7.05')
```

### 第 10 题

先根据题意组织输入，再计算结果。任务是金额 8.325 按 ROUND_HALF_UP 结算到分。

```python
from decimal import ROUND_HALF_UP, Decimal
print(repr(Decimal('8.325').quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)))
```

```text
Decimal('8.33')
```

[返回练习](../questions/03-numbers.md)
