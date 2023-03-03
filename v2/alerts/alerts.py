"""Alerts Module, Automatically run skills"""

import tkinter as tk
from config.config import Config

class Alert():
    def __init__(self, bot, gui) -> None:
        config = Config.read_config()

        # ============= debug mode toggle =============
        debug = config['GUI Config']['DEBUG']
        if debug == "True": self.DEBUG = True
        else: self.DEBUG = False
        # =============================================

        self.background_colour = config['GUI Colours']['background_colour']
        self.foreground_colour = config['GUI Colours']['foreground_colour']
        self.widget_colour = config['GUI Colours']['widget_colour']

        self.bot = bot
        self.gui = gui
        self.alert_name = None

        self.alert_frame = tk.Frame(self.gui.main_container, bg=self.widget_colour, padx=5, pady=5)

        self.gui.alerts_in_use.append(self)

    
    def draw_widget(self):
        self.alert_frame = tk.Frame(self.gui.main_container, bg="purple", padx=5, pady=5)
        self.alert_label = tk.Label(self.alert_frame, text="test alert")

        self.alert_label.pack()
        self.alert_frame.place(x=100, y=100)

    def set_name(self, name):
        """sets the name of the skill"""
        self.skill_name = name

    def close_alert(self):
        """closes the widget"""
        self.alert_frame.destroy()

