import os
from flask import Flask, render_template
from espn_api.nfl_games import get_nfl_games
from espn_api.nba_games import get_nba_games
from espn_api.soccer_games import get_soccer_games
from espn_api.custom_utils import get_week_range
from flask_talisman import Talisman
from flask_assets import Bundle, Environment
from pprint import pprint

app = Flask(__name__)
env_config = os.getenv("PROD_APP_SETTINGS", "config.DevelopmentConfig")
app.config.from_object(env_config)

css_bundle = Bundle('css/sections/globals.css', 
										'css/sections/page.css',
										'css/sections/game.css',
										'css/sections/player.css',
										filters='cssmin', output='css/styles.css')

assets = Environment(app)
assets.register('main_styles.css', css_bundle)

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
	start_week_str, end_week_str = get_week_range()
	LALIGA_CODE = "esp.1"
	info = get_soccer_games(LALIGA_CODE, f"{start_week_str}-{end_week_str}")
	return render_template("soccer/laliga/base.html", 
												info=info, 
												title="La Liga Scorers")

@app.route("/epl")
def epl():
	start_week_str, end_week_str = get_week_range()
	EPL_CODE = "eng.1"
	info = get_soccer_games(EPL_CODE, f"{start_week_str}-{end_week_str}")
	return render_template("soccer/epl/base.html", 
												info=info, 
												title="English Premier League Scorers")

if os.getenv("PROD_APP_SETTINGS"):
	Talisman(app, content_security_policy=None)
else:
	pass

if __name__ == "__main__":
	app.run()