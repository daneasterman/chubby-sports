import os
from pprint import pprint
from flask import Flask, render_template
from espn_api.nfl_games import get_nfl_games
from espn_api.nba_games import get_nba_games
from espn_api.nba_leaders import get_nba_leaders

from pprint import pprint

app = Flask(__name__)
env_config = os.getenv("PROD_APP_SETTINGS", "config.DevelopmentConfig")
app.config.from_object(env_config)

@app.route("/")
def nfl():
	data = get_nfl_games()
	return render_template("games.html", data=data)

@app.route("/nba")
def nba():
	data = get_nba_games()
	leaders = get_nba_leaders()
	return render_template("games.html", data=data, leaders=leaders)

if __name__ == "__main__":
	app.run()