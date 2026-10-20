"""Day 3 综合练习：猜数字游戏（周三晚）。

运行方式：
    cd ~/Projects/learn-ai/week01
    source .venv/bin/activate
    python day03-2026-10-21/guess.py

目标：补全 TODO，得到一个猜错不崩溃、输错有提示的游戏。
今晚用到的知识点：函数、while 循环、try/except、random 模块、f-string。
"""

import random


def play() -> None:
    """猜数字：程序随机生成 1-100 的整数，玩家反复输入，猜中后显示次数。"""
    # TODO 1: 用 random.randint(1, 100) 生成答案，存到 answer
    answer = ...

    count = 0  # 已猜的次数

    while True:
        raw = input("请输入 1-100 的整数（或 q 退出）: ").strip()

        # TODO 2: 如果输入是 "q"，打印 "已退出" 并 return
        ...

        # TODO 3: 把 raw 转成整数；
        #   - 转换失败（ValueError）→ 打印 "这不是数字，请重新输入"，continue
        #   - 提示：用 try/except 包住 int(raw)
        try:
            guess = ...
        except ...:
            print("这不是数字，请重新输入")
            continue

        count += 1

        # TODO 4: 比较 guess 和 answer：
        #   大了 → 打印 "大了"（含猜的次数提示更好）
        #   小了 → 打印 "小了"
        #   相等 → 打印 "猜中了！共用了 N 次"（用 f-string），然后 break
        ...


def main() -> None:
    print("=== 猜数字游戏 ===")
    play()
    # TODO 5（进阶）：猜完问一句 "再来一局吗？(y/n)"，y 就再玩一次


if __name__ == "__main__":
    main()

# ------------------------------------------------------------------
# 提示区（卡住 10 分钟再看）
#
# 1:  answer = random.randint(1, 100)
# 3:  try: guess = int(raw)
#     except ValueError: ...        # 注意是 ValueError 不是 Exception
# 4:  if guess > answer: ...
#     elif guess < answer: ...
#     else: print(f"猜中了！共用了 {count} 次"); break
# ------------------------------------------------------------------
