from datetime import datetime, date

#1  # Get the current day, month, year, hour, minute and timestamp from datetime module
now = datetime.now()
d = now.day
mth = now.month
y = now.year
h = now.hour
m = now.minute
s = now.second
print(now)
print(f"{d}/{mth}/{y}, {h}:{m}, {now.timestamp()}")

#2  # Format the current date using this format: "%m/%d/%Y, %H:%M:%S")
formatted_now = now.strftime("%m/%d/%Y, %H:%M:%S")
print(formatted_now)

#3  # Today is 5 December, 2019. Change this time string to time.
time_string = "Today is 5 December, 2019."
date_part = time_string.replace("Today is ", "").replace(".", "").strip()
date_part = date_part.replace(",", "")
dt_parsed = datetime.strptime(date_part, "%d %B %Y")
print("Parsed datetime:", dt_parsed)

#4  # Calculate the time difference between now and new year.
today = date(year=y, month=mth, day=d)
new_year = date(year=y+1, month=1, day=1)
time_left_for_newyear = new_year - today
print('Time left for new year: ', time_left_for_newyear)
t1 = datetime(year = y, month = mth, day = d, hour = h, minute = m, second = s)
t2 = datetime(year = y+1, month = 1, day = 1, hour = 0, minute = 0, second = 0)
diff = t2 - t1
print('Time left for new year:', diff)

#5  # Calculate the time difference between 1 January 1970 and now.
epoch = datetime(1970, 1, 1)
time_since_epoch = now - epoch
print("Days:", time_since_epoch.days)
print("Seconds (remaining of the last day):", time_since_epoch.seconds)
print("Total seconds since epoch:", int(time_since_epoch.total_seconds()))