from  datetime import date as dt
import datetime as dt1
from datetime import time 
import time
import pytz


print(dt1.timedelta())
print(dt1.datetime(1998, 8 , 15))
main = dt.today()

main_1 =  dt1.datetime.now()
for i in range(0,2):
    time.sleep(2)
    m1 = dt1.datetime.now()
    print(m1)





while True:
    print("This prints once a minute.")
    time.sleep(5)
    m1 = dt1.datetime.now()
    print(m1)

