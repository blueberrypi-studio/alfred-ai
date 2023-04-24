import torch
from torchtext.data.utils import get_tokenizer

from models import TransformerModel, PositionalEncoding

print("hello")
tokenizer = get_tokenizer('basic_english', TransformerModel)
print("huh")

# Load the trained model
model = torch.load('model.pth')

# Set the model to evaluation mode
model.eval()
print("lol")

# Create a prompt or a question
prompt = "What is the capital of France?"

# Encode the prompt as a tensor
input_ids = torch.tensor(tokenizer.encode(prompt)).unsqueeze(0)  # Batch size 1

# Generate a response
output = model(input_ids)

# Get the predicted next token
predicted_next_token = torch.argmax(output[0, -1, :]).item()

# Decode the predicted next token
predicted_next_word = tokenizer.decode([predicted_next_token])

# Concatenate the prompt and the predicted next word
response = prompt + predicted_next_word

print(response)
