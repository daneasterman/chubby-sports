import requests
from espn_api.custom_utils import BASE_ESPN, get_team_name, make_wiki_link
from pprint import pprint

NFL_SCORES = f"{BASE_ESPN}/football/nfl/scoreboard"
NFL_TEAMS_URL = f"{BASE_ESPN}/football/nfl/teams"

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
							"team": get_team_name(NFL_TEAMS_URL, athlete["team"]["id"])
							})
				elif l["name"] == "rushingYards":
					athlete = l["leaders"][0]["athlete"]
					rushers.append({		
							"full_name": athlete["fullName"],
							"position": athlete["position"]["abbreviation"],
							"headshot": athlete["headshot"],
							"wiki": make_wiki_link(athlete["fullName"]),
							"team": get_team_name(NFL_TEAMS_URL, athlete["team"]["id"])
						})
				elif l["name"] == "receivingYards":
					athlete = l["leaders"][0]["athlete"]
					receivers.append({
							"full_name": athlete["fullName"],
							"position": athlete["position"]["abbreviation"],
							"headshot": athlete["headshot"],
							"wiki": make_wiki_link(athlete["fullName"]),
							"team": get_team_name(NFL_TEAMS_URL, athlete["team"]["id"])
						})
		
	return passers, rushers, receivers

