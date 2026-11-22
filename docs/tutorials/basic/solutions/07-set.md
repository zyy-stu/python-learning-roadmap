# Python 集合 set参考答案

每段 Python 代码可独立运行。

## 基础题

### 第 1 题

```python
print(repr(sorted(set([1, 1, 2]))))
```

```text
[1, 2]
```

### 第 2 题

```python
items = set()
items.add('a')
print(repr('a' in items))
```

```text
True
```

### 第 3 题

```python
a, b = {1, 2}, {2, 3}
print(repr(sorted(a | b)))
```

```text
[1, 2, 3]
```

### 第 4 题

```python
print(repr({1, 2} & {2, 3}))
```

```text
{2}
```

### 第 5 题

```python
items = {1, 2}
items.discard(3)
print(repr(items))
```

```text
{1, 2}
```

## 进阶题

### 第 6 题

```python
print(repr({1, 2} ^ {2, 3}))
```

```text
{1, 3}
```

### 第 7 题

```python
a, b = {1}, {1, 2}
print(repr((a <= b, a.isdisjoint(b))))
```

```text
(True, False)
```

### 第 8 题

```python
rules = {frozenset({'写', '读'}): '可编辑'}
print(repr(rules[frozenset({'读', '写'})]))
```

```text
'可编辑'
```

## 综合题

### 第 9 题

先根据题意组织输入，再计算结果。任务是报名编号 {101, 102, 103} 与签到 {102, 103, 999}，返回缺席与未报名误签名单。

```python
registered, attended = {101, 102, 103}, {102, 103, 999}
print(repr((sorted(registered - attended), sorted(attended - registered))))
```

```text
([101], [999])
```

### 第 10 题

先根据题意组织输入，再计算结果。任务是对 ['甲', '乙', '甲'] 去重并保留第一次出现的顺序。

```python
names = ['甲', '乙', '甲']
print(repr(list(dict.fromkeys(names))))
```

```text
['甲', '乙']
```

[返回练习](../questions/07-set.md)
