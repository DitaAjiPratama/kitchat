# kitchat
Python Script for conversation with openai.

It need `openai` python library.

It have a features that you may not like:
- Non-Free Network Services

## Usage

    kitchat.chat(api_key, model_type, chat)

Example:

    import kitchat
    api_key = "xxxxxxxxxx"
    model   = "gpt-3.5-turbo"
    chat    = """Who are you?"""
    kitchat.chat(api_key, model, chat)
