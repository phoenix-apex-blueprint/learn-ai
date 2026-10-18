# AI 学习计划（2026-10-18 制定）

> 主线递进：**Agent 开发（3 个月）→ AI Infra（6 个月）→ AI for Science（12 个月）→ 终点：LLM 算法与训练**
>
> 假设每周投入 12–15 小时。如果实际可投入时间不同，按比例伸缩各阶段，但不要砍掉里程碑项目。

## 总体逻辑

```
阶段1 (M1-M3)   Agent/LLM 应用 ── 学会"用"模型：API、RAG、工具调用、评测
阶段2 (M4-M6)   AI Infra        ── 学会"跑"模型：Transformer 内部、推理优化、部署
阶段3 (M7-M12)  AI for Science ── 学会"训"模型 + 用 AI 解决真实科学问题
终点 (M12+)     LLM 算法/训练   ── 预训练、后训练（SFT/RLHF）、分布式训练
```

每一阶段都是下一阶段的地基：Agent 开发让你理解模型的能力边界（做训练时知道优化什么）；Infra 让你理解计算本质（做训练时能搞定分布式和显存）；Science 给训练一个真实的落地场景。

---

## 阶段 1：Agent 开发 / LLM 应用（第 1–12 周）

**目标**：能独立设计、实现、评测并部署一个完整的 Agent 应用。

| 周 | 内容 | 产出 |
|----|------|------|
| 1 | Python 环境搭建（uv、venv）、numpy/pandas 基础、git；第一次调 LLM API（消息、流式输出） | 命令行聊天机器人 |
| 2 | API 深入：system prompt、结构化输出（JSON schema）、错误重试、成本与 token 计量、prompt caching | 支持 streaming + 工具计费的 CLI 助手 |
| 3 | 工具调用（function calling）：定义 schema、执行循环、并行工具调用、MCP 协议概念 | 能查天气/读文件/跑代码的迷你 Agent |
| 4 | 数学最小集 + 机器学习直觉（线性代数向量/矩阵、概率、梯度下降是什么）；同时读 Transformer 直觉材料 | 笔记 + 能向别人解释 attention |
| 5 | Embedding 与 RAG：文本切分、向量库（如 LanceDB/Chroma）、检索质量调优 | 对自己的文档做问答 |
| 6 | RAG 进阶 + 评测：hybrid search、rerank；学会写 eval（golden set、LLM-as-judge） | RAG 评测报告 |
| 7 | Agent 架构：ReAct 循环、多步规划、上下文管理、子 Agent、防止跑飞的手段 | 复杂任务 Agent（如自动整理数据出报告） |
| 8 | 可观测性与调试：tracing、日志、失败模式分析 | 给第 7 周的 Agent 加上完整追踪 |
| 9 | 上下文工程与成本优化：缓存、压缩历史、模型分级路由（小模型干粗活） | 成本下降 50% 的优化报告 |
| 10–12 | **里程碑项目**：一个面向真实用户的完整 Agent 应用（自己找需求），含 eval 套件 + 部署（可简单地用 Docker） | 上线的项目 + GitHub README |

**自测标准（第 12 周末）**：
- [ ] 能不查文档写出工具调用循环
- [ ] 能说出 RAG 答错问题的 5 种原因和对应解法
- [ ] 项目有量化 eval 指标，而不只是"感觉不错"
- [ ] 能估算自己应用每月 API 成本

**资源**：各厂商官方文档和 cookbook（Anthropic Agent 设计指南、OpenAI Cookbook）、DeepLearning.AI 短课。本机已配置火山方舟（Ark）CLI，可以直接用它调模型做练习，不必先买海外 API。

---

## 阶段 2：AI Infra（第 13–26 周）

**目标**：理解模型从权重到 token 的全过程，能部署和优化推理服务。

| 周 | 内容 | 产出 |
|----|------|------|
| 13–14 | **Transformer 从零手写**：Karpathy "Let's build GPT" + nanoGPT，逐行理解 tokenization → attention → 采样 | 手写可训练的 mini-GPT |
| 15 | PyTorch 进阶：autograd、显存管理、混合精度；GPU 架构基础（SM、显存带宽为什么是瓶颈） | 笔记 + 显存估算练习 |
| 16–17 | 推理原理：KV Cache、prefill vs decode、continuous batching、PagedAttention（读 vLLM 论文） | 能画出推理全流程图 |
| 18–19 | 实战部署：用 vLLM 或 SGLang 部署一个开源模型（Qwen/GLM 系列），压测吞吐和延迟 | benchmark 报告（tokens/s、TTFT、P99） |
| 20 | 量化：GPTQ/AWQ/FP8 原理，量化前后质量与速度对比 | 量化对比实验报告 |
| 21–22 | CUDA 入门：写一个并行向量加法/简单 attention kernel；理解 PyTorch 的 torch.compile | 自己的 kernel 代码 |
| 23–24 | 服务化：OpenAI 兼容 server、多租户路由、限流、监控（Prometheus 指标） | 一个小型"自制推理平台" |
| 25–26 | **里程碑**：给 vLLM/SGLang 等开源项目提一个 PR（修 bug、文档或小 feature）——这是 Infra 求职的硬通货 | merged/open PR |

**自测标准（第 26 周末）**：
- [ ] 手写注意力前向传播，不用查资料
- [ ] 能解释为什么 continuous batching 吞吐高
- [ ] 部署过至少一个开源模型并给出完整 benchmark
- [ ] 有一个开源 PR

**资源**：Karpathy（nanoGPT/Zero to Hero）、《How to Scale Your Model》、vLLM/SGLang 文档与源码、CS336 前几讲。

---

## 阶段 3：AI for Science + 冲刺训练（第 27–52 周）

**目标**：完成从"用模型"到"训模型"的跨越，并把训练能力用到一个科学问题上。

| 周 | 内容 | 产出 |
|----|------|------|
| 27–30 | 训练基础：Hugging Face 生态、LoRA/QLoRA 微调开源模型、数据集构建与清洗 | 微调出一个领域小模型 |
| 31–34 | 后训练：SFT → DPO → RLHF/RLVR 原理与实践（TRL 库）；reward 设计的坑 | 一个经过偏好优化的模型 + 评测 |
| 35–38 | **AI for Science 选题**（选一个：蛋白质/药物 ESM、DiffFold 系工具；材料/分子性质预测；数学定理与符号推理；天文/气象时间序列）——学领域基础 + 复现一篇论文 | 论文复现报告 |
| 39–44 | **里程碑**：用 LLM + 微调/Agent 解决一个真实科学子问题（数据集自己收集构建），写正式报告或博客 | 完整 Science 项目 |
| 45–48 | 预训练：scaling laws、数据配比、分布式训练（FSDP/DeepSpeed/Megatron 概念）；用 CS336 或开源复现项目从头训一个小 LM | 从零预训练记录（loss 曲线、消融） |
| 49–52 | **终点项目**：端到端完成一个小规模 LLM——预训练 + SFT + RLHF + 自己做推理服务部署 | 完整作品集：从权重到可用的聊天模型 |

**自测标准（第 52 周末）**：
- [ ] 独立微调过 ≥2 个模型，知道数据质量 > 一切
- [ ] 复现过一篇 Science 方向论文
- [ ] 从零预训练过一个小 LM，理解 scaling laws 和数据配比
- [ ] 作品集：Agent 应用 + 开源 PR + Science 项目 + 端到端小模型，四个成果

**资源**：CS336（Stanford，从零构建语言模型）、Hugging Face course + TRL 文档、Karpathy nanoGPT 系列、目标 Science 领域的综述与开源工具。

---

## 三条贯穿全年的原则

1. **项目 > 课程**：每个阶段以里程碑项目收官，作品集是唯一被招聘者验证的东西。
2. **用 AI 学 AI**：全程让 Claude 这类 Agent 当结对伙伴——但每个概念要求自己能脱稿复述和手写，防止"看会了"。
3. **每周一篇**：从第 4 周起每周精读/泛读一篇论文或深度博客，先中文解读，后直接读原文。做训练阶段时读论文应成为肌肉记忆。

## 当前节奏检查点

- **1 个月后（2026-11-18）**：应完成第 1–4 周，如果还在第 2 周就要压缩数学部分
- **3 个月后（2027-01-18）**：里程碑 Agent 应用上线
- **6 个月后（2027-04-18）**：开源 PR + benchmark 报告
- **12 个月后（2027-10-18）**：端到端小模型完成
