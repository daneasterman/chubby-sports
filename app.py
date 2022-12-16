import os
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
	return render_template("nfl/base.html", info=info, title="NFL Leaders")

@app.route("/nba")
def nba():
	info = get_nba_games()
	return render_template("nba/base.html", info=info, title="NBA Leaders")

@app.route("/worldcup")
def worldcup():
	WORLDCUP_CODE = "fifa.world"
	semis = get_soccer_games(WORLDCUP_CODE, "20221213-20221216")	
	finals = get_soccer_games(WORLDCUP_CODE, "20221218")
	return render_template("/soccer/worldcup/base.html",
												semis=semis,
												finals=finals,
												title="World Cup Scorers")

@app.route("/laliga")
def laliga():
	LALIGA_CODE = "esp.1"
	info = get_soccer_games(LALIGA_CODE)
	return render_template("soccer/laliga/base.html", 
												info=info, 
												title="La Liga Scorers")

@app.route("/epl")
def epl():
	EPL_CODE = "eng.1"
	info = get_soccer_games(EPL_CODE)
	return render_template("soccer/epl/base.html", 
												info=info, 
												title="Premier League Scorers")

if os.getenv("PROD_APP_SETTINGS"):
	Talisman(app, content_security_policy=None)
else:
	pass

if __name__ == "__main__":
	app.run()