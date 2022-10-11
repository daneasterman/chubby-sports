local_zone = tz.tzlocal()
tz_aware_obj = utc_obj.astimezone(local_zone)
time_pretty = tz_aware_obj.strftime("%H:%M")