soccer_clean = {
		"yesterday": {
			"day": yest_day_pretty, 
			"date": yest_date_pretty
		},
		"today": {
			"day": today_day_pretty, 
			"date": today_date_pretty
		}
	}

	_, yest_day_pretty, yest_date_pretty = get_pretty_est(yesterday_est_str)
	_, today_day_pretty, today_date_pretty = get_pretty_est(today_est_str)	