import requests
from pprint import pprint

BASE_ESPN = "https://site.api.espn.com/apis/site/v2/sports/"
NFL_URL = f"{BASE_ESPN}football/nfl/scoreboard"

def make_wiki_link(player_name):
	BASE = "https://en.wikipedia.org/wiki/"
	subpath = player_name.replace(" ", "_")
	return BASE + subpath

def generate_leaders():
	nfl_data = requests.get(NFL_URL).json()
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
					make_wiki_link(athlete["fullName"])					
					passers.append({
							"full_name": athlete["fullName"],
							"position": athlete["position"]["abbreviation"],
							"headshot": athlete["headshot"],
							"wiki": make_wiki_link(athlete["fullName"])
							})
				elif l["name"] == "rushingYards":
					athlete = l["leaders"][0]["athlete"]
					rushers.append({		
							"full_name": athlete["fullName"],
							"position": athlete["position"]["abbreviation"],
							"headshot": athlete["headshot"],
							"wiki": make_wiki_link(athlete["fullName"])				
						})
				elif l["name"] == "receivingYards":
					athlete = l["leaders"][0]["athlete"]
					receivers.append({
							"full_name": athlete["fullName"],
							"position": athlete["position"]["abbreviation"],
							"headshot": athlete["headshot"],
							"wiki": make_wiki_link(athlete["fullName"])						
						})
	
	return passers, rushers, receivers

