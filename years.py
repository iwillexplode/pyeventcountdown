from datetime import date
from datetime import datetime
import time

years = []
count = 0
monthdaysleap = [0,31,60,91,121,152,182,213,244,274,305,335]
monthdays = [0,31,59,90,120,151,181,212,243,273,304,334]
for i in range(0,1000):
    years.append(count)
    if i % 4 == 0:
        count = count + 366
    else:
        count = count + 365
#print(years)
#print(len(years))

day = input("whats the event day? 1-31 " )   
month = input("whats the event month? 1-12 ")
year = input("whats the event year? 2000-2999 ") 
hour = input("whats the event hour? 00 - 23 ")
minute = input("whats the event minute? 0 - 59 ")

eventstring = day, month, year, hour, minute
#print(eventstring)

yearindex = int(year) - 2000
eventyear = years[yearindex]

if int(year) % 4 == 0:
    eventmonth = monthdaysleap[int(month)-1]
else:
    eventmonth = monthdays[int(month)-1]

eventday = int(day)
totalevent = eventday + eventmonth + eventyear
#print(totalevent)

eventtime = int(hour) * 3600 + int(minute) * 60 + 0

while True:
    today = date.today()
    d1 = today.strftime("%m")
    d2 = today.strftime("%y")
    d3 = today.strftime("%d")

    todayindex = int(d2)
    todayyear = years[todayindex]

    if int(d2) % 4 == 0:
        todaymonth = monthdaysleap[int(d1)-1]
    else:
        todaymonth = monthdays[int(d1)-1]

    todayday = int(d3)
    totaltodayevent = todayday + todaymonth + todayyear
    #print(totaltodayevent)

    now = datetime.now()
    t3 = now.strftime("%S")
    t1 = now.strftime("%H")
    t2 = now.strftime("%M")

    todaytime = int(t1) * 3600 + int(t2) * 60 + int(t3)
 
    timedifference = int(eventtime) - int(todaytime)

    daystogo = totalevent - totaltodayevent


    #print(daystogo)
    results = divmod(timedifference,60)
    #print(results[0],":", results[1])

    if daystogo == 0:                       #today
        if timedifference >= 0:
            results = divmod(timedifference,3600)
            results2 = divmod(results[1],60)
            print(daystogo,"days", results[0], "hours", results2[0], "minutes", results2[1], "seconds", "to go")
        else:
            timedifference = 0 - timedifference
            results = divmod(timedifference,3600)
            results2 = divmod(results[1],60)
            print(daystogo,"days", results[0], "hours", results2[0], "minutes", results2[1], "seconds", "ago")


    elif daystogo < 0:                      #days before
        if timedifference > 0:
            daystogo = daystogo + 1
            timedifference = 86400 - timedifference
        else:
            timedifference = 0 - timedifference
            
        daystogo = 0 - daystogo
        
        #print("result")
        results = divmod(timedifference,3600)
        results2 = divmod(results[1],60)
        print(daystogo,"days", results[0], "hours", results2[0], "minutes", results2[1], "seconds", "ago")

    else:                                   #days after
        if timedifference < 0:
            daystogo = daystogo - 1
            timedifference = 86400 + timedifference
        #print("result")
        results = divmod(timedifference,3600)
        results2 = divmod(results[1],60)
        print(daystogo,"days", results[0], "hours", results2[0], "minutes", results2[1], "seconds", "to go")

    time.sleep(1)
