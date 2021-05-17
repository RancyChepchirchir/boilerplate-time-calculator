
def add_time(start_time, duration, week_day = False):

    days_week = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    days_week_C = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    in_time = start_time.split()[0]
    am_pm = start_time.split()[1]

    in_hour = in_time.split(":")[0]         #initial hour
    in_min = in_time.split(":")[1]          #initial minutes
    dur_hour = duration.split(":")[0]       #hours to add
    dur_min = duration.split(":")[1]        #minutes to add

    new_hour = int(in_hour) + int(dur_hour)     #add hours
    new_min = int(in_min) + int(dur_min)        #add minutes

    extra_hours = 0                             #hours to add after converting minutes
    while new_min > 60:                         #subtracting each hour from the minutes
        new_min = new_min - 60
        extra_hours += 1                        #summing up the extra hours

    if new_min < 10:
        new_min = str(new_min).zfill(2)

    new_hour = new_hour + extra_hours           #adding the extra hours to the hours

    div_days = divmod(new_hour, 12)             # calculates how many half days (12 hours) there are
    half_days = div_days[0]                     #how many groups of 12 hours there are
    hour = div_days[1]                         #how many hours after subtracting 12

    full_days = half_days//2                     #number of days

    if half_days % 2 == 0:                      #if the groups of 12 hours are even then ampm doesn't change
        new_am_pm = am_pm
    else:
        if am_pm == "AM":                       #if thet are odd then switch the ampm
            new_am_pm = "PM"
        else:
            new_am_pm = "AM"

    msg = ""                                    #message will indicate number of days of difference
    if 4 > half_days >= 2:
        msg = "(next day)"
    elif half_days >= 4:
        msg = "(" + str(full_days) + " days later" + ")"

    x = ""
    if week_day:
        x = days_week.index(week_day.lower())
        y = (x + full_days) % 7
        new_day = days_week_C[y]
        final_time = str(hour) + ":" + str(new_min) + " " + new_am_pm + "," + " " + new_day + " " + msg
        return final_time
    else:
        final_time = str(hour) + ":" + str(new_min) + " " + new_am_pm + " " + msg
        return final_time
