import requests
import json
from dateutil.parser import parse
from collections import defaultdict
from nfl_api.leaders import generate_leaders
from pprint import pprint

BASE_ESPN = "https://site.api.espn.com/apis/site/v2/sports/"
NFL_URL = f"{BASE_ESPN}football/nfl/scoreboard"
LALIGA_URL = f"{BASE_ESPN}soccer/esp.1/scoreboard"

def get_games():
	nfl_data = requests.get(NFL_URL).json()
	events = nfl_data['events']	
	
	passers, rushers, receivers = generate_leaders()
	passer_iterable = iter(passers)
	rusher_iterable = iter(rushers)
	receiver_iterable = iter(receivers)	
	
	games = []	
	for e in events:
		competitions = e["competitions"]
		for c in competitions:
			home_team = c["competitors"][0]
			away_team = c["competitors"][1]
			
			raw_unix_date = c["date"]
			python_date_obj = parse(raw_unix_date)
			date_plain_lang = python_date_obj.strftime("%B %d %Y")				
			day_plain_lang = python_date_obj.strftime("%A")
			
			game = {
					"home_team": {
						"name": home_team["team"]["displayName"],
						"score": home_team["score"],
						"logo": home_team["team"]["logo"]
						},
					"away_team": {
						"name": away_team["team"]["displayName"],
						"score": away_team["score"],
						"logo":  away_team["team"]["logo"]
						},
					"day": day_plain_lang,
					"date": date_plain_lang,
					"stadium": c["venue"]["fullName"],
					"leaders": {
						"passing": next(passer_iterable), 
						"rushing": next(rusher_iterable),
						"receiving": next(receiver_iterable)
						}
			}
			games.append(game)

	# with open('json/games_v5.json', 'w') as outfile:
	# 	json.dump(games, outfile)

	return games
get_games()
