import os
from pprint import pprint
from datetime import datetime, timezone
from flask import Flask, render_template
from espn_api.nfl_games import get_nfl_games
from espn_api.nba_games import get_nba_games
from espn_api.soccer_games import get_soccer_games
from espn_api.custom_utils import get_est_datetime
from flask_talisman import Talisman

from pprint import pprint

app = Flask(__name__)
env_config = os.getenv("PROD_APP_SETTINGS", "config.DevelopmentConfig")
app.config.from_object(env_config)

@app.route("/")
def nfl():
	info = get_nfl_games()
	return render_template("games.html", info=info, title="NFL Leaders")

@app.route("/nba")
def nba():
	info = get_nba_games()
	return render_template("games.html", info=info, title="NBA Leaders")

@app.route("/worldcup")
def worldcup():
	WORLDCUP_CODE = "fifa.world"
	date_range = "20221210-20221216"
	games = get_soccer_games(WORLDCUP_CODE, date_range)
	
	return render_template(
		"soccer/worldcup/games.html", 
		info=games,
		title="World Cup Scorers")


if os.getenv("PROD_APP_SETTINGS"):
	Talisman(app, content_security_policy=None)
else:
	pass

if __name__ == "__main__":
	app.run()