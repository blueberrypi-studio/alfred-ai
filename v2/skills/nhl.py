import requests
from skills import A_Skill


class Todays_Schedule(A_Skill):
    __custom__ = True
    def get_request(self, query_url):
        response = requests.get(query_url)
        return response.json()

    def todays_schedule(self):
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

        return todays_games
        


if __name__ == '__main__':
    nhl = Todays_Schedule()
    for game in nhl.todays_schedule():
        print(game)
