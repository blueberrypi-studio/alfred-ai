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

BACKGROUND_COLOUR = "black"
FOREGROUND_COLOUR = "white"

class Application(tk.Frame):
    def __init__(self, bot_name):
        self.root = tk.Tk()
        self.root.title(WINDOW_TITLE)
        self.root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
        self.bot_name = bot_name
        # keep on top of other windows, regardless of focus  
        if HOLD_TOP_LAYER: self.root.attributes("-topmost", 1)

        tk.Frame.__init__(self, self.root)
        self.create_widgets()

    def create_widgets(self):
        
        self.main_container = tk.Frame(bg="purple", padx=5, pady=5)
        self.heading_container = tk.Frame(master=self.main_container, bg="blue", padx=5, pady=5)
        self.response_container = tk.Frame(master=self.main_container, bg="green", padx=5, pady=5)
        self.entry_container = tk.Frame(master=self.main_container, bg="yellow")

        self.name_tag = tk.Label(master=self.heading_container, text=self.bot_name, bg=BACKGROUND_COLOUR, fg=FOREGROUND_COLOUR, font=("Arial", 25))
        self.name_tag.pack()

        self.response_field = tk.Label(master=self.response_container, text="Answer goes here")
        self.response_field.pack()
        
        self.entry_field = tk.Entry(master=self.entry_container, width=(WINDOW_WIDTH))
        self.entry_field.pack()
        self.root.bind('<Return>', self.parse)
        
        self.main_container.pack(fill="both", expand=True)
        self.heading_container.pack(fill="both")
        self.response_container.pack(fill="both", expand=True)
        self.entry_container.pack(fill="both", expand=False)

        # change window icon
        p1 = tk.PhotoImage(file = 'v2/images/icon.png')
        self.root.iconphoto(False, p1)

    def parse(self, event):
        # TODO: interface this with bot, rather than just update with inputted text
        user_input = self.entry_field.get()
        self.response_field.config(text=user_input)
        

    def start(self):
        """Starts The application"""
        
        self.root.mainloop()


if __name__ == "__main__":
    bot1 = Application().start()
