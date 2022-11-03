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
	
	athlete_data = []
	leader_list = []
	for e in events:
		competitions = e["competitions"]
		for c in competitions:	
			competitors = c.get("competitors")
			for c in competitors:				
				leaders = c.get("leaders")
				# breakpoint()
				for l in leaders:
					leader_list.append(l)
					if l["name"] == "pointsPerGame":
						athlete = l["leaders"][0]["athlete"]
						athlete_data.append(athlete)
						# point_leader = {
						# 	"full_name": athlete["fullName"],
						# 	"position": athlete["position"]["abbreviation"],
						# 	"headshot": athlete["headshot"],
						# 	"wiki": make_wiki_link(athlete["fullName"]),
						# 	"team": get_team_name(NBA_TEAMS_URL, athlete["team"]["id"])								
						# }						
						# leader_dict["points"].append(point_leader)
						
	
	with open('json/nba_leaders/competitors.json', 'w') as outfile:
		json.dump(competitors, outfile)	
	# return leader_dict["points"]

get_nba_leaders()