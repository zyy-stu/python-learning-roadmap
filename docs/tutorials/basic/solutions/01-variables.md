# Python 变量参考答案

每段 Python 代码可独立运行。

## 基础题

### 第 1 题

```python
a, b = 2, 7
a, b = b, a
print(repr((a, b)))
```

```text
(7, 2)
```

### 第 2 题

```python
x, y = 3, 4
print(repr(x + y))
```

```text
7
```

### 第 3 题

```python
quantity = 2
quantity = '2 件'
print(repr(type(quantity).__name__))
```

```text
'str'
```

### 第 4 题

```python
import keyword
print(repr(keyword.iskeyword('class')))
```

```text
True
```

### 第 5 题

```python
print(repr('item_count'.isidentifier()))
```

```text
True
```

## 进阶题

### 第 6 题

```python
original = []
other = original
other.append(8)
print(repr(original))
```

```text
[8]
```

### 第 7 题

```python
original = [4]
other = original.copy()
print(repr(id(original) == id(other)))
```

```text
False
```

### 第 8 题

```python
total = 10


def local_total():
    total = 3
    return total
print(repr((local_total(), total)))
```

```text
(3, 10)
```

## 综合题

### 第 9 题

先根据题意组织输入，再计算结果。任务是商品每件 12 元、买 3 件、运费 5 元，分开绑定三项后计算总价。

```python
unit_price, quantity, shipping = 12, 3, 5
print(repr(unit_price * quantity + shipping))
```

```text
41
```

### 第 10 题

先根据题意组织输入，再计算结果。任务是库存中苹果 5、梨 2，用不同变量记录售出苹果 3 件后的两种库存。

```python
apple, pear, sold = 5, 2, 3
apple -= sold
print(repr((apple, pear)))
```

```text
(2, 2)
```

[返回练习](../questions/01-variables.md)
