import tkinter as tk

from skills import A_Skill


class Skill_Class(A_Skill): # note capitalisation
    __custom__ = True # tag used to show this module is a skill      
        
    def skill_class(self): # note same name as class, but no capitals (same as tag name in intents.json)
        self.set_name("Skill Name Goes Here")
        
        # skill implementation goes here
        
        if self.DEBUG == True:
            # any debug statements go here
            pass

        self.draw_widget(data)

        return data


    def draw_widget(self):
        """draw a widget, can exclude this if needed (in parent class also)"""
        self.widget_frame = tk.Frame(self.gui.main_container, bg="white", padx=5, pady=5)
        self.content_frame = tk.Frame(self.widget_frame, bg="black")
        
        self.widget_title = tk.Label(self.content_frame, text=self.skill_name).pack()

        self.widget_frame.place(x=100, y=100)
        self.content_frame.pack()
        

if __name__ == '__main__':
    pass
