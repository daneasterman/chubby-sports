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