import requests
from pprint import pprint

BASE_ESPN = "https://site.api.espn.com/apis/site/v2/sports/"
NFL_SCORES = f"{BASE_ESPN}football/nfl/scoreboard"
NFL_TEAMS = f"{BASE_ESPN}football/nfl/teams"

def make_wiki_link(player_name):
	BASE = "https://en.wikipedia.org/wiki/"
	subpath = player_name.replace(" ", "_")
	return BASE + subpath

def get_team_name(team_id):
	# team_id = "3"
	data = requests.get(NFL_TEAMS).json()
	teams = data["sports"][0]["leagues"][0]["teams"]
	for t in teams:
		team_dict = t["team"]
		if team_id in team_dict.values():
			return team_dict["displayName"]

def generate_leaders():
	nfl_data = requests.get(NFL_SCORES).json()
	events = nfl_data['events']
	passers = []
	rushers = []
	receivers = []
	for e in events:
		competitions = e["competitions"]
		for c in competitions:
			leaders = c.get("leaders")
			for l in leaders:
				if l["name"] == "passingYards":
					athlete = l["leaders"][0]["athlete"]
					passers.append({
							"full_name": athlete["fullName"],
							"position": athlete["position"]["abbreviation"],
							"headshot": athlete["headshot"],
							"wiki": make_wiki_link(athlete["fullName"]),
							"team": get_team_name(athlete["team"]["id"])
							})
				elif l["name"] == "rushingYards":
					athlete = l["leaders"][0]["athlete"]
					rushers.append({		
							"full_name": athlete["fullName"],
							"position": athlete["position"]["abbreviation"],
							"headshot": athlete["headshot"],
							"wiki": make_wiki_link(athlete["fullName"]),
							"team": get_team_name(athlete["team"]["id"])
						})
				elif l["name"] == "receivingYards":
					athlete = l["leaders"][0]["athlete"]
					receivers.append({
							"full_name": athlete["fullName"],
							"position": athlete["position"]["abbreviation"],
							"headshot": athlete["headshot"],
							"wiki": make_wiki_link(athlete["fullName"]),
							"team": get_team_name(athlete["team"]["id"])
						})
		
	return passers, rushers, receivers

