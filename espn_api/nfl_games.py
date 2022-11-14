import requests
from espn_api.custom_utils import BASE_ESPN, get_pretty_est, make_wiki_link
# from custom_utils import BASE_ESPN, get_pretty_est
# from espn_api.nfl_leaders import generate_leaders
from pprint import pprint
import json

def get_team_name(home_team, away_team, player_team_id):
	if player_team_id == home_team["team"]["id"]:
		return home_team["team"]["displayName"]
	elif player_team_id == away_team["team"]["id"]:
		return away_team["team"]["displayName"]
	else:
		return ""

def get_nfl_games():
	NFL_URL = f"{BASE_ESPN}/football/nfl/scoreboard"	
	
	nfl_raw = requests.get(NFL_URL).json()
	events = nfl_raw['events']
	week = nfl_raw["week"]["number"]
	nfl_clean = {"week": week}
	
	nfl_clean['games'] = []	
	for e in events:
		competitions = e["competitions"]
		for c in competitions:
			home_team = c["competitors"][0]
			away_team = c["competitors"][1]
			
			time_pretty, day_pretty, date_pretty = get_pretty_est(c["date"])
			
			leaders = c.get("leaders")
			passing_leader = [l for l in leaders if l["name"] == 'passingYards']
			receiving_leader = [l for l in leaders if l["name"] == 'receivingYards']
			rushing_leader = [l for l in leaders if l["name"] == 'rushingYards']

			passing_data = passing_leader[0]["leaders"][0]["athlete"]
			receiving_data = receiving_leader[0]["leaders"][0]["athlete"]
			rushing_data = rushing_leader[0]["leaders"][0]["athlete"]
			
			game = {
					"home_team": {
						"name": home_team["team"]["displayName"],
						"score": home_team["score"],
						"logo": home_team["team"]["logo"],
						"record": home_team["records"][0]["summary"]
						},
					"away_team": {
						"name": away_team["team"]["displayName"],
						"score": away_team["score"],
						"logo":  away_team["team"]["logo"],
						"record": away_team["records"][0]["summary"]
						},
					"time": time_pretty,
					"day": day_pretty,
					"date": date_pretty,
					"stadium": c["venue"]["fullName"],
					"city": c["venue"]["address"]["city"],
					"leaders": {
						"passing": {
							"data": passing_data,
							"wiki": make_wiki_link(passing_data["displayName"]),
							"team": get_team_name(home_team, away_team, passing_data.get("team")["id"])
						},
						"receiving": {
							"data": receiving_data,
							"wiki": make_wiki_link(receiving_data["displayName"]),
							"team": get_team_name(home_team, away_team, receiving_data.get("team")["id"])									
						},
						"rushing": {
							"data": rushing_data,
							"wiki": make_wiki_link(rushing_data["displayName"]),
							"team": get_team_name(home_team, away_team, rushing_data.get("team")["id"])
						}
					}
			}			
			nfl_clean['games'].append(game)

	# with open('json/nfl_v1.json', 'w') as outfile:
	# 	json.dump(nfl_clean, outfile, indent=2)
	return nfl_clean