# Python 列表 list参考答案

每段 Python 代码可独立运行。

## 基础题

### 第 1 题

```python
print(repr(list(range(4))))
```

```text
[0, 1, 2, 3]
```

### 第 2 题

```python
print(repr([4, 8, 12][-1]))
```

```text
12
```

### 第 3 题

```python
items = [1, 2]
items.append(3)
print(repr(items))
```

```text
[1, 2, 3]
```

### 第 4 题

```python
items = [1, 2, 3]
items[1] = 9
print(repr(items))
```

```text
[1, 9, 3]
```

### 第 5 题

```python
items = [1, 2, 1]
items.remove(1)
print(repr(items))
```

```text
[2, 1]
```

## 进阶题

### 第 6 题

```python
items = [0, 1, 2, 3, 4]
print(repr([value * value for value in items if value % 2 == 0]))
```

```text
[0, 4, 16]
```

### 第 7 题

```python
items = [3, 1, 2]
print(repr((sorted(items, reverse=True), items)))
```

```text
([3, 2, 1], [3, 1, 2])
```

### 第 8 题

```python
from copy import deepcopy

original = [[1]]
clone = deepcopy(original)
clone[0][0] = 2
print(repr((original, clone)))
```

```text
([[1]], [[2]])
```

## 综合题

### 第 9 题

先根据题意组织输入，再计算结果。任务是成绩 [62, 91, 48, 80] 筛出及格项并降序排列，空输入返回空列表。

```python
scores = [62, 91, 48, 80]
print(repr(sorted((score for score in scores if score >= 60), reverse=True)))
```

```text
[91, 80, 62]
```

### 第 10 题

先根据题意组织输入，再计算结果。任务是创建两行三列的独立网格，将第 0 行第 1 列设为 1。

```python
grid = [[0] * 3 for _ in range(2)]
grid[0][1] = 1
print(repr(grid))
```

```text
[[0, 1, 0], [0, 0, 0]]
```

[返回练习](../questions/05-list.md)
