import requests
# from espn_api.custom_utils import BASE_ESPN, get_team_name, make_wiki_link
from custom_utils import BASE_ESPN, get_team_name, make_wiki_link
from pprint import pprint
import json

NFL_SCORES = f"{BASE_ESPN}/football/nfl/scoreboard"
NFL_TEAMS_URL = f"{BASE_ESPN}/football/nfl/teams"

def generate_leaders():
	nfl_data = requests.get(NFL_SCORES).json()
	events = nfl_data['events']
	passers = []
	rushers = []
	receivers = []
	athlete_list = []
	for e in events:
		competitions = e["competitions"]		
		for c in competitions:
			competitors = c.get("competitors")
			for c in competitors:
				leaders = c.get("leaders")
				for l in leaders:					
					if l["name"] == "passingLeader":						
						athlete = l["leaders"][0]["athlete"]
						athlete_list.append(athlete)

						# passers.append({
						# 		"full_name": athlete["fullName"],
						# 		"position": athlete["position"]["abbreviation"],
						# 		"headshot": athlete["headshot"],
						# 		"wiki": make_wiki_link(athlete["fullName"]),
						# 		"team": get_team_name(NFL_TEAMS_URL, athlete["team"]["id"])
						# 		})
					# elif l["name"] == "rushingLeader":
					# 	athlete = l["leaders"][0]["athlete"]
					# 	rushers.append({		
					# 			"full_name": athlete["fullName"],
					# 			"position": athlete["position"]["abbreviation"],
					# 			"headshot": athlete["headshot"],
					# 			"wiki": make_wiki_link(athlete["fullName"]),
					# 			"team": get_team_name(NFL_TEAMS_URL, athlete["team"]["id"])
					# 		})
					# elif l["name"] == "receivingLeader":
					# 	athlete = l["leaders"][0]["athlete"]
					# 	receivers.append({
					# 			"full_name": athlete["fullName"],
					# 			"position": athlete["position"]["abbreviation"],
					# 			"headshot": athlete["headshot"],
					# 			"wiki": make_wiki_link(athlete["fullName"]),
					# 			"team": get_team_name(NFL_TEAMS_URL, athlete["team"]["id"])
					# 		})
	
	with open('json/nfl_leaders/athlete_list.json', 'w') as outfile:
		json.dump(athlete_list, outfile)
	# return passers, rushers, receivers

generate_leaders()