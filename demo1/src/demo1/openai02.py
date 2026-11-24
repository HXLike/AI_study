import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)

with client.responses.create(
    model="deepseek-v4-flash-vision-exp",
    instructions="你是个调皮捣蛋的AI，语言简短搞怪，时不时撒个娇",
    input=[
        {
             "role": "user",
             "content": "你好呀，初次见面，以后你就叫哈哈吧"
        }
    ],
    stream=True
) as stream:
    for event in stream:
        if event.type == "response.reasoning_text.delta":
            if event.delta:
                print(event.delta, end="", flush=True)
        elif event.type == "response.reasoning_text.done":
            print("\n" + "=" * 10)
        elif event.type == "response.output_text.delta":
            if event.delta:
                print(event.delta, end="", flush=True)
        elif event.type == "response.completed":
            print("\n" + "=" * 10)
            print("输出完成")