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
        self.alert_colour = config['GUI Colours']['alert_colour']

        self.bot = bot
        self.gui = gui
        self.alert_name = None
        self.previous_alert_data = None
        self.request_url = None

        self.gui.alerts_in_use.append(self)
        

    def check_for_update(self):
        """check for new updates"""
        new_data = self.get_request(self.request_url)
        if self.previous_alert_data is not None:
            if new_data != self.previous_alert_data:
                self.previous_alert_data = new_data
                return True
            else:
                return False
        self.previous_alert_data = new_data
        return False

    def set_name(self, name):
        """sets the name of the skill"""
        self.alert_name = name

    def close_alert(self):
        """closes the widget"""
        print(f"widget should be gone {self.alert_frame}")
        self.alert_frame.destroy()
        print(f"widget should be gone {self.alert_frame}")

