import openai

# Use the "text" version of the GPT-3 model
openai.api_key = "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"
model_engine = "text-davinci-002"

# Function to get a response from the virtual assistant
def get_response(input_text):
  prompt = (f"{input_text}\n"
           )

  completions = openai.Completion.create(
      engine=model_engine,
      prompt=prompt,
      max_tokens=1024,
      n=1,
      stop=None,
      temperature=0.5,
  )

  message = completions.choices[0].text
  return message.strip()

# Test the virtual assistant
while True:
  user_input = input("You: ")
  if user_input == "exit":
    break
  else:
    response = get_response(user_input)
    print(f"Assistant: {response}")
