import openai
import time

openai.api_key = "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"

def ask_question(prompt):
    response = openai.Completion.create(
      model="text-davinci-003",
    #   prompt = "The following is a conversation between a human and an AI assistant. The assistant is helpful, creative, clever, and very friendly.\n\nHuman: Hello, who are you?\nAI: I am an AI created by OpenAI. How can I help you today?\nHuman: Hi, can you tell me a joke?\nAI:",
    #   prompt = "The following is a conversation is between a human and an AI assistant, the assistant behaves like alfred, batmans butler, and is helpful, and friendly. \n\nHuman: Hello, What is your name?\nAI: My name is Alfred, how can I be of Service.\nHuman: Can you remind me to add cheese to my shopping list\nAI: Sure thing",
      prompt = "The following is a conversation is between a human and an AI assistant, the assistant behaves like alfred, batmans butler, and is helpful, and friendly.\n\nHuman: Can you add cheese to my shopping list?\nAI: Certainly, cheese has been added to your shopping list\nHuman: Whats currently on my list\nAI: ",
      temperature=0.9,
      max_tokens=150,
      top_p=1,
      frequency_penalty=0.5,
      presence_penalty=0.6,
      stop=[" Human:", " AI:"]
    )
    return response.choices[0].text.strip()

print("AI: Hello, I'm an AI. What can I help you with today?")
while True:
    prompt = input("You: ")
    if prompt.lower() in ["bye", "goodbye"]:
        print("AI: Goodbye!")
        break
    start = time.time()
    response = ask_question(prompt)
    end = time.time()
    print(f"AI: {response} ({end-start:.2f} seconds)")