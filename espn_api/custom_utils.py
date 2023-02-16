from dateutil import parser, tz
from datetime import datetime, timezone, timedelta

BASE_ESPN = "https://site.api.espn.com/apis/site/v2/sports"
# CUSTOM_TZ = tz.gettz('America/New_York')
CUSTOM_TZ = tz.gettz('Europe/London')

def get_est_datetime():
	today_utc_obj = datetime.now(tz=timezone.utc)
	today_custom_obj = today_utc_obj.astimezone(CUSTOM_TZ)
	today_custom_str = str(today_utc_obj.astimezone(CUSTOM_TZ))	
	today_trunc_custom_str = today_custom_obj.strftime("%Y%m%d")
	return today_custom_str, today_trunc_custom_str

def get_pretty_custom(raw_datestring, timezone):
	utc_obj = parser.parse(raw_datestring)
	custom_datetime = utc_obj.astimezone(timezone)
	time_pretty = custom_datetime.strftime("%-H:%M")
	day_pretty = custom_datetime.strftime("%A")
	date_pretty = custom_datetime.strftime("%B %d %Y")
	return time_pretty, day_pretty, date_pretty

def get_week_range():
	current_date = datetime.now()
	start_week_obj = current_date - timedelta(days=current_date.weekday())
	end_week_obj = start_week_obj + timedelta(days=6)
	start_week_str = start_week_obj.strftime("%Y%m%d")
	end_week_str = end_week_obj.strftime("%Y%m%d")
	return start_week_str, end_week_str

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
