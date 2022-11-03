import requests
# from espn_api.custom_utils import BASE_ESPN, get_team_name, make_wiki_link, get_current_est_datetime
from custom_utils import BASE_ESPN, get_team_name, make_wiki_link, get_current_est_datetime
from pprint import pprint
import json

est_now = get_current_est_datetime()
NBA_SCORES = f"{BASE_ESPN}/basketball/nba/scoreboard?dates={est_now}"
NBA_TEAMS_URL = f"{BASE_ESPN}/basketball/nba/teams"

def get_nba_leaders():
	nba_data = requests.get(NBA_SCORES).json()
	events = nba_data['events']
	leader_dict = {}
	points_dict = {}
	assists = []
	rebounds = []
	for e in events:		
		competitions = e["competitions"]
		for c in competitions:	
			competitors = c.get("competitors")
			for c in competitors:
				leaders = c.get("leaders")
				# breakpoint()
				for l in leaders:
					if l["name"] == "pointsPerGame":
						athlete = l["leaders"][0]["athlete"]						
						points = {
							"points": {
								"full_name": athlete["fullName"],
								"position": athlete["position"]["abbreviation"],
								"headshot": athlete["headshot"],
								"wiki": make_wiki_link(athlete["fullName"]),
								"team": get_team_name(NBA_TEAMS_URL, athlete["team"]["id"])	
							}
						}						
					elif l["name"] == "assistsPerGame":
						athlete = l["leaders"][0]["athlete"]
						assists.append({
								"full_name": athlete["fullName"],
								"position": athlete["position"]["abbreviation"],
								"headshot": athlete["headshot"],
								"wiki": make_wiki_link(athlete["fullName"]),
								"team": get_team_name(NBA_TEAMS_URL, athlete["team"]["id"])
							})					
					elif l["name"] == "reboundsPerGame":
						athlete = l["leaders"][0]["athlete"]
						rebounds.append({
								"full_name": athlete["fullName"],
								"position": athlete["position"]["abbreviation"],
								"headshot": athlete["headshot"],
								"wiki": make_wiki_link(athlete["fullName"]),
								"team": get_team_name(NBA_TEAMS_URL, athlete["team"]["id"])
							})
					
	
	with open('json/nba_leaders/points_dict_v1.json', 'w') as outfile:
		json.dump(points_dict, outfile, indent=2)	
	# return leader_dict

get_nba_leaders()