import requests
import tkinter as tk
from skills import A_Skill


class Todays_Schedule(A_Skill):
    __custom__ = True
           

    def get_request(self, query_url):
        response = requests.get(query_url)
        return response.json()

    def draw_widget(self, game_list):

        self.widget_frame = tk.Frame(self.gui.main_container, bg="white", padx=5, pady=5)
        self.content_frame = tk.Frame(self.widget_frame, bg="black")
        
        self.widget_title = tk.Label(self.content_frame, text=self.skill_name).pack()
        for game in game_list:
            widget_label = tk.Label(self.content_frame, text=game, bg="black", fg="white")
            widget_label.pack()

        self.widget_frame.place(x=100, y=100)
        self.content_frame.pack()
        
        
    def todays_schedule(self):
        self.set_name("NHL Schedule")
        todays_games = []
        data = self.get_request("https://statsapi.web.nhl.com/api/v1/schedule/?expand=schedule.linescore")
        sub_dict = data['dates'][0]
        games_list = sub_dict['games']

        for game in games_list:
            game = game["teams"]
            home_team = game['home']['team']['name']
            away_team = game['away']['team']['name']

            home_score = game['home']['score']
            away_score = game['away']['score']

            game_score = (f"{home_team}: {home_score}", f"{away_team}: {away_score}")
            todays_games.append(game_score)
        
        if self.DEBUG == True:
            for game in todays_games:
                print(game)

        self.draw_widget(todays_games)
        return todays_games
        


if __name__ == '__main__':
    nhl = Todays_Schedule()
    for game in nhl.todays_schedule():
        print(game)
