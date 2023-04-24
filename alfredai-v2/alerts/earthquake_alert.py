import tkinter as tk
import requests

from alerts import Alert

# REQUEST_URL = "https://api.geonet.org.nz/quake?MMI=3"
REQUEST_URL = "https://api.geonet.org.nz/quake?MMI=1"

class Earthquake_Alert(Alert):
    __alert__ = True # tag used to show this module is an alert

    def get_request(self, query_url):
        response = requests.get(query_url)
        return response.json()      
        
    def earthquake_alert(self):
        """init the alert"""
        self.set_name("Earthquake Alert")
        self.request_url = REQUEST_URL

    
    def get_data(self):
        """assign data to relative variables for display"""
        data = self.get_request(REQUEST_URL)
        self.earthquake = data["features"][0]
        self.magnitude = self.earthquake["properties"]["magnitude"]
        self.location = self.earthquake["properties"]["locality"]
        self.depth = self.earthquake["properties"]["depth"]
        self.time = self.earthquake["properties"]["time"]
        
        if self.DEBUG == True:
            print(self.time)
            print(self.location)
            print(self.magnitude)
            print(self.depth)
        
        self.previous_alert_data = data
          

    def draw_alert(self):
        """draw a widget, can exclude this if needed (in parent class also)"""
        self.get_data()
        self.alert_frame = tk.Frame(self.gui.main_container, bg=self.alert_colour, padx=5, pady=5)
        self.content_frame = tk.Frame(self.alert_frame, bg=self.background_colour)
        
        self.widget_title = tk.Label(self.content_frame, text=self.alert_name, bg=self.background_colour, fg=self.foreground_colour).pack()

        self.time_label = tk.Label(self.content_frame, text=self.time, bg=self.background_colour, fg=self.foreground_colour).pack(side="left")
        self.magnitude_label = tk.Label(self.content_frame, text=self.magnitude, bg=self.background_colour, fg=self.foreground_colour).pack(side="left")
        self.location_label = tk.Label(self.content_frame, text=self.location, bg=self.background_colour, fg=self.foreground_colour).pack(side="left")
        self.depth_label = tk.Label(self.content_frame, text=self.depth, bg=self.background_colour, fg=self.foreground_colour).pack(side="left")
        

        self.alert_frame.place(x=1200, y=700)
        self.content_frame.pack()
        

if __name__ == '__main__':
    pass