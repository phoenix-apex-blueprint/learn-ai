# Day 6（2026-10-24 周六 · 3–4h 整块，本周主战场 1/2）

> **今日产出**：① numpy 5 题全过 ② 打出你的第一发真实 LLM API 调用
> 手机放另一个房间。

## 时间安排

| 时段 | 时长 | 内容 |
|------|------|------|
| 第一件事 | 30min | 📐 数学：矩阵乘法手算 |
| Block 1 | 1.5h | 🐍 numpy 练习 5 题 |
| Block 2 | 1.5h | 🤖 第一次调 LLM API |

## 📐 数学（30 分钟）

本周数学收官——矩阵乘法手算（阶段 A 第 1–3 周主题的最后一块）：

1. 手算 $\begin{pmatrix} 2 & 1 \\ 0 & 3 \end{pmatrix} \begin{pmatrix} 1 \\ 2 \end{pmatrix}$（提示：结果 = 第 1 列 × 1 + 第 2 列 × 2，用「线性组合」视角验算）
2. 手算 $\begin{pmatrix} 1 & 2 \end{pmatrix} \begin{pmatrix} 3 \\ 4 \end{pmatrix}$ 和 $\begin{pmatrix} 1 \\ 2 \end{pmatrix} \begin{pmatrix} 3 & 4 \end{pmatrix}$，观察行向量×列向量 vs 列向量×行向量的区别
3. numpy 验证：`np.array([[2,1],[0,3]]) @ np.array([1,2])`

## 🐍 Block 1：numpy 练习（1.5h）

完成 `numpy_practice.py`（就在本目录）的 5 道题。周四已标记过没把握的题，先啃它们。卡住 10 分钟以上再看文件底部的提示区。

## 🤖 Block 2：第一次调 LLM API（1.5h）

**教材**：
- 🇨🇳 中文：火山方舟 Chat Completions 接口文档 https://www.volcengine.com/docs/82379/1330310
- 🇬🇧 英文：OpenAI API 参考（协议同源，业界通用格式）https://platform.openai.com/docs/api-reference/chat

**步骤**：
1. （10 分钟）用本机已配好的 arkcli 感受真实推理：`arkcli +chat "用一句话解释什么是大语言模型"`
2. （20 分钟）在 Claude Code 里说「**帮我配好聊天机器人的 API**」——我会用 arkcli 生成调用示例、配好 API Key
3. （60 分钟）自己从零写一个 `call_llm.py`（约 15 行，存到本目录）：发一句话给模型，打印回复和 token 用量。**不抄骨架，凭对协议的理解写**——messages、model、response.choices[0].message.content 这几个关键词在文档里找

**验收**：
- [ ] numpy 5 题全部跑通
- [ ] `call_llm.py` 能返回模型回复并显示 token 数
- [ ] 两个文件都已 commit

## ⚠️ 提醒

今天的核心是 Block 2 的**第一次真实调用**。numpy 如果超时就降到 3 题，明天周日补——API 这一步不能砍。
