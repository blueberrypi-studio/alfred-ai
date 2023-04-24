import tkinter as tk
from config.config import Config

class A_Skill():
    def __init__(self, bot, gui):
        config = Config.read_config()

        debug = config['GUI Config']['DEBUG']
        if debug == "True": self.DEBUG = True
        else: self.DEBUG = False

        self.background_colour = config['GUI Colours']['background_colour']
        self.foreground_colour = config['GUI Colours']['foreground_colour']
        self.widget_colour = config['GUI Colours']['widget_colour']

        self.bot = bot
        self.gui = gui
        self.skill_name = None
        
        self.widget_frame = tk.Frame(self.gui.main_container, bg=self.widget_colour, padx=5, pady=5)
        self.gui.widgets_in_use.append(self)

        # for widget in self.gui.widgets_in_use:
        #     print(self.gui.widgets_in_use)
        #     if type(widget) == type(self):
        #         del(self)
        #         return f"You are already running the"





    def draw_widget(self):
        self.widget_frame = tk.Frame(self.gui.main_container, bg="purple", padx=5, pady=5)
        self.widget_label = tk.Label(self.widget_frame, text="test widget")

        self.widget_label.pack()
        self.widget_frame.place(x=100, y=100)

    def set_name(self, name):
        """sets the name of the skill"""
        self.skill_name = name

    def close_widget(self):
        """closes the widget"""
        self.widget_frame.destroy() 

