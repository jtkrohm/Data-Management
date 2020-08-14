#We will collect data on whether it is day or night based on time
#in order to build and test our function for making datasets
import datetime
import pandas as pd
from datetime import date


IS_DAY = True
dayx = {0:"Monday",1:"Tuesday",2:"Wednesday",3:"Thursday",4:"Friday",5:"Saturday",6:"Sunday"}
day_raw = datetime.datetime.today().weekday()
today = date.today
x = ["Time","Day", "Month","Year","Day / Night"]

print(dayx[day_raw])
print(datetime.datetime.today().month)
print(datetime.datetime.today().year)
