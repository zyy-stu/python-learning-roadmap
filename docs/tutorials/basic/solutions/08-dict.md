# Python 字典 dict参考答案

每段 Python 代码可独立运行。

## 基础题

### 第 1 题

```python
record = {'name': '小林'}
print(repr(record['name']))
```

```text
'小林'
```

### 第 2 题

```python
print(repr({'a': 1}.get('b', 0)))
```

```text
0
```

### 第 3 题

```python
record = {'a': 1}
record.update(a=3, b=2)
print(repr(record))
```

```text
{'a': 3, 'b': 2}
```

### 第 4 题

```python
record = {'a': 1, 'b': 2}
removed = record.pop('a')
print(repr((removed, record)))
```

```text
(1, {'b': 2})
```

### 第 5 题

```python
print(repr(list({'a': 1, 'b': 2}.items())))
```

```text
[('a', 1), ('b', 2)]
```

## 进阶题

### 第 6 题

```python
print(repr({value: value**2 for value in range(1, 4)}))
```

```text
{1: 1, 2: 4, 3: 9}
```

### 第 7 题

```python
record = {'用户': {'分数': 90}}
print(repr(record['用户']['分数']))
```

```text
90
```

### 第 8 题

```python
groups = {}
groups.setdefault('一班', []).append('甲')
print(repr(groups))
```

```text
{'一班': ['甲']}
```

## 综合题

### 第 9 题

先根据题意组织输入，再计算结果。任务是统计文本 'web ai web' 的词频，空输入应得空字典。

```python
counts = {}
for word in 'web ai web'.split():
    counts[word] = counts.get(word, 0) + 1
print(repr(counts))
```

```text
{'web': 2, 'ai': 1}
```

### 第 10 题

先根据题意组织输入，再计算结果。任务是按课程汇总学员 [('数学', '甲'), ('英语', '乙'), ('数学', '丙')]，组内保持原顺序。

```python
rows = [('数学', '甲'), ('英语', '乙'), ('数学', '丙')]
groups = {}
for course, name in rows:
    groups.setdefault(course, []).append(name)
print(repr(groups))
```

```text
{'数学': ['甲', '丙'], '英语': ['乙']}
```

[返回练习](../questions/08-dict.md)
