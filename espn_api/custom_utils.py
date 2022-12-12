from dateutil import parser, tz
from datetime import datetime, timezone, timedelta

BASE_ESPN = "https://site.api.espn.com/apis/site/v2/sports"
EST_TZ = tz.gettz('America/New_York')

def get_est_datetime(): 	
	today_utc = datetime.now(tz=timezone.utc)
	today_est_datetime = today_utc.astimezone(EST_TZ)
	today_est_str = str(today_utc.astimezone(EST_TZ))
	today_trunc_est_str = today_est_datetime.strftime("%Y%m%d")
	
	return today_est_str, today_trunc_est_str

def get_pretty_est(raw_datestring):
	utc_obj = parser.parse(raw_datestring)			
	usa_eastern_datetime = utc_obj.astimezone(EST_TZ)
	time_pretty = usa_eastern_datetime.strftime("%-H:%M")
	day_pretty = usa_eastern_datetime.strftime("%A")
	date_pretty = usa_eastern_datetime.strftime("%B %d %Y")
	return time_pretty, day_pretty, date_pretty

def make_wiki_link(player_name):
	BASE = "https://en.wikipedia.org/wiki/"
	subpath = player_name.replace(" ", "_")
	return BASE + subpath

def get_nfl_team_name(home_team, away_team, player_data):
	if player_data["team"]["id"] == home_team["team"]["id"]:
		return home_team["team"]["displayName"]
	elif player_data["team"]["id"] == away_team["team"]["id"]:
		return away_team["team"]["displayName"]
	else:
		return ""

def get_soccer_scorers(details):
	goal_scorers = []
	penalty_scorers = []
	for deet in details:		
		if "goal" in deet["type"]["text"].casefold():
			player_name = deet["athletesInvolved"][0]["displayName"]
			goal_scorers.append({
				"name": player_name,
				"position": deet["athletesInvolved"][0]["position"],
				"goal_type": deet["type"]["text"],
				"wiki_link": make_wiki_link(player_name)
			})			
		elif "penalty" in deet["type"]["text"].casefold():
			player_name = deet["athletesInvolved"][0]["displayName"]
			penalty_scorers.append({
				"name": player_name,
				"position": deet["athletesInvolved"][0]["position"],
				"goal_type": deet["type"]["text"],
				"wiki_link": make_wiki_link(player_name)
			})	
	return goal_scorers, penalty_scorers			
