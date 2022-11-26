import requests
from espn_api.custom_utils import BASE_ESPN, get_pretty_est, get_soccer_scorers, get_current_est_datetime
# from custom_utils import BASE_ESPN, get_pretty_est, make_wiki_link, get_soccer_scorers
from pprint import pprint
import json

def get_soccer_games(LEAGUE_CODE):
	full_est_now, trunc_est_now = get_current_est_datetime()	
	LEAGUE_ENDPOINT = f"{BASE_ESPN}/soccer/{LEAGUE_CODE}/scoreboard?dates=20221125"	
	soccer_raw = requests.get(LEAGUE_ENDPOINT).json()
	events = soccer_raw['events']
	
	time_pretty, day_pretty, date_pretty = get_pretty_est(full_est_now)
	soccer_clean = {"day": day_pretty, "date": date_pretty}
	
	soccer_clean['games'] = []	
	for e in events: 
		competitions = e["competitions"]		
		for comp in competitions:
			home_team = comp["competitors"][0]
			away_team = comp["competitors"][1]
			time_pretty, day_pretty, date_pretty = get_pretty_est(comp["date"])		
			details = comp.get("details")
			goals, penalties = get_soccer_scorers(details)

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
				"scorers": {
					"goals": goals,
					"penalties": penalties
				},
				"time": time_pretty,
				"day": day_pretty,
				"date": date_pretty,
				"stadium": comp["venue"]["fullName"],
				"city": comp["venue"]["address"]["city"],
			}
			soccer_clean['games'].append(game)

	# breakpoint()
	# print("len**", len(laliga_clean["games"]))
	# with open('json/laliga/v3.json', 'w') as outfile:
	# 	json.dump(laliga_clean, outfile)
	return soccer_clean

# get_laliga_games()
