"""
Alfred AI version 2
same as version 1, built into a gui
@author: Haydn Boul
@date: 27-12-22
"""

import threading
import tkinter as tk

from config.config import Config

class Application(tk.Frame):
    def __init__(self, brain, bot_name):
        self.config = Config.read_config()
        self.root = tk.Tk()
        self.brain = brain
        self.root.title(self.config['General Settings']['window_title'])
        self.window_width = self.config['General Settings']['window_width']
        self.window_height = self.config['General Settings']['window_height']
        self.root.geometry(f"{self.window_width}x{self.window_height}")
        
        self.bot_name = self.config['General Settings']['bot_name']

        self.background_colour = self.config['GUI Colours']['background_colour']
        self.foreground_colour = self.config['GUI Colours']['foreground_colour']
        self.widget_colour = self.config['GUI Colours']['widget_colour']

        # keep on top of other windows, regardless of focus  
        if self.config['General Settings']['hold_top_layer'] == "True": self.root.attributes("-topmost", 1)
        self.widgets_in_use = []
        self.alerts_in_use = []
        tk.Frame.__init__(self, self.root)
        self.create_widgets()

    def create_widgets(self):
        
        self.main_container = tk.Frame(bg=self.background_colour, padx=5, pady=5)
        self.heading_container = tk.Frame(master=self.main_container, padx=5, pady=5, bg=self.background_colour)
        self.input_box = tk.Frame(master=self.main_container, bg=self.widget_colour, padx=5, pady=5)
        self.response_container = tk.Frame(master=self.input_box, bg=self.background_colour, padx=5, pady=5)
        self.past_input_container = tk.Frame(master=self.input_box, bg=self.background_colour, padx=5, pady=5)
        self.entry_container = tk.Frame(master=self.input_box, bg=self.background_colour, padx=5, pady=5)

        self.canvas = tk.Canvas(self.heading_container, width=300, height=300, borderwidth=0, highlightthickness=0, bg=self.background_colour)
        
        self.canvas.create_oval(25,25,275,275,outline=self.widget_colour, width=5)
        self.canvas.pack(anchor="center")

        self.canvas.create_text(150, 150, font=("Arial", 50), text=self.bot_name, fill=self.foreground_colour)

        self.past_input_label = tk.Label(master=self.past_input_container, bg=self.background_colour, fg=self.foreground_colour, text="You: ", font=("Arial", 15))
        self.past_input_label.pack(side="left")
        
        self.response_field = tk.Label(master=self.response_container, bg=self.background_colour, fg=self.foreground_colour, text=f"{self.bot_name}: Hi Sir, How can I help?", font=("Arial", 15))
        self.response_field.pack(side="left")
        
        self.entry_field = tk.Entry(master=self.entry_container, width=self.window_width, font=("Arial", 15))
        self.entry_field.pack()
        self.entry_field.focus_set()
        self.root.bind('<Return>', self.parse)
        
        self.main_container.pack(fill="both", expand=True)
        self.heading_container.place(rely=.5, relx=.5, anchor="center")
        self.input_box.pack(fill="both", expand=False, side="bottom")
        
        self.entry_container.pack(fill="both", expand=False, side="bottom")
        self.past_input_container.pack(fill="both", expand=False, side="top")
        self.response_container.pack(fill="both", expand=False, side="bottom")
        
        # change window icon
        p1 = tk.PhotoImage(file = 'images/icon.png')
        self.root.iconphoto(False, p1)


    def parse(self, event):
        # TODO: interface this with bot, rather than just update with inputted text
        user_input = self.entry_field.get()
        response = self.brain.request(user_input)
        self.past_input_label.config(text=f"You: {user_input}")
        self.response_field.config(text=f"{self.bot_name}: {response}")
        self.entry_field.delete(0, "end")
        

    def start(self):
        """Starts The application"""
        
        self.root.mainloop()


if __name__ == "__main__":
    bot1 = Application().start()
