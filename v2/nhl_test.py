import requests

def get_request(query_url):
    response = requests.get(query_url)
    return response.json()


todays_games = []
data = get_request("https://statsapi.web.nhl.com/api/v1/schedule/?expand=schedule.linescore")
sub_dict = data['dates'][0]
games_list = sub_dict['games']

for game_info in games_list:
    data = game_info["linescore"]
    print(data)

    home_team = data['teams']['home']['team']['name']
    away_team = data['teams']['away']['team']['name']

    home_score = data['teams']['home']['goals']
    away_score = data['teams']['away']['goals']

    period = data['currentPeriodOrdinal']
    if period == 0:
        time="not yet started"
    else:
        time = data['currentPeriodTimeRemaining']


    game_score = (f"{period}",f"{time}", f"{home_team}: {home_score}", f"{away_team}: {away_score}")
    todays_games.append(game_score)

# print(data)
for game in todays_games:
    print(game)

