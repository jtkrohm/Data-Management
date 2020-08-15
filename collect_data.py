import datetime
import pandas as pd
from datetime import date
import time


dayx = {0:"Monday",1:"Tuesday",2:"Wednesday",3:"Thursday",4:"Friday",5:"Saturday",6:"Sunday"}
day_raw = datetime.datetime.today().weekday()
today = date.today
x = ["Time","Day", "Month","Year"]
m = datetime.datetime.today().month
y = datetime.datetime.today().year
t = str(datetime.datetime.now().time())
df = pd.DataFrame([[t, dayx[day_raw], m, y]])
df.columns = x
print(df)

while True:
	today = date.today
	day_raw = datetime.datetime.today().weekday()
	m = datetime.datetime.today().month
	y = datetime.datetime.today().year
	t = str(datetime.datetime.now().time())
	#row.append([t, dayx[day_raw], m, y])
	#print(row[-1])
	df1 = pd.DataFrame([[t, dayx[day_raw], m, y]])
	df1.columns = x
	df1.append([df1], ignore_index = True) 
	print(df1)
#	time.sleep(15)





