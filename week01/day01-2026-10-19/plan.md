# Day 1（2026-10-19 周一晚 · 约 1.5–2h）

> **今日目标**：装好开发环境 + 数学第一课
> 参考总计划：`../../PLAN.md` 阶段 1 · 第 1 周

## 时间安排

| 时段 | 时长 | 内容 |
|------|------|------|
| 第一件事 | 30min | 📐 数学：3B1B《线性代数的本质》EP1 + 练习 |
| 第二件事 | 60–90min | 🛠️ 安装 uv、创建虚拟环境、安装依赖 |

## 📐 数学（30 分钟，雷打不动的第一件事）

**教材（中英双版本，选一个看）**：
- 🇨🇳 中文：B 站官方账号「3Blue1Brown」→《线性代数的本质》P1「向量究竟是什么」（官方中文字幕）
- 🇬🇧 英文：https://www.3blue1brown.com/lessons/vectors （YouTube 官方频道）

视频约 10 分钟，剩下 20 分钟做本目录 `math-练习.md` 的第 1–3 题（第 4 题是思考题，写在枕边慢慢想，周五再回来收）。

**验收**：合上视频，能向空气解释「向量的两种理解方式」。

## 🛠️ 开发环境（60–90 分钟）

**教材**：
- 🇨🇳 中文：廖雪峰 Python 教程「安装 Python」一节 https://liaoxuefeng.com/python/（环境部分速读即可）
- 🇬🇧 英文：uv 官方文档安装页 https://docs.astral.sh/uv/getting-started/installation/（uv 暂无官方中文文档，跟着命令敲就行，就 3 条）

**步骤**：
1. 安装 uv：`curl -LsSf https://astral.sh/uv/install.sh | sh`，重开终端验证 `uv --version`
2. 创建虚拟环境并安装依赖：
   ```bash
   cd ~/Projects/learn-ai/week01
   uv venv
   source .venv/bin/activate
   uv pip install numpy openai
   ```
3. 验证：`uv run python -c "import numpy; print(numpy.__version__)"`
4. `git add -A && git commit` 记录今天的进度

**验收**：
- [ ] `uv --version` 有输出
- [ ] numpy 版本号能打印
- [ ] 今天的数学练习已做完 3 题
- [ ] 已 commit

## ⚠️ 卡住了怎么办

环境问题超过 15 分钟就直接问 Claude——周内晚的时间太宝贵，不能耗在装环境上。**但命令要自己敲**，Claude 只负责告诉你敲什么。
