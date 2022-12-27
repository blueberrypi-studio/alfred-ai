"""
Alfred AI version 2
same as version 1, built into a gui
@author: Haydn Boul
@date: 27-12-22
"""

import threading
import tkinter as tk

# TODO: Remove this to a .conf or similar file
WINDOW_WIDTH = 300
WINDOW_HEIGHT = 400
WINDOW_TITLE = "Alfred AI"
HOLD_TOP_LAYER = True

BOT_NAME = "Alfred"
BACKGROUND_COLOUR = "black"
FOREGROUND_COLOUR = "white"


def setup():
    """Setups the window"""
    alfred = tk.Tk()
    alfred.title(WINDOW_TITLE)
    alfred.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
    # keep on top of other windows, regardless of focus  
    if HOLD_TOP_LAYER: alfred.attributes("-topmost", 1) 

    return alfred


def draw_gui(alfred):
    main_container = tk.Frame(alfred, bg=BACKGROUND_COLOUR).pack(fill="both", expand=True)

    name_tag = tk.Label(main_container, text=BOT_NAME, bg=BACKGROUND_COLOUR, fg=FOREGROUND_COLOUR, font=("Arial", 25))
    name_tag.pack()






def main():
    alfred = setup()
    
    draw_gui(alfred)
    alfred.mainloop()


if __name__ == "__main__":
    main()


