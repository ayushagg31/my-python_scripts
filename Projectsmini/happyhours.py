import sys
import sched
import urllib
import time
import datetime
import webbrowser
import os
s = sched.scheduler(time.time, time.sleep)


def task():
    for i in range(num):
        testfile.retrieve(name[i], filename[i])
        print "Download Complete"+str(i)


def bhago():
    sys.exit()

# def youtube(url):
#	command = "wget "+ url
#	os.system(command)


# print time.time()

now = datetime.datetime.now()
if now.hour >= 0 and now.hour <= 1:
    t_hr = 1
elif now.hour > 1 and now.hour <= 12:
    t_hr = 12 + 13
elif now.hour > 12 and now.hour < 24:
    t_hr = 25
#t1_hr = 28
t_min = 59
t_sec = 60
diff_hr = t_hr-now.hour
diff_min = t_min-now.minute
diff_sec = t_sec-now.second
total_time_left = diff_sec+diff_min*60 + (diff_hr*60*60)
# print total_time_left
print "total_time_left == "+str(diff_hr)+":"+str(diff_min)+":"+str(diff_sec)

diff = 10800
testfile = urllib.URLopener()
num = input("enter no. of download files for the happy hours-->  ")
name = []
filename = []
for j in range(num):
    name += [raw_input("Enter url of website-->  ")]
    filename += [raw_input("enter filename-->")]

s.enter(total_time_left, 1, task, ())
s.enter(total_time_left+diff, 1, bhago, ())
s.run()
print time.time()
