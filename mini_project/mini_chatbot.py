from ollama import chat

system_msg="you are a friendly tutor.Answer in one question"
history=[ {"role":"system","content":system_msg}]
question_counter=0
while True:
    question = input("you:")
    if question=="":
        print("Nithisha:Please type something")
        continue

    if question.lower().strip()=="/history":
        print("-----your conversation so far -----")
        if len(history)<2:
            print("Nothing here so far!")
        for msg in history [1:]:
            if msg["role"]=="user":
                speaker="you"
            else:
                speaker="Nithisha"
            print(f"{speaker}:{msg["content"]}")
        print("-------------------------------")
        print()
        continue

    if question.lower().strip()=="/help":
        print("----------available commands-------")
        print("/history-displays conversation history")
        print("/clear-clears chat history")
        print("/help-displays this list")
        print("exit-quits the chatbot")
        print()
        continue

    if question.lower().strip()=="/clear":
        history=[{"role":"system","content":system_msg}]
        print("your history is cleared.Start a fresh conversation.")
        print()
        continue

    if question.lower().strip()=="exit":
        print("Nithisha:Goodbye user.please come back soon!")
        break
    history.append({"role":"user","content":question})
    question_counter+=1
    try:
        response = chat(
                model="llama3.2",
                messages=history
            )
        reply=response["message"]["content"]
        history.append({"role":"assistant","content":reply})
        print(f"Nithisha:{reply}")
        print()
    except Exception as e:
        print("unknown issue.Is ollama running?")
