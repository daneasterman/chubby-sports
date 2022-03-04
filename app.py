from flask import Flask, render_template
from nfl_api.get_game_leaders import get_game_leaders

app = Flask(__name__)

@app.route("/")
def home():
	games = get_game_leaders()	
	return render_template("nfl.html", games=games)

if __name__ == "__main__":
	app.run()