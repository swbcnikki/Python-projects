# timedelta does not have a strf
def timeformat(milisecs):
    total_seconds = int(milisecs/1000)
    hours, remainder = divmod(total_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    if hours:
        string = '{}:{:02d}:{:02d}'.format(hours, minutes, seconds)
    else:
        string = '{:02d}:{:02d}'.format(minutes, seconds)
    return string