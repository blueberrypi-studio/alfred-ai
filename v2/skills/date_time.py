import tkinter as tk
from time import strftime

from skills import A_Skill


class Time(A_Skill): # note capitalisation
    __custom__ = True # tag used to show this module is a skill      
        
    def time(self): # note same name as class, but no capitals (same as tag name in intents.json)
        self.set_name("Time Module")
        self.draw_widget()
        string = strftime('%H:%M:%S %p')
        self.time_text.config(text=string)
        self.time_text.after(1000, self.update_time)
        
        if self.DEBUG == True:
            print(string)
    

    def update_time(self):
        """updates the time label"""
        string = strftime('%H:%M:%S %p')
        self.time_text.config(text=string)
        self.time_text.after(1000, self.update_time)



    def draw_widget(self):
        """draw a widget, can exclude this if needed (in parent class also)"""
        self.widget_frame = tk.Frame(self.gui.main_container, bg=self.widget_colour, padx=5, pady=5)
        self.content_frame = tk.Frame(self.widget_frame, bg=self.background_colour)
        
        self.time_text = tk.Label(self.content_frame, text="", font=("Arial", 25), fg=self.foreground_colour, bg=self.background_colour, padx=5, pady=5)
        self.time_text.pack()

        self.widget_frame.place(x=1000, y=100)
        self.content_frame.pack()
        

if __name__ == '__main__':
    pass
