# KitChat
Python Script for conversation with openai.

It need `openai` python library.

## Usage

    kitchat.chat(api_key, model_type, chat)

Example:

    import kitchat
    api_key = "xxxxxxxxxx"
    model   = "gpt-3.5-turbo"
    chat    = """Who are you?"""
    result  = kitchat.chat(api_key, model, chat)
    print(result)

## Anti-Features

It have a features that you may not like:
- Non-Free Network Services
