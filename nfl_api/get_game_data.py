import requests
from dateutil.parser import parse
from collections import defaultdict
from pprint import pprint

BASE_ESPN = "https://site.api.espn.com/apis/site/v2/sports/"
NFL_URL = f"{BASE_ESPN}football/nfl/scoreboard"
LALIGA_URL = f"{BASE_ESPN}soccer/esp.1/scoreboard"

def get_game_data():
	nfl_data = requests.get(NFL_URL).json()
	events = nfl_data['events']
	
	for e in events:
		competitions = e["competitions"]		
		for c in competitions:
			home_team = c["competitors"][0]
			away_team = c["competitors"][1]			
			leaders = c.get("leaders")

			home_team_name = home_team["team"]["displayName"]
			home_team_score = home_team["score"]
			home_team_logo = home_team["team"]["logo"]			
			away_team_name = away_team["team"]["displayName"]
			away_team_score = away_team["score"]
			away_team_logo = away_team["team"]["logo"]
			
			stadium = c["venue"]["fullName"]
			raw_unix_date = c["date"]
			python_date_obj = parse(raw_unix_date)
			human_readable_date = python_date_obj.strftime("%A %B %d %Y at %I:%M%p")
					
			games_dict = defaultdict(list)
			game = {
					"home_team": {
						"name": home_team_name, 
						"score": home_team_score,
						"logo": home_team_logo
						},
					"away_team": {
						"name": away_team_name, 
						"score": away_team_score,
						"logo": away_team_logo
						},
					"date": human_readable_date,
					"stadium": stadium,
				}
			# breakpoint()
			games_dict["games"].append({"game": game})
	breakpoint()
	return games_dict, home_team, away_team, leaders

get_game_data()
