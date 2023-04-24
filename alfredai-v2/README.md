## Version 2
Bag of words Algorithim, same as version one, with a few minor tweaks.  
Version 2 of the ai features a gui interface, overtop of the existing version 1 AI code.  
The AI code is based of this [youtube tutorial](https://www.youtube.com/watch?v=RpWeNzfSUHw).

### First install
#### Setup
1. clone this repo
```
git clone https://github.com/blueberrypi-studio/alfred-ai.git
```
2. set up a python venv, or use conda (recomended) using python 3.9 (3.10 will not work)
3. activate the venv/conda
4. Run the command 
```
pip install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cpu
```
5. Run the command
```
pip install nltk
```

On the first install you _**must**_:

5. navigate to the `v2/ai/` directory
6. uncomment this line from `nltk_utils.py` -> `# nltk.download('punkt')`
7. run `nltk_utils.py` with `python3 nltk_utils.py`
8. recomment this line from `nltk_utils.py` -> `nltk.download('punkt')`

### How to run
Create and or edit existing intents in the `intents.json` file  
(see Training section below)


2. navigate to the `v2/ai/` directory
3. Ensure you have followed the first install instructions above.
3. Run the training script using `python3 train.py`
4. Run the bot using `python3 bot.py`


### Training

Here is an example of the training data in the `intents.json` file

```
{
"tag": "greeting",
    "patterns": [
      "Hi",
      "Hey",
      "How are you",
      "Is anyone there?",
      "Hello",
      "Good day"
    ],
    "responses": [
      "Hey",
      "Hello",
      "Hi there, what can I do for you?",
      "Hi there, how can I help?"
    ]
}
```

### Skills
To add a new skill, simply add a new class into the skills folder.  
There is a template for this in the `skills/skills_template.py` file. -> [Here](https://github.com/blueberrypi-studio/alfred-ai/blob/main/v2/skills/skill_template.py)

The Parent class has several methods to make intergration into the main system as simple as possible. The only thing other than the new skill that needs to be added is a new intent in `data/intents.json` (see above)





