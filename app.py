import os
from pprint import pprint
from datetime import datetime, timezone
from flask import Flask, render_template
from espn_api.nfl_games import get_nfl_games
from espn_api.nba_games import get_nba_games
from espn_api.soccer_games import get_soccer_games
from espn_api.custom_utils import get_est_datetime


from pprint import pprint

app = Flask(__name__)
env_config = os.getenv("PROD_APP_SETTINGS", "config.DevelopmentConfig")
app.config.from_object(env_config)

@app.route("/")
def nfl():
	info = get_nfl_games()
	return render_template("games.html", info=info)

@app.route("/nba")
def nba():
	info = get_nba_games()	
	return render_template("games.html", info=info)

@app.route("/worldcup")
def worldcup():
	WORLDCUP_CODE = "fifa.world"
	_, today_trunc_est_str, _, yest_trunc_est_str = get_est_datetime()	
	yest_games = get_soccer_games(WORLDCUP_CODE, yest_trunc_est_str)
	today_games = get_soccer_games(WORLDCUP_CODE, today_trunc_est_str)

	return render_template(
		"soccer/worldcup/games.html", 
		yest_info=yest_games, 
		today_info=today_games)

if __name__ == "__main__":
	app.run()