import time
import os
from basereal import BaseReal
from logger import logger

def llm_response(message,nerfreal,llm_output_text):
    start = time.perf_counter()
    from openai import OpenAI
    client = OpenAI(
        api_key="fastgpt-sKtHWqHNMceIby5WXc2k03EhHoOfjfmD83ELjZ9wbOpGBx8b4YqkhC",
        base_url="http://127.0.0.1:3000/api/v1",
    )
    end = time.perf_counter()
    print(f"llm Time init: {end-start}s")
    completion = client.chat.completions.create(
        model="qwen2.5-instruct",
        messages=[{'role': 'user', 'content': message}],
        stream=True
    )
    print(message)
    print(completion)
    result=""
    first = True
    for chunk in completion:
        if len(chunk.choices)>0:
            #print(chunk.choices[0].delta.content)
            msg = chunk.choices[0].delta.content
            if msg is None:
                continue  # 跳过本次循环，继续下一个 chunk
            if first:
                end = time.perf_counter()
                print(f"llm Time to first chunk: {end-start}s")
                first = False
            lastpos=0
            #msglist = re.split('[,.!;:，。！?]',msg)
            for i, char in enumerate(msg):
                if char in ",.!;:，。！？：；" :
                    result = result+msg[lastpos:i+1]
                    lastpos = i+1
                    if len(result)>10:
                        print(result)
                        nerfreal.put_msg_txt(result)
                        # 累加到全局变量
                        llm_output_text += result
                        result=""
            result = result+msg[lastpos:]
    end = time.perf_counter()
    print(f"llm Time to last chunk: {end-start}s")
    llm_output_text += result
    nerfreal.put_msg_txt(result)