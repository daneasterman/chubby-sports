import requests
from dateutil import parser, tz
from datetime import datetime, timezone

BASE_ESPN = "https://site.api.espn.com/apis/site/v2/sports"
EST_TZ = tz.gettz('America/New_York')

def get_current_est_datetime(): 	
	utc_now = datetime.now(tz=timezone.utc)
	est_now = utc_now.astimezone(EST_TZ)		
	est_now_str = est_now.strftime("%Y%m%d")	
	return est_now_str

def get_pretty_est(raw_datestring):
	utc_obj = parser.parse(raw_datestring)			
	usa_eastern_datetime = utc_obj.astimezone(EST_TZ)
	day_pretty = usa_eastern_datetime.strftime("%A")
	date_pretty = usa_eastern_datetime.strftime("%B %d %Y")
	return day_pretty, date_pretty


def make_wiki_link(player_name):
	BASE = "https://en.wikipedia.org/wiki/"
	subpath = player_name.replace(" ", "_")
	return BASE + subpath

def get_team_name(uri, team_id):	
	data = requests.get(uri).json()
	teams = data["sports"][0]["leagues"][0]["teams"]
	for t in teams:
		team_dict = t["team"]
		if team_id in team_dict.values():
			return team_dict["displayName"]

