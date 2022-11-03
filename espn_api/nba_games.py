import requests
from dateutil import parser, tz
from datetime import datetime, timezone
# from espn_api.custom_utils import BASE_ESPN, get_pretty_est, get_current_est_datetime
from custom_utils import BASE_ESPN, get_pretty_est, get_current_est_datetime
from nba_leaders import get_nba_leaders
# from espn_api.nba_leaders import get_nba_leaders

from pprint import pprint
import json

def get_nba_games():
	est_now = get_current_est_datetime()
	NBA_URL = f"{BASE_ESPN}/basketball/nba/scoreboard?dates={est_now}"	
	nba_raw = requests.get(NBA_URL).json()
	events = nba_raw['events']		
		
	nba_clean = {}
	nba_clean['games'] = []
	for e in events:
		competitions = e["competitions"]
		for c in competitions:
			home_team = c["competitors"][0]
			away_team = c["competitors"][1]			
			day_pretty, date_pretty = get_pretty_est(c["date"])

			home_leaders = home_team.get("leaders")
			pl_parent = [l for l in home_leaders if l["name"] == 'pointsPerGame']
			points_leader = pl_parent[0]["leaders"][0]["athlete"]
			

			game = {
					"home_team": {
						"name": home_team["team"]["displayName"],
						"score": home_team["score"],
						"logo": home_team["team"]["logo"],
						"record": home_team["records"][0]["summary"],						
						"leaders": {
							"points": {
							"name": points_leader["fullName"]
							}
						},
					},					
					"away_team": {
						"name": away_team["team"]["displayName"],
						"score": away_team["score"],
						"logo":  away_team["team"]["logo"],
						"record": away_team["records"][0]["summary"]
						},					
					"day": day_pretty,
					"date": date_pretty,
					"stadium": c["venue"]["fullName"],
			}
			nba_clean['games'].append(game)

	with open('json/nba_games/nba_v6.json', 'w') as outfile:
		json.dump(nba_clean, outfile, indent=2)
	# breakpoint()
	# return nba_clean

get_nba_games()