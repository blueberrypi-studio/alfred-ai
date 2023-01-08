import tkinter as tk

from skills import A_Skill


class Close_All(A_Skill): 
    __custom__ = True     
        
    def close_all(self): 
        self.set_name("Close all widgets")
        
        for widget in self.gui.widgets_in_use:
            widget.close_widget()
        
            if self.DEBUG == True:
                # any debug statements go here
                print(f"{widget.skill_name} was closed")
                
        self.gui.widgets_in_use = []
        

if __name__ == '__main__':
    pass
