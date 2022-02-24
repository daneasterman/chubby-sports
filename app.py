from flask import Flask, render_template
from nfl_api.get_game_leaders import get_game_leaders

app = Flask(__name__)

@app.route("/")
def indext():
	games = get_game_leaders()
	breakpoint()
	return render_template("index.html", count=5)


if __name__ == "__main__":
	app.run()