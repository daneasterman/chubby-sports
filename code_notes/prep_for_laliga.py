@app.route("/laliga")
def laliga():
	info = get_laliga_games()	
	return render_template("games.html", info=info)