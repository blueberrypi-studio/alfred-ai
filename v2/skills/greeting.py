import tkinter as tk
import datetime

from skills import A_Skill


class Greeting(A_Skill): 
    __custom__ = True     
        
    def greeting(self): 
        self.set_name("Greeting")
        
        time = datetime.datetime.now()
        if time.hour < 12:
            return "Good Morning sir"
        if time.hour >= 12 and time.hour < 17:
            return "Good Afternoon sir"
        else:
            return "Good Evening sir"
        
        
        
        if self.DEBUG == True:
            # any debug statements go here
            print(time)
            pass


        # return data

        

if __name__ == '__main__':
    pass
