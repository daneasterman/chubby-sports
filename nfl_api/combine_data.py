from pprint import pprint
import json
from get_game_data import get_game_data

games_dict, leader_list = get_game_data()

games_list = []
for l in leader_list:
	for g in games_dict["games"]:
		g["game"].update({"leader": l})

# pprint(games_dict)
# breakpoint()

with open('json/test1.json', 'w') as outfile:
	json.dump(games_dict, outfile)
