# Day 7（2026-10-25 周日 · 2.5–3h，本周收官）

> **今日产出**：一个能多轮对话、显示 token 用量的命令行聊天机器人
> 这是本周里程碑——你从「学 AI」到「做 AI」的分界线。

## 时间安排

| 时段 | 时长 | 内容 |
|------|------|------|
| 第一件事 | 30min | 📐 数学：本周自测 5 题 |
| Block 1 | 2h | 🤖 完成聊天机器人 |
| Block 2 | 30min | 📝 周复盘 + 布置下周 |

## 📐 数学自测（30 分钟）

让 Claude 出题（直接说「出本周数学自测 5 题」），范围：向量加法/数乘、模长、点积、余弦相似度、矩阵×向量。闭卷做，答错的写进下周复习清单。

## 🤖 Block 1：完成聊天机器人（2h）

补全 `chatbot_starter.py`（本目录）的 6 个 TODO：

1. API Key 从环境变量读取（`os.environ`）
2. 追加 user 消息进 `messages`
3. 调用 `client.chat.completions.create(...)`
4. 取出回复文本
5. 把 assistant 回复追加回 `messages`（**故意注释掉一次，观察模型「失忆」**——这是理解 LLM 无状态本质的关键实验）
6. 打印每轮 token 用量

**进阶挑战（时间够再做）**：
- 流式输出（`stream=True`，让回复一个字一个字蹦出来）
- 启动时输入人设（如「鲁迅」「猫娘」）填进 system 消息

**教材**：
- 🇨🇳 中文：火山方舟文档（同昨天）
- 🇬🇧 英文：OpenAI Streaming 指南 https://platform.openai.com/docs/guides/streaming

## 📝 Block 2：周复盘（30 分钟）

1. 写 `notes.md`：
   - 本周最大收获（1 条）
   - 最卡的地方（1 条）
   - 聊天机器人有没有做「失忆实验」？结论是什么？
2. `git add -A && git commit`，push 到 GitHub
3. 在 Claude Code 里说「**生成下周（Week 2）的学习计划**」——我会基于本周完成度来排

## ✅ 本周里程碑检查（对照 ../../PLAN.md 第 1 周）

- [ ] uv + venv + git 环境可用
- [ ] numpy 5 题跑通（cosine_similarity 函数第 5 周复用）
- [ ] 聊天机器人能多轮对话 + token 统计
- [ ] 数学：向量/点积/余弦相似度/矩阵乘法 手算能力建立
- [ ] 全部 commit + push
