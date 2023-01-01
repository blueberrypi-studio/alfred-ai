import tkinter as tk
from config.config import Config

class A_Skill():
    def __init__(self, bot, gui):
        self.DEBUG = True

        self.bot = bot
        self.gui = gui
        self.skill_name = None
        config = Config.read_config()

        self.background_colour = config['GUI Colours']['background_colour']
        self.foreground_colour = config['GUI Colours']['foreground_colour']
        self.widget_colour = config['GUI Colours']['widget_colour']
        

    def draw_widget(self):
        self.widget_frame = tk.Frame(self.gui.main_container, bg="purple", padx=5, pady=5)
        self.widget_label = tk.Label(self.widget_frame, text="test widget")

        self.widget_label.pack()
        self.widget_frame.place(x=100, y=100)

    def set_name(self, name):
        """sets the name of the skill"""
        self.skill_name = name
