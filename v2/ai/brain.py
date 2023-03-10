import random
import json
import threading

import torch
import torch.nn as nn

import pyttsx3

from ai.model import NeuralNet
from ai.nltk_utils import bag_of_words, tokenize
from skills import * # import all skills


class Brain():
    def __init__(self, bot_name, config, gui=None):
        self.bot_name = bot_name
        self.gui = gui
        self.config = config

        # code sourced from https://stackoverflow.com/a/51693418
        self.skills = [x for x in globals() if hasattr(globals()[str(x)], '__custom__')]

        # self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        self.device = "cpu"

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

        self.engine = pyttsx3.init()
        self.speak = self.config['General Settings']['speak']
        self.engine.setProperty('rate', 175)
        # voices = self.engine.getProperty('voices')
        # self.engine.setProperty('voice', voices[1].id)
        

    def set_gui(self, gui):
        self.gui = gui

    def say(self, response):
        if self.speak == "True":
            self.engine.say(response)
            self.engine.runAndWait()
            self.engine.stop()
            return
            
    
    def request(self, sentence):
            
        sentence = tokenize(sentence)
        sentence
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
                    response = f"{random.choice(intent['responses'])}"
                    
                    if tag in self.skills:
                        
                        m = globals()[tag](self, self.gui)
                        
                        func = getattr(m, tag.lower())
                        print(f"Skill run: {tag}")

                        result = func()
                        if result is not None:
                            response = result
                                    
        else:
            response = f"I do not understand..."
        
        self.thread = threading.Thread(target=self.say, args=(response,))
        self.thread.start()
        return response


if __name__ == "__main__":
    alfred = Brain("Timmy")
    alfred.request("Look something up for me?")



        

