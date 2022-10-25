import requests
from dateutil import parser, tz
from datetime import datetime, timezone

# from nfl_api.leaders import generate_leaders
# from leaders import generate_leaders
from pprint import pprint
import json

BASE_ESPN = "https://site.api.espn.com/apis/site/v2/sports"
EST_TZ = tz.gettz('America/New_York')

def get_current_est_datetime(): 	
	utc_now = datetime.now(tz=timezone.utc)
	est_now = utc_now.astimezone(EST_TZ)		
	est_now_str = est_now.strftime("%Y%m%d")	
	return est_now_str

def get_pretty_est(raw_datestring):
	utc_obj = parser.parse(raw_datestring)			
	usa_eastern_datetime = utc_obj.astimezone(EST_TZ)
	day_pretty = usa_eastern_datetime.strftime("%A")
	date_pretty = usa_eastern_datetime.strftime("%B %d %Y")
	return day_pretty, date_pretty

def get_games():
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
			nba_clean['games'].append(game)

	with open('json/nba_v4.json', 'w') as outfile:
		json.dump(nba_clean, outfile, indent=2)
	# breakpoint()
	return nba_clean

get_games()