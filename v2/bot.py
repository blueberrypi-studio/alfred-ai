from gui.GUI import Application
from ai.brain import Brain


BOT_NAME = "Alfred"

        
def main():
    bot = Brain(BOT_NAME)
    gui = Application(bot, BOT_NAME)
    gui.start()
    
    

main()