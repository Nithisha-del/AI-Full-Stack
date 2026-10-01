from ollama import chat
roles=[
    "you are strict teacher.answer briskly and with in 1 line.",
    "you are movie director.answer in flimy way.one line answer",
    "you are a lawyer.answer professionally.one line answer."
]
for role in roles:
    response=chat(
        model="llama3.2",
        messages=[
            {
                "role":"system",
                "content":role
              

            },
            {
                "role":"user",
                "content":"how many coloure in the rainbow?"
                
            }
        ]
    )
    print(f"---{role}---")
    print(response.message.content)
    print()
