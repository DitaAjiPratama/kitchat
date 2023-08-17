import os
import openai

def chat(api_key, model_type, prompt):
    openai.api_key = api_key
    conversation_history = []
    conversation_history.append({"role": "user", "content": prompt})
    response = openai.ChatCompletion.create(
        model=model_type,
        messages=conversation_history
    )
    assistant_reply = response['choices'][0]['message']['content']
    return assistant_reply
