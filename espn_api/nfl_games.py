import requests
from espn_api.custom_utils import BASE_ESPN, get_pretty_est, make_wiki_link, get_team_name
# from custom_utils import BASE_ESPN, get_pretty_est
# from espn_api.nfl_leaders import generate_leaders
from pprint import pprint
import json

def get_nfl_games():
	NFL_URL = f"{BASE_ESPN}/football/nfl/scoreboard"
	NFL_TEAMS_URL = f"{BASE_ESPN}/football/nfl/teams"
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
			
			passing_team = passing_leader[0]["leaders"][0]["athlete"]["team"]["id"]
			receiving_team = receiving_leader[0]["leaders"][0]["athlete"]["team"]["id"]	
			rushing_team = rushing_leader[0]["leaders"][0]["athlete"]["team"]["id"]	
			
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
							"data": passing_leader[0]["leaders"][0]["athlete"],
							"wiki": make_wiki_link(passing_leader[0]["leaders"][0]["athlete"]["displayName"]),
							# "team": get_team_name(NFL_TEAMS_URL, passing_team)
						},
						"receiving": {
							"data": receiving_leader[0]["leaders"][0]["athlete"],
							"wiki": make_wiki_link(receiving_leader[0]["leaders"][0]["athlete"]["displayName"]),
							# "team": get_team_name(NFL_TEAMS_URL, receiving_team)						
						},
						"rushing": {
							"data": rushing_leader[0]["leaders"][0]["athlete"],
							"wiki": make_wiki_link(rushing_leader[0]["leaders"][0]["athlete"]["displayName"]),
							# "team": get_team_name(NFL_TEAMS_URL, rushing_team)
						}
					}
			}			
			nfl_clean['games'].append(game)

	# with open('json/nfl_v1.json', 'w') as outfile:
	# 	json.dump(nfl_clean, outfile, indent=2)
	return nfl_clean