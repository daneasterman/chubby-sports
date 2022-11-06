import requests
from dateutil import parser, tz
from datetime import datetime, timezone
from espn_api.custom_utils import BASE_ESPN, get_pretty_est, get_current_est_datetime, make_wiki_link
# from custom_utils import BASE_ESPN, get_pretty_est, get_current_est_datetime, make_wiki_link
from pprint import pprint
import json

def get_nba_games():
	full_est_now, trunc_est_now = get_current_est_datetime()	
	NBA_URL = f"{BASE_ESPN}/basketball/nba/scoreboard?dates={trunc_est_now}"	
	nba_raw = requests.get(NBA_URL).json()
	events = nba_raw['events']
	
	time_pretty, day_pretty, date_pretty = get_pretty_est(full_est_now)		
	nba_clean = {"day": day_pretty, "date": date_pretty }
	
	nba_clean['games'] = []
	for e in events:
		competitions = e["competitions"]
		for c in competitions:
			home_team = c["competitors"][0]
			away_team = c["competitors"][1]
			time_pretty, day_pretty, date_pretty = get_pretty_est(c["date"])		

			home_leaders = home_team["leaders"]
			away_leaders = away_team["leaders"]
			
			home_points_leader = [h for h in home_leaders if h["name"] == 'pointsPerGame']			
			home_assists_leader = [h for h in home_leaders if h["name"] == 'assistsPerGame']
			home_rebounds_leader = [h for h in home_leaders if h["name"] == 'reboundsPerGame']	

			away_points_leader = [a for a in away_leaders if a["name"] == 'pointsPerGame']			
			away_assists_leader = [a for a in away_leaders if a["name"] == 'assistsPerGame']
			away_rebounds_leader = [a for a in away_leaders if a["name"] == 'reboundsPerGame']

			game = {
					"home_team": {
						"name": home_team["team"]["displayName"],
						"score": home_team["score"],
						"logo": home_team["team"]["logo"],
						"record": home_team["records"][0]["summary"],						
						"leaders": {
							"points": {
								"data": home_points_leader[0]["leaders"][0]["athlete"],
								"wiki": make_wiki_link(home_points_leader[0]["leaders"][0]["athlete"]["displayName"])
							},
							"assists": {
								"data": home_assists_leader[0]["leaders"][0]["athlete"],
								"wiki": make_wiki_link(home_assists_leader[0]["leaders"][0]["athlete"]["displayName"])
							},
							"rebounds": {
								"data": home_rebounds_leader[0]["leaders"][0]["athlete"],
								"wiki": make_wiki_link(home_rebounds_leader[0]["leaders"][0]["athlete"]["displayName"])
							}
						},
					},					
					"away_team": {
						"name": away_team["team"]["displayName"],
						"score": away_team["score"],
						"logo":  away_team["team"]["logo"],
						"record": away_team["records"][0]["summary"],
						"leaders": {
							"points": {
								"data": away_points_leader[0]["leaders"][0]["athlete"],
								"wiki": make_wiki_link(away_points_leader[0]["leaders"][0]["athlete"]["displayName"])
							},
							"assists": {
								"data": away_assists_leader[0]["leaders"][0]["athlete"],
								"wiki": make_wiki_link(away_assists_leader[0]["leaders"][0]["athlete"]["displayName"])
							},
							"rebounds": {
								"data": away_rebounds_leader[0]["leaders"][0]["athlete"],
								"wiki": make_wiki_link(away_rebounds_leader[0]["leaders"][0]["athlete"]["displayName"])
							}
						},
						},
					"time": time_pretty,
					"stadium": c["venue"]["fullName"],
					"city": c["venue"]["address"]["city"]
			}
			nba_clean['games'].append(game)

	# with open('json/nba_games/all_leaders_v2.json', 'w') as outfile:
	# 	json.dump(nba_clean, outfile)
	# breakpoint()
	return nba_clean

# get_nba_games()