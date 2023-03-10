from pprint import pprint
from nfl_api.games import get_game_data

def get_games_and_leaders():
	games_dict, leaders = get_game_data()
	if leaders is None:
		pass
	else:
		passing_yards = [pl_dict for pl_dict in leaders if pl_dict["name"] == "passingYards"]		
		rushing_yards = [pl_dict for pl_dict in leaders if pl_dict["name"] == "rushingYards"]
		receiving_yards = [pl_dict for pl_dict in leaders if pl_dict["name"] == "receivingYards"]		
		
		for passer in passing_yards:
			for p in passer["leaders"]:
				passing_leader = {
					"full_name": p["athlete"]["fullName"],
					"position": p["athlete"]["position"]["abbreviation"],
					"headshot": p["athlete"]["headshot"],
				}
				for g in games_dict["games"]:
					g["game"].update({"passing_leader": passing_leader})		
		
		for rusher in rushing_yards:
			for r in rusher["leaders"]:
				rushing_leader = {
					"full_name": r["athlete"]["fullName"],
					"position": r["athlete"]["position"]["abbreviation"],
					"headshot": r["athlete"]["headshot"],
				}				
				for g in games_dict["games"]:
					g["game"].update({"rushing_leader": rushing_leader})
		
		for receiver in receiving_yards:			
			for r in receiver["leaders"]:
				receiving_leader = {
					"full_name": r["athlete"]["fullName"],
					"position": r["athlete"]["position"]["abbreviation"],
					"headshot": r["athlete"]["headshot"],
				}				
				for g in games_dict["games"]:
					g["game"].update({"receiving_leader": receiving_leader})
	games = games_dict["games"]
	breakpoint()
	return games_dict["games"]

get_games_and_leaders()


# example usage in Python interpreter:
# games = games_dict["games"]
# for g in games:
# 	print(g["game"]["home_team"])