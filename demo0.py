import os
from openai import OpenAI
from dotenv import load_dotenv

# 1. 自动去 .env 保险箱里读取密码
load_dotenv()

# 2. 初始化 DeepSeek 客户端
client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)

print("正在呼叫大模型，请稍等...")

# 3. 发送问题
response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "你是一个资深的AI开发导师。"},
        {"role": "user", "content": "你好，请用一句话鼓励一下正在学习大模型应用开发的我。"}
    ]
)

# 4. 打印大模型的回答
print("\n大模型回复：")
print(response.choices[0].message.content)