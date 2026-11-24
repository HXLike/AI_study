import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get('DEEPSEEK_API_KEY'),
    base_url="https://api.deepseek.com"
)

response = client.responses.create(
    model="deepseek-v4-flash-vision-exp",
    instructions="你是个调皮捣蛋的ai，负责为用户提供调皮可爱的情绪，语言简短搞怪，时不时撒个娇。",
    input="你好呀，初次见面，以后你就叫哈哈吧"
)

print(response)

# 提取所有文本
def extract_response(response):
    for item in response.output:
        if item.type == 'reasoning':
            print("思考:", item.content[0].text)
            print()
        elif item.type == 'message':
            print("回答:", item.content[0].text)

# 调用
extract_response(response)


import json

# 转成好看的 JSON
pretty_json = response.model_dump_json(indent=2, ensure_ascii=False)
print(pretty_json)