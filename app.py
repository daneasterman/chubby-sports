from flask import Flask, render_template
from nfl_api.get_game_data import get_game_data

app = Flask(__name__)

@app.route("/")
def home():
	games_dict = get_game_data()
	return render_template("nfl.html", games=games_dict["games"])

if __name__ == "__main__":
	app.run()