"""numpy 练习（Day 1，Block 2）。

运行方式：
    cd ~/Projects/learn-ai/week01
    source .venv/bin/activate
    python numpy_practice.py

要求：只改 TODO 处，跑通后整个文件应无报错执行到底。
建议先自己写，卡住超过 10 分钟再看文件底部的提示区。
"""

import numpy as np

print("=" * 50)
print("练习 1：创建数组")
print("=" * 50)

# TODO 1a: 创建一个包含 0~9 共 10 个整数的一维数组，命名为 a
a = ...

# TODO 1b: 创建一个 3 行 4 列、全是 0 的二维数组，命名为 z
z = ...

# TODO 1c: 创建一个 2x2 的数组，元素为 [[1, 2], [3, 4]]，命名为 m
m = ...

print("a =", a)
print("z shape =", z.shape)   # 应输出 (3, 4)
print("m =", m)

print()
print("=" * 50)
print("练习 2：索引与切片")
print("=" * 50)

# TODO 2a: 取出 a 的第 3 个元素（下标从 0 开始）
third = ...

# TODO 2b: 取出 a 的最后 3 个元素
last3 = ...

# TODO 2c: 取出 m 的第 2 行
row2 = ...

print("third =", third)        # 应为 2
print("last3 =", last3)        # 应为 [7 8 9]
print("row2 =", row2)          # 应为 [3 4]

print()
print("=" * 50)
print("练习 3：基本运算")
print("=" * 50)

# TODO 3a: 计算 a 中所有元素的平均值
mean_a = ...

# TODO 3b: 计算 a 中所有元素的和
sum_a = ...

# TODO 3c: 创建数组 b = a * 2 + 1（逐元素运算，不需要写循环！）
b = ...

print("mean_a =", mean_a)      # 应为 4.5
print("sum_a =", sum_a)        # 应为 45
print("b =", b)

print()
print("=" * 50)
print("练习 4：点积")
print("=" * 50)

x = np.array([1, 2, 3])
y = np.array([4, -5, 6])

# TODO 4a: 计算 x 和 y 的点积（用 np.dot 或 @ 运算符）
dot_xy = ...

# TODO 4b: 用公式 验证 4a 的结果（提示：sqrt 用 np.sqrt）
norm_x = ...
norm_y = ...

print("dot_xy =", dot_xy)      # 应为 12
print("norm_x =", norm_x)      # 应为 3.7416...
print("norm_y =", norm_y)      # 应为 8.7749...

print()
print("=" * 50)
print("练习 5：写一个函数——余弦相似度")
print("=" * 50)


def cosine_similarity(v1: np.ndarray, v2: np.ndarray) -> float:
    """计算两个向量的余弦相似度。

    公式：cos(v1, v2) = (v1 · v2) / (|v1| * |v2|)
    这个函数第 5 周学 RAG/embedding 时会直接复用，认真写。
    """
    # TODO 5: 补全（两三行即可，可以用上面的 np.dot / np.linalg.norm）
    ...


# 自测：这三组结果你应该能口头解释为什么
print(cosine_similarity([1, 2, 3], [2, 4, 6]))    # 应约为 1.0（方向相同）
print(cosine_similarity([1, 0], [0, 1]))          # 应为 0.0（垂直）
print(cosine_similarity([1, 0], [-1, 0]))         # 应约为 -1.0（方向相反）

print()
print("🎉 全部跑通！记得 git add + commit。")

# ------------------------------------------------------------------
# 提示区（卡住再看）
#
# 1a: np.arange(10)
# 1b: np.zeros((3, 4))   注意是双括号——参数是一个元组
# 2b: a[-3:]
# 3a: a.mean()
# 4a: np.dot(x, y) 或 x @ y
# 5:  return float(np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2)))
# ------------------------------------------------------------------
