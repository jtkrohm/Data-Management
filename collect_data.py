import datetime
import pandas as pd
from datetime import date
import time


dayx = {0:"Monday",1:"Tuesday",2:"Wednesday",3:"Thursday",4:"Friday",5:"Saturday",6:"Sunday"}
day_raw = datetime.datetime.today().weekday()
today = date.today
x = ["Time","Day", "Month","Year"]
#print(dayx[day_raw])
print(x)
m = datetime.datetime.today().month
y = datetime.datetime.today().year
t = str(datetime.datetime.now().time())
data = [x]


while True:
	today = date.today
	day_raw = datetime.datetime.today().weekday()
	m = datetime.datetime.today().month
	y = datetime.datetime.today().year
	t = str(datetime.datetime.now().time())
	data.append([t, dayx[day_raw], m, y])
	print(data[-1])
	time.sleep(15)
