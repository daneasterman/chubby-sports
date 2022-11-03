# elif l["name"] == "assistsPerGame":
# 		athlete = l["leaders"][0]["athlete"]
# 		assists.append({
# 				"full_name": athlete["fullName"],
# 				"position": athlete["position"]["abbreviation"],
# 				"headshot": athlete["headshot"],
# 				"wiki": make_wiki_link(athlete["fullName"]),
# 				"team": get_team_name(NBA_TEAMS_URL, athlete["team"]["id"])
# 			})					
# elif l["name"] == "reboundsPerGame":
# 	athlete = l["leaders"][0]["athlete"]
# 	rebounds.append({
# 			"full_name": athlete["fullName"],
# 			"position": athlete["position"]["abbreviation"],
# 			"headshot": athlete["headshot"],
# 			"wiki": make_wiki_link(athlete["fullName"]),
# 			"team": get_team_name(NBA_TEAMS_URL, athlete["team"]["id"])
# 		})