import datetime
import pandas as pd
from datetime import date
import time



x = ["Time","Day", "Month","Year"]
dayx = {0:"Monday",1:"Tuesday",2:"Wednesday",3:"Thursday",4:"Friday",5:"Saturday",6:"Sunday"}
rows =[x] 


try:
	while True:
#define columns using input and for loop.
#Append all columns to a dedicated nested list
		today = date.today
		day_raw = datetime.datetime.today().weekday()
		m = datetime.datetime.today().month
		y = datetime.datetime.today().year
		t = str(datetime.datetime.now().time())
#################
		rows.append([[t],[dayx[day_raw]],[m],[y]])
#		print(rows[-1], "\n")
		df1 = pd.DataFrame(rows)
		print(df1.shape, "\n")
		time.sleep(2)
################
except KeyboardInterrupt:
	df1.to_csv("~/dev/automate_python/test.csv")





