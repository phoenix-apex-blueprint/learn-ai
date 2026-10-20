# Day 4（2026-10-22 周四晚 · 约 1.5–2h）

## 时间安排

| 时段 | 时长 | 内容 |
|------|------|------|
| 第一件事 | 30min | 📐 数学：3B1B「点积与对偶性」 |
| 第二件事 | 60–90min | 🐍 NumPy Quickstart 通读（只读不刷题，为周六铺路） |

## 📐 数学（30 分钟）

**教材**：
- 🇨🇳 中文：B 站「3Blue1Brown」→《线性代数的本质》P9「点积与对偶性」
- 🇬🇧 英文：https://www.3blue1brown.com/lessons/dot-products

看完做 `math-练习.md` 的 5 道题（点积符号判断、投影、夹角余弦、找正交向量），并把两个口头问题写进 notes.md：
1. 点积的两种计算视角（逐项乘加 vs 投影）分别是什么？
2. 点积为正 / 为负 / 为零，分别说明两个向量的什么关系？（这条第 5 周讲 embedding 相似度时天天要用）

## 🐍 NumPy 通读（60–90 分钟）

**教材（中英对照着看，英文为主、中文辅助）**：
- 🇬🇧 英文：NumPy 官方 Quickstart，只看前 4 节（The Basics / Indexing / Basic Operations / Universal Functions）
  https://numpy.org/doc/stable/user/quickstart.html
- 🇨🇳 中文：NumPy 中文文档对应章节 https://www.numpy.org.cn/user/quickstart.html

**读法**：打开 REPL 跟着每一节的示例代码敲一遍，不追求记住，目标是**周六做练习时知道该翻回哪一节**。遇到 `axis` 参数看不懂就先跳过，那是第二周的内容。

**顺手做一件事**：打开 `day06-2026-10-24/numpy_practice.py` 通读一遍题目（只读不做），标记出你觉得最没把握的 2 题——周六优先啃它们。

**验收**：
- [ ] Quickstart 前 4 节的示例都在 REPL 敲过
- [ ] `math-练习.md` 5 题完成
- [ ] numpy 练习已通读并标记 2 道没把握的题
- [ ] notes.md 写了点积两个问题的回答
- [ ] 已 commit
