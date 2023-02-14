import requests
from espn_api.custom_utils import *
# from custom_utils import *

def get_soccer_games(LEAGUE_CODE, uri_date=""):	
	COMP_URL = f"{BASE_ESPN}/soccer/{LEAGUE_CODE}/scoreboard?dates={uri_date}"
	soccer_raw = requests.get(COMP_URL).json()
	events = soccer_raw['events']	
	
	soccer_clean = {}
	soccer_clean['games'] = []
	for e in events: 
		competitions = e["competitions"]
		for comp in competitions:
			home_team = comp["competitors"][0]
			away_team = comp["competitors"][1]
			time_pretty, day_pretty, date_pretty = get_pretty_custom(comp["date"])		
			details = comp.get("details")
			goals, penalties = get_soccer_scorers(details)			

			game = {
				"home_team": {
					"name": home_team["team"]["displayName"],
					"score": home_team["score"],
					"logo": home_team["team"]["logo"],					
				},
				"away_team": {
					"name": away_team["team"]["displayName"],
					"score": away_team["score"],
					"logo":  away_team["team"]["logo"],					
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

	
	# print("len**", len(laliga_clean["games"]))
	# with open('json/laliga/v3.json', 'w') as outfile:
	# 	json.dump(laliga_clean, outfile)
	# breakpoint()
	return soccer_clean

# get_laliga_games()
