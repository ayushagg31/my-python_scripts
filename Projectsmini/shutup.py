import sched
import time
import os
import datetime

s = sched.scheduler(time.time, time.sleep)

def shoo():
	os.system('shutdown')

now = datetime.datetime.now()
if now.hour >= 0 & now.hour <=12:
	t_hr = 4
elif now.hour >12 and now.hour <24:
	t_hr = 28
t_min = 59
t_sec = 60
diff_hr = t_hr-now.hour
diff_min = t_min-now.minute
diff_sec = t_sec-now.second
total_time_left = diff_sec+diff_min*60+ (diff_hr*60*60)
print "total_time_left == "+str(diff_hr)+":"+str(diff_min)+":"+str(diff_sec)
data = total_time_left
s.enter(data, 1, shoo , ())
s.run()	