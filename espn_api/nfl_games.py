import requests
from espn_api.custom_utils import BASE_ESPN, get_pretty_est
# from custom_utils import BASE_ESPN, get_pretty_est
from espn_api.nfl_leaders import generate_leaders
from pprint import pprint
import json

def get_nfl_games():
	NFL_URL = f"{BASE_ESPN}/football/nfl/scoreboard"
	nfl_raw = requests.get(NFL_URL).json()
	events = nfl_raw['events']
	week = nfl_raw["week"]["number"]
	nfl_clean = {"week": week}
	
	passers, rushers, receivers = generate_leaders()
	passer_iterable = iter(passers)
	rusher_iterable = iter(rushers)
	receiver_iterable = iter(receivers)
	
	nfl_clean['games'] = []	
	for e in events:
		competitions = e["competitions"]
		for c in competitions:
			home_team = c["competitors"][0]
			away_team = c["competitors"][1]
			time_pretty, day_pretty, date_pretty = get_pretty_est(c["date"])
			
			game = {
					"home_team": {
						"name": home_team["team"]["displayName"],
						"score": home_team["score"],
						"logo": home_team["team"]["logo"],
						"record": home_team["records"][0]["summary"]
						},
					"away_team": {
						"name": away_team["team"]["displayName"],
						"score": away_team["score"],
						"logo":  away_team["team"]["logo"],
						"record": away_team["records"][0]["summary"]
						},
					"time": time_pretty,			
					"day": day_pretty,
					"date": date_pretty,
					"stadium": c["venue"]["fullName"],
					"city": c["venue"]["address"]["city"],
					"leaders": {
						"passing": next(passer_iterable), 
						"rushing": next(rusher_iterable),
						"receiving": next(receiver_iterable)
						}
			}			
			nfl_clean['games'].append(game)

	# with open('json/nfl_v1.json', 'w') as outfile:
	# 	json.dump(nfl_clean, outfile, indent=2)
	return nfl_clean