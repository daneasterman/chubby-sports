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
			leaders = c["leaders"]

			home_team_name = home_team["team"]["displayName"]
			home_team_score = home_team["score"]
			away_team_name = away_team["team"]["displayName"]
			away_team_score = away_team["score"]
			
			stadium = c["venue"]["fullName"]
			raw_unix_date = c["date"]
			python_date_obj = parse(raw_unix_date)
			human_readable_date = python_date_obj.strftime("%A %B %d %Y at %I:%M%p")		
			
			games_dict = defaultdict(list)
			game = {
					"home_team": {"name": home_team_name, "score": home_team_score},
					"away_team": {"name": away_team_name, "score": away_team_score},
					"date": human_readable_date,
					"stadium": stadium,
				}
			games_dict["games"].append({"game": game})
			
	return games_dict, home_team, away_team, leaders

def get_game_leaders():
	games_dict, home_team, away_team, leaders = get_game_data()
	if home_team.get("leaders"):
		# To do: add code which extracts team-specific leader info here before game starts
		pass
	else:
		passing_yards = [pl_dict for pl_dict in leaders if pl_dict["name"] == "passingYards"]		
		rushing_yards = [pl_dict for pl_dict in leaders if pl_dict["name"] == "rushingYards"]
		receiving_yards = [pl_dict for pl_dict in leaders if pl_dict["name"] == "receivingYards"]
		
		for passer in passing_yards:
			for p in passer["leaders"]:
				passing_leader = {
					"full_name": p["athlete"]["fullName"],
					"position": p["athlete"]["position"]["abbreviation"],
					"headshot": p["athlete"]["headshot"],
				}
				for g in games_dict["games"]:
					g["game"].update({"passing_leader": passing_leader})		
		
		for rusher in rushing_yards:			
			for r in rusher["leaders"]:
				rushing_leader = {
					"full_name": r["athlete"]["fullName"],
					"position": r["athlete"]["position"]["abbreviation"],
					"headshot": r["athlete"]["headshot"],
				}				
				for g in games_dict["games"]:
					g["game"].update({"rushing_leader": rushing_leader})
		
		for receiver in receiving_yards:			
			for r in receiver["leaders"]:
				receiving_leader = {
					"full_name": r["athlete"]["fullName"],
					"position": r["athlete"]["position"]["abbreviation"],
					"headshot": r["athlete"]["headshot"],
				}				
				for g in games_dict["games"]:
					g["game"].update({"receiving_leader": receiving_leader})

	# breakpoint()
	return games_dict["games"]
get_game_leaders()

# example usage in Python interpreter:
# games = games_dict["games"]
# for g in games:
# 	print(g["game"]["home_team"])