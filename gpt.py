import openai
from config import key, model, max_token,bg

openai.api_key = key
# 提问代码


def gpt(prompt):
    # 你的问题
    

    # 调用 ChatGPT 接口
    
    chat_completion = openai.ChatCompletion.create(
    model=model,
    max_tokens=max_token,
    temperature=0.7,
    messages=[
        {"role": "user", "content": bg+prompt}
    ]
    )

    response = chat_completion['choices'][0]['message']['content']
    print(response)
    return response

#print(gpt(input()))