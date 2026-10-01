from ollama import chat
response = chat(
    model="llama3.2",
    messages=[
        {
            "role":"user",
            "content":"What is sql? explain briefly."
        }
    ]
)
print(response.message.content)
