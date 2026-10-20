# Day 6 数学练习：矩阵乘法手算（阶段 A 收官）

核心口诀（本周建立的第三块基石）：**矩阵 × 向量 = 各列向量的线性组合**。

## 第 1 题（矩阵乘向量——两种方法互相验证）

手算 $\begin{pmatrix} 2 & 1 \\ 0 & 3 \end{pmatrix} \begin{pmatrix} 1 \\ 2 \end{pmatrix}$

- 方法 A（逐行点积）：第 1 行 $(2,1)$ 与 $(1,2)$ 点积；第 2 行 $(0,3)$ 与 $(1,2)$ 点积
- 方法 B（列的线性组合）：第 1 列 $\times 1$ + 第 2 列 $\times 2$

> 你的答案（两种方法结果应一致）：

## 第 2 题（行向量 vs 列向量——形状很重要）

手算并观察结果形状的区别：

1. $\begin{pmatrix} 1 & 2 \end{pmatrix} \begin{pmatrix} 3 \\ 4 \end{pmatrix}$（结果是一个数？）
2. $\begin{pmatrix} 1 \\ 2 \end{pmatrix} \begin{pmatrix} 3 & 4 \end{pmatrix}$（结果是一张 2×2 的表？）

> 你的答案（这就是周六 numpy 练习里 shape 概念的数学基础）：

## 第 3 题（2×2 乘 2×2，稍进阶）

手算 $\begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix} \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$
（右边这个矩阵的作用是「交换两列」——先猜答案长什么样，再算）

> 你的答案：

## 第 4 题（连接本周全部内容）

口述（合上材料）：
1. 矩阵乘向量为什么是「线性组合」？
2. 点积和矩阵乘法是什么关系？（提示：矩阵乘向量的每个分量都是一次点积）

> 你的答案：

## Python 验证

```python
import numpy as np
M = np.array([[2, 1], [0, 3]])
v = np.array([1, 2])
print(M @ v)                      # 第 1 题
print(np.array([1, 2]) @ np.array([3, 4]))   # 第 2 题第 1 小题
print(np.outer([1, 2], [3, 4]))    # 第 2 题第 2 小题（outer 积）
A = np.array([[1, 2], [3, 4]])
B = np.array([[0, 1], [1, 0]])
print(A @ B)                      # 第 3 题
```
