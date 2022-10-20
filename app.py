import os
from pprint import pprint
from flask import Flask, render_template
from espn_api.games import get_games
from pprint import pprint

app = Flask(__name__)
env_config = os.getenv("PROD_APP_SETTINGS", "config.DevelopmentConfig")
app.config.from_object(env_config)

@app.route("/")
def home():
	nfl = get_games()	
	return render_template("nfl.html", nfl=nfl)

# insert generic sport here.
# instantiate the sport class

if __name__ == "__main__":
	app.run()