"""
Alfred AI version 2
same as version 1, built into a gui
@author: Haydn Boul
@date: 27-12-22
"""

import threading
import tkinter as tk

# TODO: Remove this to a .conf or similar file
WINDOW_WIDTH = 1500
WINDOW_HEIGHT = 800
WINDOW_TITLE = "Alfred AI"
HOLD_TOP_LAYER = True

BACKGROUND_COLOUR = "black"
FOREGROUND_COLOUR = "white"

class Application(tk.Frame):
    def __init__(self, brain, bot_name):
        self.root = tk.Tk()
        self.root.title(WINDOW_TITLE)
        self.root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
        self.brain = brain
        self.bot_name = bot_name
        # keep on top of other windows, regardless of focus  
        if HOLD_TOP_LAYER: self.root.attributes("-topmost", 1)

        tk.Frame.__init__(self, self.root)
        self.create_widgets()

    def create_widgets(self):
        
        self.main_container = tk.Frame(bg="purple", padx=5, pady=5)
        self.heading_container = tk.Frame(master=self.main_container, bg="yellow", padx=5, pady=5)
        self.response_container = tk.Frame(master=self.main_container, bg="green", padx=5, pady=5)
        self.entry_container = tk.Frame(master=self.main_container, bg="yellow")

        self.name_tag = tk.Label(master=self.heading_container, text=self.bot_name, bg=BACKGROUND_COLOUR, fg=FOREGROUND_COLOUR, font=("Arial", 25))
        self.name_tag.pack(anchor="center")

        self.response_field = tk.Label(master=self.response_container, text="Answer goes here")
        self.response_field.pack()
        
        self.entry_field = tk.Entry(master=self.entry_container, width=(WINDOW_WIDTH))
        self.entry_field.pack()
        self.root.bind('<Return>', self.parse)
        
        self.main_container.pack(fill="both", expand=True)
        self.heading_container.place(rely=.5, relx=.5, anchor="center")
        self.entry_container.pack(fill="both", expand=False, side="bottom")
        self.response_container.pack(fill="both", expand=False, side="bottom")
        

        # change window icon
        p1 = tk.PhotoImage(file = 'images/icon.png')
        self.root.iconphoto(False, p1)

    def parse(self, event):
        # TODO: interface this with bot, rather than just update with inputted text
        user_input = self.entry_field.get()
        response = self.brain.request(user_input)
        self.response_field.config(text=response)
        

    def start(self):
        """Starts The application"""
        
        self.root.mainloop()


if __name__ == "__main__":
    bot1 = Application().start()
