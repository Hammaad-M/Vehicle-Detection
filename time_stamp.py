def format_time_unit(unit):
    result = ""
    if unit < 10:
        result += "0" + str(unit)
    else:
        result += str(unit)
    return result

def format_time(hours, minutes, seconds):
    time = ""
    time += format_time_unit(hours)
    time += ":" + format_time_unit(minutes)
    time += ":" + format_time_unit(seconds)
    return time

def get_timestamp(seconds):
    hours = 0;
    minutes = 0
    if seconds >= 60:
        if seconds >= 3600:
            hours = int(seconds / 3600)
            seconds -= hours * 3600
        minutes = int(seconds / 60)
        seconds -= minutes * 60
    return format_time(hours, minutes, seconds)
