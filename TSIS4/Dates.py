#Exercise 1
from datetime import datetime, timedelta
x = datetime.now()
y = x - timedelta(days = 5)
print("Current date", x.strftime("%Y-%B-%A"))
print("New Date", y.strftime("%Y-%B-%A"))

#Exercise 2
from datetime import datetime , timedelta
x = datetime.now()
y = x - timedelta(days=1)
z = x + timedelta(days=1)
print(x.strftime("%A"))
print(y.strftime("%A"))
print(z.strftime("%A"))

#Exercise 3
import datetime
x = datetime.datetime.now()
y = x - datetime.timedelta(days=5)
a = y.replace(microsecond=0)
print("Current date:", x)
print(a)

#Exercise 4
from datetime import datetime , timedelta
x = datetime.now()
y = x - timedelta(days=1)
difference = x-y
seconds = difference.total_seconds()
print(seconds)

#Example 1
import datetime
x = datetime.datetime.now()        #current date
print(x)         

#Example 2
import datetime
x = datetime.datetime.now()
print(x.year)                       # 2024 Monday    
print(x.strftime("%A"))             # ("%A") current day

#Example 3
import datetime
x = datetime.datetime(2020 , 5, 17)         # 2020-05-17  00:00:00
print(x)

#Example 4
import datetime
x = datetime.datetime(2018, 6 , 1)              #("%B") - Month
print(x.strftime("%B"))

                            #Table
""" Directive	Description	Example	Try it
%a	Weekday, short version	Wed	
%A	Weekday, full version	Wednesday	
%w	Weekday as a number 0-6, 0 is Sunday	3	
%d	Day of month 01-31	31	
%b	Month name, short version	Dec	
%B	Month name, full version	December	
%m	Month as a number 01-12	12	
%y	Year, short version, without century	18	
%Y	Year, full version	2018	
%H	Hour 00-23	17	
%I	Hour 00-12	05	
%p	AM/PM	PM	
%M	Minute 00-59	41	
%S	Second 00-59	08	
%f	Microsecond 000000-999999	548513	
%z	UTC offset	+0100	
%Z	Timezone	CST	
%j	Day number of year 001-366	365	
%U	Week number of year, Sunday as the first day of week, 00-53	52	
%W	Week number of year, Monday as the first day of week, 00-53	52	
%c	Local version of date and time	Mon Dec 31 17:41:00 2018	
%C	Century	20	
%x	Local version of date	12/31/18	
%X	Local version of time	17:41:00	
%%	A % character	%	
%G	ISO 8601 year	2018	
%u	ISO 8601 weekday (1-7)	1	
%V	ISO 8601 weeknumber (01-53)	01 """
