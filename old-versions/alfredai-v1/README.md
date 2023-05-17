## Version 1
Bag of words Algorithim.
based of a [youtube tutorial](https://www.youtube.com/watch?v=RpWeNzfSUHw)

### First install
#### Setup
* set up a python venv
* activate the venv
* run `pip3 install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cpu`
* `pip install nltk`

On the first install you _**must**_:
1. uncomment this line from `nltk_utils.py` -> `# nltk.download('punkt')`
2. run `nltk_utils.py` with `python 3 nltk_utils.py`
3. recomment this line from `nltk_utils.py` -> `nltk.download('punkt')`

### How to run
Create and or edit existing intents in the `intents.json` file  
(see First install section above)

1. Run the training script using `python3 train.py`
2. Run the bot using `python3 bot.py`


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

