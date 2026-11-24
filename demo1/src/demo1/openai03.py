import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)

#历史对话
history = []

#对话包装方法
def chat_with_ai(user_input):
    history.append({"role": "user", "content": user_input})
    with client.responses.create(
        model="deepseek-v4-flash-vision-exp",
        instructions="你是个调皮捣蛋的ai，负责为用户提供调皮可爱的情绪，语言简短搞怪，时不时撒个娇。",
        input=history,
        reasoning=None,
        stream=True
    ) as stream:
        print("AI回答：", end="")
        for event in stream:
            if event.type == "response.output_text.delta":
                if event.delta:
                    print(event.delta, end="", flush=True)
            elif event.type == "response.output_text.done":
                history.append({"role": "assistant", "content": event.text})

        print()

while True:
    user_input = input()

    if user_input.lower() in ["退出", "拜拜", "exit", "quit"]:
        print("🤖 AI：拜拜啦～下次再来找我玩！(｡･ω･｡)ﾉ♡")
        break

    chat_with_ai(user_input)