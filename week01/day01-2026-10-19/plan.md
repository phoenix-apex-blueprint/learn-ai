# Week 1 · Day 1（2026-10-19 周日）

> **今日主题：搭好环境 + 打出你的第一发 LLM API 调用**
> 今日产出：① 可用的 Python 开发环境 ② 一个能跑的命令行聊天机器人雏形
> 参考总计划：`../PLAN.md` 阶段 1 · 第 1 周

## 时间安排（周末日，共约 6.5h）

| 时段 | 时长 | 内容 |
|------|------|------|
| 上午 1 | 30min | 📐 数学：3B1B《线性代数的本质》EP1 |
| 上午 2 | 1.5h | 🛠️ Block 1：安装 uv、建虚拟环境、git 仓库 |
| 午休 | — | — |
| 下午 1 | 1.5h | 🐍 Block 2：numpy 入门 + 练习 |
| 下午 2 | 2h | 🤖 Block 3：第一次调 LLM API，写聊天机器人 |
| 晚上 | 30min | 📝 复盘：写学习日志 + 明晚（周一）任务布置 |

---

## 📐 数学（30 分钟，今天的第一件事）

**教材**：3Blue1Brown《线性代数的本质》EP1「向量是什么」
- B 站官方账号「3Blue1Brown」搜「线性代数的本质」，或官网 https://www.3blue1brown.com/topics/linear-algebra
- 视频约 10 分钟，剩下 20 分钟做 `math-练习.md` 里的 4 道题

**验收**：合上视频，能向空气解释「向量是什么、两种理解方式」。

## 🛠️ Block 1：开发环境（1.5h）

**教材/资料**：
- uv 官方文档安装页：https://docs.astral.sh/uv/getting-started/installation/
- 廖雪峰 Python 教程（快速过「安装 Python」「第一个程序」即可）：https://liaoxuefeng.com/python/
- git 今天只需要 3 个命令：`init` / `add` / `commit`

**步骤**：
1. 安装 uv：`curl -LsSf https://astral.sh/uv/install.sh | sh`，重开终端验证 `uv --version`
2. 进入本目录，创建虚拟环境并激活：
   ```bash
   cd ~/Projects/learn-ai/week01
   uv venv            # 创建 .venv
   source .venv/bin/activate
   uv pip install numpy openai   # 一次装好今天和 Block 3 要用的库
   ```
3. 初始化 git 仓库（在 `~/Projects/learn-ai` 根目录执行 `git init`），写第一个 commit
4. 用 `uv run python -c "import numpy; print(numpy.__version__)"` 验证

**验收**：终端里能打印出 numpy 版本号，且 `git log` 里有第一条 commit。

## 🐍 Block 2：numpy 入门（1.5h）

**教材**：NumPy 官方 Quickstart（前 4 节：Basics / Indexing / Basic Operations / Universal Functions）
- 英文：https://numpy.org/doc/stable/user/quickstart.html
- 中文版可搜「NumPy 中文文档 quickstart」

**练习**：完成 `numpy_practice.py` 中的 5 道题（每题都有 TODO 标记和提示）

**验收**：5 道题全部跑通，`numpy_practice.py` 能无报错执行到底并打印结果。

## 🤖 Block 3：第一次调 LLM API（2h）

**教材**：火山方舟 API 文档（OpenAI 兼容协议）
- https://www.volcengine.com/docs/82379/1330310 （Chat Completions 接口）

**步骤**：
1. 先用本机已配好的 arkcli 感受一下真实推理：在终端运行 `arkcli +chat "你好，请做个自我介绍"`（10 分钟）
2. 读 `chatbot_starter.py` 骨架，补全 TODO，把它变成一个能多轮对话的 CLI 聊天机器人
3. API Key / 接入点配置：**到这一步时直接在 Claude Code 里说「帮我配好聊天机器人的 API」**，我会用 arkcli 帮你生成调用示例和凭证配置

**验收**：终端里能连续对话 3 轮以上，程序能打印每次消耗的 token 数。

## 📝 晚间复盘（30min）

1. 在 `notes.md` 写 3 行日志：今天学会了什么 / 卡在哪里 / 明天先做什么
2. 让 Claude 出 3 道自测题（数学、numpy、API 各一道），口头回答
3. commit 今天所有文件

## ✅ 今日完成标准（全部打勾才算过）

- [ ] 能口头解释「向量」的两种理解
- [ ] `uv` 装好，虚拟环境激活，git 有 commit
- [ ] numpy 5 道练习跑通
- [ ] 聊天机器人能多轮对话并显示 token 用量
- [ ] 学习日志已写、已 commit

## ⚠️ 卡住了怎么办

- 环境问题（装不上、路径报错）→ 超过 15 分钟就直接问 Claude，别耗时间
- 概念不懂 → 先看一遍中文资料，还不懂就问
- **今天的核心目标是 Block 3 的 API 调用，前面卡住可以降级（比如 numpy 只做 3 题），Block 3 不能砍**
