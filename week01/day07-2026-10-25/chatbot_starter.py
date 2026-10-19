"""CLI 聊天机器人骨架（Day 1，Block 3）。

运行方式：
    cd ~/Projects/learn-ai/week01
    source .venv/bin/activate
    export ARK_API_KEY="..."   # 到这一步时让 Claude 用 arkcli 帮你配置
    python day07-2026-10-25/chatbot_starter.py

目标：补全所有 TODO，得到一个能多轮对话、显示 token 用量的聊天机器人。
"""

from openai import OpenAI

# 火山方舟的 API 兼容 OpenAI 协议，所以直接用 openai 库、换一个 base_url 即可。
# 这是你今天学到的第一个重要工程知识：**主流 LLM API 长得都一样**，
# 学会一套 = 学会所有家。
client = OpenAI(
    api_key=...,            # TODO 1: 从环境变量读，提示：import os; os.environ["ARK_API_KEY"]
    base_url="https://ark.cn-beijing.volces.com/api/v3",
)

# 聊天机器人的"记忆"就是一个消息列表：
#   - system: 设定机器人的身份（你可以在周末给它换个人设玩）
#   - 之后每轮对话把 user 和 assistant 的消息都追加进去
messages = [
    {"role": "system", "content": "你是一个友好简洁的学习助手，回答控制在三句话以内。"},
]


def chat(user_input: str) -> str:
    """发送一轮对话，返回模型的回复文本。"""
    # TODO 2: 把用户输入以 {"role": "user", ...} 的格式追加进 messages

    # TODO 3: 调用 client.chat.completions.create(
    #             model=...,        # 模型 ID，配置时由 Claude 告诉你
    #             messages=messages,
    #         )
    #         拿到 response 对象
    response = ...

    # TODO 4: 从 response 中取出回复文本（提示：response.choices[0].message.content）
    reply = ...

    # TODO 5: 把机器人的回复以 {"role": "assistant", ...} 追加进 messages
    #         （不追加的话，模型下一轮就会"失忆"——试试注释掉看效果！）

    # TODO 6: 打印本轮消耗的 token 数（提示：response.usage.prompt_tokens
    #          和 response.usage.completion_tokens）
    print(f"[tokens: 输入 ??? + 输出 ???]")

    return reply


def main():
    print("聊天机器人已启动（输入 exit 退出）")
    while True:
        user_input = input("你: ").strip()
        if user_input.lower() in ("exit", "quit", "退出"):
            print("机器人: 再见！")
            break
        if not user_input:
            continue
        reply = chat(user_input)
        print(f"机器人: {reply}")


if __name__ == "__main__":
    main()

# ------------------------------------------------------------------
# 进阶挑战（今天时间够再做）：
#
# 1. 流式输出：给 create() 加 stream=True，让回复一个字一个字蹦出来
#    （提示：网上搜 "openai python streaming"，约 10 行改动）
# 2. 多人设：启动时让用户输入一个设定（如"猫娘""鲁迅"），填进 system 消息
# 3. 对抗测试：故意问它上下文里 3 轮之前说过的东西，验证"记忆"是否生效
# ------------------------------------------------------------------
