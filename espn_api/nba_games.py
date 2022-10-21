import requests
from dateutil import parser, tz
from nfl_api.leaders import generate_leaders
# from leaders import generate_leaders
from pprint import pprint
import json

BASE_ESPN = "https://site.api.espn.com/apis/site/v2/sports/"
NFL_URL = f"{BASE_ESPN}football/nfl/scoreboard"
LALIGA_URL = f"{BASE_ESPN}soccer/esp.1/scoreboard"

def get_games():
	nfl_raw = requests.get(NFL_URL).json()
	events = nfl_raw['events']
	week = nfl_raw["week"]["number"]
	nfl_clean = {"week": week}
	
	nfl_clean['games'] = []	
	for e in events:
		competitions = e["competitions"]
		for c in competitions:
			home_team = c["competitors"][0]
			away_team = c["competitors"][1]
			
			raw_datestring = c["date"]
			utc_obj = parser.parse(raw_datestring)
			usa_eastern_timezone = tz.gettz('America/New_York')
			usa_eastern_datetime = utc_obj.astimezone(usa_eastern_timezone)
			day_pretty = usa_eastern_datetime.strftime("%A")
			date_pretty = usa_eastern_datetime.strftime("%B %d %Y")
			
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
					"day": day_pretty,
					"date": date_pretty,
					"stadium": c["venue"]["fullName"],					
			}			
			nfl_clean['games'].append(game)

	# with open('json/games_v8.json', 'w') as outfile:
	# 	json.dump(nfl_clean, outfile, indent=2)
	return nfl_clean

# get_games()