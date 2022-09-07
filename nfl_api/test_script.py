import requests
from dateutil.parser import parse
from collections import defaultdict
from pprint import pprint

BASE_ESPN = "https://site.api.espn.com/apis/site/v2/sports/"
NFL_URL = f"{BASE_ESPN}football/nfl/scoreboard"

nfl_data = requests.get(NFL_URL).json()
events = nfl_data['events']

games_dict = defaultdict(list)
for e in events:
  for key, val in e.items():
			if key == "competitions":
				
				for v in val:
					home_teams = v["competitors"][0]		
					away_teams = v["competitors"][1]					

					home_teams_name = home_teams["team"]["displayName"]
					home_teams_score = home_teams["score"]
					home_teams_logo = home_teams["team"]["logo"]			
					away_teams_name = away_teams["team"]["displayName"]
					away_teams_score = away_teams["score"]
					away_teams_logo = away_teams["team"]["logo"]

					stadium = v["venue"]["fullName"]
					raw_unix_date = v["date"]
					python_date_obj = parse(raw_unix_date)
					human_readable_date = python_date_obj.strftime("%A %B %d %Y at %I:%M%p")
					
					game = {
							"home_team": {
								"name": home_teams_name, 
								"score": home_teams_score,
								"logo": home_teams_logo
								},
							"away_team": {
								"name": away_teams_name, 
								"score": away_teams_score,
								"logo": away_teams_logo
								},
							"date": human_readable_date,
							"stadium": stadium,
						}					
					games_dict["games"].append({"game": game})			
# breakpoint()
pprint(games_dict)


					