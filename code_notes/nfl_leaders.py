import requests
from espn_api.custom_utils import BASE_ESPN, get_team_name, make_wiki_link
# from custom_utils import BASE_ESPN, get_team_name, make_wiki_link

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
					# athlete_list.append(athlete)
					passers.append({
							"full_name": athlete.get("fullName"),
							"position": athlete.get("position")["abbreviation"],
							"headshot": athlete.get("headshot"),
							"wiki": make_wiki_link(athlete.get("fullName")),
							"team": get_team_name(NFL_TEAMS_URL, athlete.get("team")["id"])
							})
				elif l["name"] == "rushingYards":
					athlete = l["leaders"][0]["athlete"]
					rushers.append({		
							"full_name": athlete.get("fullName"),
							"position": athlete.get("position")["abbreviation"],
							"headshot": athlete.get("headshot"),
							"wiki": make_wiki_link(athlete.get("fullName")),
							"team": get_team_name(NFL_TEAMS_URL, athlete.get("team")["id"])
						})
				elif l["name"] == "receivingYards":
					athlete = l["leaders"][0]["athlete"]
					receivers.append({
							"full_name": athlete.get("fullName"),
							"position": athlete.get("position")["abbreviation"],
							"headshot": athlete.get("headshot"),
							"wiki": make_wiki_link(athlete.get("fullName")),
							"team": get_team_name(NFL_TEAMS_URL, athlete.get("team")["id"])
						})
	
	# with open('json/nfl_leaders/receivers.json', 'w') as outfile:
	# 	json.dump(receivers, outfile)
	return passers, rushers, receivers

# generate_leaders()