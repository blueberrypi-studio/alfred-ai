import random
import json

import torch
import torch.nn as nn

from ai.model import NeuralNet
from ai.nltk_utils import bag_of_words, tokenize
from ai.skills import Skills as sk


class Brain():
    def __init__(self, bot_name):
        self.bot_name = bot_name
        self.sk = sk()
        self.skills = self.sk.get_skills()

        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

        with open('data/intents.json') as json_data:
            self.intents = json.load(json_data)

        file = "data/data.pth"
        data = torch.load(file)

        self.input_size = data["input_size"]
        self.hidden_size = data["hidden_size"]
        self.output_size = data["output_size"]
        self.all_words = data['all_words']
        self.tags = data['tags']
        self.model_state = data["model_state"]

        self.model = NeuralNet(self.input_size, self.hidden_size, self.output_size).to(self.device)
        self.model.load_state_dict(self.model_state)
        self.model.eval()

    def event_loop(self):
        print("Let's chat! (type 'quit' to exit)")
        while True:
            sentence = input("You: ")
            if sentence == "quit":
                break

            sentence = tokenize(sentence)
            X = bag_of_words(sentence, self.all_words)
            X = X.reshape(1, X.shape[0])
            X = torch.from_numpy(X)

            output = self.model(X)
            _, predicted = torch.max(output, dim=1)

            tag = self.tags[predicted.item()]

            probs = torch.softmax(output, dim=1)
            prob = probs[0][predicted.item()]
            if prob.item() > 0.75:
                for intent in self.intents['intents']:
                    if tag == intent["tag"]:
                        print(f"{self.bot_name}: {random.choice(intent['responses'])}\n")
                        if tag in self.skills:
                            # print(tag)

                            self.skills.choose_skill(tag)
                        
                            
                    
            else:
                print(f"{self.bot_name}: I do not understand...")


if __name__ == "__main__":
    alfred = Brain("Timmy")
    alfred.event_loop()



        

