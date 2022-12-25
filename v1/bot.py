import random
import json

import torch
import torch.nn as nn

from model import NeuralNet
from nltk_utils import bag_of_words, tokenize
from skills import Skills as sk


device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

with open('intents.json') as json_data:
    intents = json.load(json_data)

FILE = "data.pth"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data['all_words']
tags = data['tags']
model_state = data["model_state"]

model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

bot_name = "Alfred"

# If adding new skills, add tag name from intents.json to this list
SKILLS = ["take_notes", "read_notes"] 

print("Let's chat! (type 'quit' to exit)")
while True:
    sentence = input("You: ")
    if sentence == "quit":
        break

    sentence = tokenize(sentence)
    X = bag_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X)

    output = model(X)
    _, predicted = torch.max(output, dim=1)

    tag = tags[predicted.item()]

    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]
    if prob.item() > 0.75:
        for intent in intents['intents']:
            if tag == intent["tag"]:
                print(f"{bot_name}: {random.choice(intent['responses'])}\n")
                if tag in SKILLS:
                    # print(tag)
                    skill = sk()
                    skill.choose_skill(tag)
                
                    
            
    else:
        print(f"{bot_name}: I do not understand...")



        

