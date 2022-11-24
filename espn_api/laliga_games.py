import requests
# from espn_api.custom_utils import BASE_ESPN, get_pretty_est, make_wiki_link, get_team_name
from custom_utils import BASE_ESPN, get_pretty_est, make_wiki_link, get_team_name
from pprint import pprint

def get_laliga_games():
	LALIGA_URL = f"{BASE_ESPN}/soccer/ESP.1/scoreboard"	
	laliga_raw = requests.get(LALIGA_URL).json()
	events = laliga_raw['events']	
	
	laliga_clean = {}
	laliga_clean['games'] = []	
	
	for e in events:
		competitions = e["competitions"]		
		for comp in competitions:
			home_team = comp["competitors"][0]
			away_team = comp["competitors"][1]
			time_pretty, day_pretty, date_pretty = get_pretty_est(comp["date"])		
			details = comp.get("details")
			
		
get_laliga_games()
