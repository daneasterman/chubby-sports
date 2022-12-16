@app.route("/epl")
def epl():
	EPL_CODE = "eng.1"
	info = get_soccer_games(EPL_CODE)
	return render_template("soccer/epl/base.html", 
												info=info, 
												title="Premier League Scorers")