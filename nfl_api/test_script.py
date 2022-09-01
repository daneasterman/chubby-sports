import requests
from dateutil.parser import parse
from collections import defaultdict
from pprint import pprint

BASE_ESPN = "https://site.api.espn.com/apis/site/v2/sports/"
NFL_URL = f"{BASE_ESPN}football/nfl/scoreboard"

nfl_data = requests.get(NFL_URL).json()
events = nfl_data['events']

for e in events:
  for key, val in e.items():
			if key == "competitions":
				for v in val:
					home_teams = v["competitors"][0]["team"]["displayName"]
					print("HOME TEAMS", home_teams)
					away_teams = v["competitors"][1]["team"]["displayName"]
					print(("AWAY TEAMS", home_teams))					

