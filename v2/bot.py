from gui.GUI import Application
from ai.brain import Brain
from config.config import Config


BOT_NAME = "Alfred"

        
def main():
    config = Config.read_config()
    # Config.print_config()
    bot = Brain(BOT_NAME)
    gui = Application(bot, BOT_NAME)
    bot.set_gui(gui)
    gui.start()
    
    
main()