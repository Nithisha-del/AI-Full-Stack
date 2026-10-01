from ollama import chat

bad="tell me about cats"
good="list 3 cat breeds that are suitable for a penthouse.2 lines about each."
responseB = chat(
    model="llama3.2",
    messages=[
        "role":"user",
        "content":bad
    ]
)
responseG = chat(
    model="llama3.2",
    messages=[
        "role":"user",
        "content":good
    ]
)
print(f"Bad prompt result:{respondB.message.content}")
print()
print(f"Good prompt result:{respondG.message.content}")