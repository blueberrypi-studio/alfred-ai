import tkinter as tk
from skills import A_Skill


class Close_All(A_Skill): 
    __custom__ = True     
        
    def close_all(self): 
        self.set_name("Close all widgets")
        print(f"Widgets in use: {self.gui.widgets_in_use}")
        print(f"Alerts in use: {self.gui.alerts_in_use}")
        for widget in self.gui.widgets_in_use:
            widget.close_widget()

        for alert in self.gui.alerts_in_use:
            alert.close_alert()
        
            if self.DEBUG == True:
                # any debug statements go here
                print(f"{widget.skill_name} was closed")
                
        self.gui.widgets_in_use = []
        # self.gui.alerts_in_use = []

        print(f"Widgets in use: {self.gui.widgets_in_use}")
        print(f"Alerts in use: {self.gui.alerts_in_use}")

if __name__ == '__main__':
    pass
