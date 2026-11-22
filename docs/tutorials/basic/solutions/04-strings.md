# Python 字符串 str参考答案

每段 Python 代码可独立运行。

## 基础题

### 第 1 题

```python
print(repr(('Python'[0], 'Python'[-1])))
```

```text
('P', 'n')
```

### 第 2 题

```python
print(repr('abcdef'[1:4]))
```

```text
'bcd'
```

### 第 3 题

```python
print(repr('  Hi  '.strip().lower()))
```

```text
'hi'
```

### 第 4 题

```python
print(repr('banana'.count('an')))
```

```text
2
```

### 第 5 题

```python
print(repr('/'.join('a,b,c'.split(','))))
```

```text
'a/b/c'
```

## 进阶题

### 第 6 题

```python
name = 'report.csv'
print(repr((name.endswith('.csv'), name.startswith('report'))))
```

```text
(True, True)
```

### 第 7 题

```python
print(repr(len('中'.encode('utf-8'))))
```

```text
3
```

### 第 8 题

```python
price = 3.5
print(repr(f'{price:.2f}'))
```

```text
'3.50'
```

## 综合题

### 第 9 题

先根据题意组织输入，再计算结果。任务是将 ' Python, WEB , ,AI ' 整理为小写标签并以逗号输出，跳过空项。

```python
source = ' Python, WEB , ,AI '
labels = [part.strip().lower() for part in source.split(',') if part.strip()]
print(repr(','.join(labels)))
```

```text
'python,web,ai'
```

### 第 10 题

先根据题意组织输入，再计算结果。任务是给订单号 7 补齐 4 位，生成 ORD-0007。

```python
order_id = 7
print(repr('ORD-{:04d}'.format(order_id)))
```

```text
'ORD-0007'
```

[返回练习](../questions/04-strings.md)
