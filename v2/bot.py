import threading
from time import sleep

# from gui.GUI import Application
from ai.brain import Brain


BOT_NAME = "Alfred"

        
def main():
    bot = Brain(BOT_NAME)
    brain_thread = threading.Thread(target=bot.event_loop())
    brain_thread.start()
    
    # Application.start()
    
    

main()