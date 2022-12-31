from gui.GUI import Application
from ai.brain import Brain


BOT_NAME = "Alfred"

        
def main():
    bot = Brain(BOT_NAME)
    gui = Application(bot, BOT_NAME)
    bot.set_gui(gui)
    gui.start()
    
    
main()