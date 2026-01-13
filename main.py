import os
from ai21 import AI21Client
from ai21.models.chat import ChatMessage

client = AI21Client()

messages = [
    ChatMessage(role="system", content="You are a helpful assistant."),
    ChatMessage(role="user", content="how i can make money?")
]

respone=client.chat.completions.create(
    model="jamba-mini",
    messages=messages
)
print(respone,"response...........")
print(respone.choices[0].message.content)
