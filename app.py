from pprint import pprint
from flask import Flask, render_template
from nfl_api.games import get_games
from pprint import pprint

app = Flask(__name__)

@app.route("/")
def home():
	games = get_games()
	return render_template("nfl.html", games=games)

if __name__ == "__main__":
	app.run()