import os
from ai21 import AI21Client
from ai21.models.chat import ChatMessage

client = AI21Client()

messages = [
    ChatMessage(role="system", content="You are a helpful assistant."),
    ChatMessage(role="user", content="who won the first cricket worldcup?")
]

respone=client.chat.completions.create(
    model="jamba-mini",
    messages=messages,
    max_tokens=50,
    n=3
)
print(respone,"response...........")
print(respone.choices[0].message.content)
