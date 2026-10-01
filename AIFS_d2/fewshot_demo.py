from ollama import chat
messages=[
    {"role":"system","content":"Identify sentiment as position,negative, neutral.Reply with one word only."},

    {"role":"user","content":"great Movie!"},
    {"role":"system","content":" positive"},
    
    {"role":"user","content":"waste of money"},
    {"role":"system","content":"negative"},

    {"role":"user","content":"it was okay "},
    {"role":"system","content":"neutral "},

    {"role":"user","content":"loved the acting but the ending was dull"}

]
response=chat(
    model="llama3.2",
    messages=messages
)
print(response.message.content)
