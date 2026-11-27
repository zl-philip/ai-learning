import os
from openai import OpenAI
from dotenv import load_dotenv

# 1. 加载密钥
load_dotenv()
client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)

# 2. 准备一个聊天记录列表（大模型需要记住上下文）
messages = [
    {"role": "system", "content": "你是一个博学且幽默的AI导师。"}
]

print("=== 聊天机器人已启动（输入 '退出' 即可结束）===")

# 3. 开启无限循环
while True:
    # 获取你在黑框里输入的话
    user_input = input("\n你: ")
    
    # 如果输入“退出”，就打破循环，结束程序
    if user_input == "退出":
        print("AI: 拜拜！下次见！")
        break
        
    # 把你的话加入聊天记录
    messages.append({"role": "user", "content": user_input})
    
    # 发送给大模型
    response = client.chat.completions.create(
        temperature=0.2,
        model="deepseek-chat",
        messages=messages
    )
    
    # 获取大模型的回复
    ai_reply = response.choices[0].message.content
    
    # 打印出来，并且把AI的话也存进聊天记录
    print(f"AI: {ai_reply}")
    messages.append({"role": "assistant", "content": ai_reply})