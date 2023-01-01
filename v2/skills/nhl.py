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
        
        self.widget_title = tk.Label(self.content_frame, text=self.skill_name).grid(row=0, column=0, columnspan=2)
        
        row = 1
        column = 0

        for game in game_list:
            game_box = tk.Frame(self.content_frame, padx=5, pady=5)
            time_label = tk.Label(game_box, text=f"{game[0]}: {game[1]}")
            time_label.pack()
            home_team_label = tk.Label(game_box, text=game[2], bg="black", fg="white", padx=5, pady=5)
            home_team_label.pack()

            away_team_label = tk.Label(game_box, text=game[3], bg="black", fg="white", padx=5, pady=5)
            away_team_label.pack()

            game_box.grid(row=row, column=column)

            column += 1
            if column >= 2:
                column = 0
                row += 1

        self.content_frame.pack()
        self.widget_frame.place(x=100, y=100)
        
            

        
        
        
    def todays_schedule(self):
        self.set_name("NHL Schedule")
        todays_games = []
        data = self.get_request("https://statsapi.web.nhl.com/api/v1/schedule/?expand=schedule.linescore")
        sub_dict = data['dates'][0]
        games_list = sub_dict['games']

        for game in games_list:
            data = game["linescore"]

            home_team = data['teams']['home']['team']['name']
            away_team = data['teams']['away']['team']['name']

            home_score = data['teams']['home']['goals']
            away_score = data['teams']['away']['goals']

            period = data['currentPeriod']
            if period == 0:
                time="not yet started"
            else:
                time = data['currentPeriodTimeRemaining']


            game_score = (f"{period}",f"{time}", f"{home_team}: {home_score}", f"{away_team}: {away_score}")
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
