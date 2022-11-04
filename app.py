import os
from pprint import pprint
from flask import Flask, render_template
from espn_api.nfl_games import get_nfl_games
from espn_api.nba_games import get_nba_games

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

if __name__ == "__main__":
	app.run()