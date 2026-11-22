# Python 元组 tuple参考答案

每段 Python 代码可独立运行。

## 基础题

### 第 1 题

```python
print(repr((5,)))
```

```text
(5,)
```

### 第 2 题

```python
print(repr(tuple([1, 2])))
```

```text
(1, 2)
```

### 第 3 题

```python
print(repr((8, 9, 10)[-1]))
```

```text
10
```

### 第 4 题

```python
print(repr((5, 6, 7, 8)[1:3]))
```

```text
(6, 7)
```

### 第 5 题

```python
print(repr((1, 2, 1).count(1)))
```

```text
2
```

## 进阶题

### 第 6 题

```python
first, *middle, last = (1, 2, 3, 4)
print(repr((first, middle, last)))
```

```text
(1, [2, 3], 4)
```

### 第 7 题

```python
record = ([2],)
record[0].append(3)
print(repr(record))
```

```text
([2, 3],)
```

### 第 8 题

```python
print(repr(('a', 'b', 'a').index('a')))
```

```text
0
```

## 综合题

### 第 9 题

先根据题意组织输入，再计算结果。任务是以坐标 (2, 4) 为键存储并查询 '已占用'。

```python
board = {(2, 4): '已占用'}
print(repr(board[(2, 4)]))
```

```text
'已占用'
```

### 第 10 题

先根据题意组织输入，再计算结果。任务是遍历两个 (商品, 数量) 元组，返回数量总和。

```python
orders = [('书', 2), ('笔', 3)]
print(repr(sum(quantity for _, quantity in orders)))
```

```text
5
```

[返回练习](../questions/06-tuple.md)
