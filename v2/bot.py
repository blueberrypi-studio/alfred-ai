# ================== imports ==================

# =============================================

# ============ import bots modules ============
from gui.GUI import Application
from ai.brain import Brain
from config.config import Config
# =============================================

# ================== Globals ==================
config = Config.read_config()
bot_name = config["General Settings"]["bot_name"]
# =============================================
        
def main():
    """run the bot"""
    bot = Brain(bot_name, config)
    gui = Application(bot, bot_name)
    bot.set_gui(gui)

    gui.start()
    
    
main()