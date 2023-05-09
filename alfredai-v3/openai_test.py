import openai
import json

# Set up OpenAI API credentials
openai.api_key = ""

# Set up the prompt and parameters
prompt="You are a virtual assistant that is helpful and friendly"
engine = "davinci-codex" 
max_tokens = 150 
temperature = 0.5 


while True:
    prompt = input("You: ")
    if prompt == "quit":
        break
    response = openai.Completion.create(
        model="gpt-3.5-turbo",
        messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"},
        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        {"role": "user", "content": "Where was it played?"}
    ]
    )
    if len(response.choices) > 0:
        message = response.choices[0].text.strip()
        print("AI: " + message)
    else:
        print("Sorry, I couldn't generate a response.")