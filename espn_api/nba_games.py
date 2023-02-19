import requests
import json
from dateutil import parser, tz
from datetime import datetime, timezone
from espn_api.custom_utils import *
# from custom_utils import *
from pprint import pprint

def get_nba_games():
	today_custom_str, today_trunc_custom_str = get_est_datetime()
	NBA_URL = f"{BASE_ESPN}/basketball/nba/scoreboard?dates={today_trunc_custom_str}"	
	nba_raw = requests.get(NBA_URL).json()
	events = nba_raw['events']
	
	LONDON = tz.gettz('Europe/London')
	NEW_YORK = tz.gettz('America/New_York')		
	_, day_pretty, date_pretty = get_pretty_custom(today_custom_str, LONDON)	
	nba_clean = {"day": day_pretty, "date": date_pretty}
	
	nba_clean['games'] = []
	for e in events:
		competitions = e["competitions"]
		for c in competitions:
			home_team = c["competitors"][0]
			away_team = c["competitors"][1]
			try: 
				home_leaders = home_team.get("leaders")
				away_leaders = away_team.get("leaders")
				
				home_points_leader = [h for h in home_leaders if h.get("name") == 'pointsPerGame']			
				home_assists_leader = [h for h in home_leaders if h.get("name") == 'assistsPerGame']
				home_rebounds_leader = [h for h in home_leaders if h.get("name") == 'reboundsPerGame']	

				away_points_leader = [a for a in away_leaders if a.get("name") == 'pointsPerGame']			
				away_assists_leader = [a for a in away_leaders if a.get("name") == 'assistsPerGame']
				away_rebounds_leader = [a for a in away_leaders if a.get("name") == 'reboundsPerGame']					
			except:
				pass
			
			uk_pretty_time, _, _ = get_pretty_custom(c["date"], LONDON)
			est_pretty_time, _, _ = get_pretty_custom(c["date"], NEW_YORK)

			# a if condition else b
			try:
				game = {
						"home_team": {
							"name": home_team["team"]["displayName"],
							"score": home_team["score"],
							"logo": home_team["team"]["logo"],
							"record": home_team.get("records")[0].get("summary"),
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
						"uk_time": uk_pretty_time,
						"est_time": est_pretty_time,					
						"stadium": c["venue"]["fullName"],
						"city": c["venue"]["address"]["city"]
					}
				nba_clean['games'].append(game)
			except:
				pass
				
			

	# with open('test_v1.json', 'w') as outfile:
	# 	json.dump(nba_clean, outfile, indent=2)
	# breakpoint()
	return nba_clean

# get_nba_games()