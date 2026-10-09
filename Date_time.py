import datetime
from datetime import date
import time
import calendar
import os
choose = int(input("Choose what you want to test: "))

#-------------------------------------------------------------------------------------------------1
#using the date class
if choose == 1: 
    #creating a date object of today's date
    today = date.today()
    print("Today's date is:", today)

    #creating a date object of a specific date
    specific_date = date(2022, 1, 1)

    #getting each time attribute from specific date object
    print("Year:", specific_date.year)
    print("Month:", specific_date.month)
    print("Day:", specific_date.day)

    #getting the year, month, and day from the date object
    print("Year:", today.year)
    print("Month:", today.month)
    print("Day:", today.day)

    #getting the minimum and maximum date values
    print("Minimum date value:", date.min)
    print("Maximum date value:", date.max)

    #getting the smallest possible difference between two date objects
    print("Smallest possible difference between two date objects:", date.resolution)
#-------------------------------------------------------------------------------------------------2
#using the time class
if choose == 2:
    #creating a time object of the current time
    current_time = time.localtime()
    print("Current time is:", time.strftime("%H:%M:%S", current_time))

    #creating and printing a time object of a specific time
    specific_time2 = time.strptime("12:30:00", "%H:%M:%S")
    print("Specific time is:", time.strftime("%H:%M:%S", specific_time2))
#-------------------------------------------------------------------------------------------------3
#using datetime.time class
if choose == 3:
    #creating a time object of the current time
    current_time = datetime.datetime.now().time()
    print("Current time is:", current_time)

    #creating and printing a time object of a specific time
    specific_time = datetime.time(12, 30, 0)
    print("hour: ", specific_time.hour)
    print("minute: ", specific_time.minute)
    print("second: ", specific_time.second)
#-------------------------------------------------------------------------------------------------4
#using the datetime.timedelta class 
if choose == 4:
    #creating a timedelta object of 1 day  
    one_day = datetime.timedelta(days=1)
    print("One day is:", one_day)

    #creating a timedelta object of 1 hour
    one_hour = datetime.timedelta(hours=1)
    print("One hour is:", one_hour)

    #creating a timedelta object of 1 minute
    one_minute = datetime.timedelta(minutes=1)
    print("One minute is:", one_minute)

    #creating a timedelta object of 1 second
    one_second = datetime.timedelta(seconds=1)
    print("One second is:", one_second)
#-------------------------------------------------------------------------------------------------5
#using the replace() method of the datetime class
if choose == 5:
    #creating a datetime object of the current date and time
    current_datetime = datetime.datetime.now()
    print("Current date and time is:", current_datetime)

    #replacing the year, month, and day of the current datetime object
    new_datetime = current_datetime.replace(year=2023, month=1, day=1)
    print("New date and time is:", new_datetime)
#-------------------------------------------------------------------------------------------------6
#Printing the week number of the current date
if choose == 6:
    #creating an object of the current date
    current_date = datetime.datetime.now().date()
    #getting the week number of the current date
    week_number = current_date.isocalendar()[1]
    print("Week number of the current date is:", week_number)
#-------------------------------------------------------------------------------------------------7
#Printing the day of the week of the current date
if choose == 7:
    #creating an object of the current date
    current_date = datetime.datetime.now().date()
    #getting the day of the week of the current date
    day_of_week = current_date.isoweekday()
    print("Day of the week of the current date is:", day_of_week)
#-------------------------------------------------------------------------------------------------8
#Using the time.sleep() method to pause the program for a specific amount of time
if choose == 8:
    today = date(2024, 11, 20)
    print("Today's date is:", today)
    update_year = today.year
    update_month = today.month
    for i in range(30):
        update_year += 1
        if update_month == 12:
            update_month = 1
        else:
            update_month += 1
        today += date.resolution
        update_day = today.day
        print("Updated date is:", date(update_year, update_month, update_day))
        time.sleep(1)  # Pause the program for 1 second
#-------------------------------------------------------------------------------------------------------9
#timestamps are the amount of seconds that have passed since 1970 january 1 00:00:00
if choose == 9:
    timestamp_example1 = time.time()#returns timestamp of the present
    print(timestamp_example1)
    date_stamp = date.fromtimestamp(timestamp_example1) #turns timestamp into a date
    print(date_stamp)
    specific_day = datetime.datetime(2028, 11, 5, 6, 30, 30)
    print(specific_day.timestamp())
#-------------------------------------------------------------------------------------------------------10
#ctime turns the given timestamp into a date
if choose == 10:
    print(time.ctime())
    timestamp_ex1 = datetime.datetime(2028, 11, 5, 6, 30, 30).timestamp()
    print(time.ctime(timestamp_ex1))
#-----------------------------------------------------------------------------------------------------------11
#gmtime and localtime both return a struct_time tuple made up of the following elements:
#tm_year (Index 0): 4-digit calendar year (e.g., 2019)
#tm_mon (Index 1): Month number from 1 to 12 (unlike the C structure, which is 0 to 11)
#tm_mday (Index 2): Day of the month from 1 to 31
#tm_hour (Index 3): Hour from 0 to 23
#tm_min (Index 4): Minute from 0 to 59
#tm_sec (Index 5): Second from 0 to 61 (accommodating leap seconds and historical offsets)
#tm_wday (Index 6): Day of the week from 0 (Monday) to 6 (Sunday)
#tm_yday (Index 7): Day of the year from 1 to 366
#tm_isdst (Index 8): Daylight Saving Time flag (1 for active, 0 for inactive, or -1 if unknown)
if choose == 11:
    print(time.localtime())
    print(time.gmtime())
    for i in time.struct_time(sequence=time.localtime()):
        print(i, end=", ")
#the main difference between gmtime and localtime is that localtime accounts for timezone settings while gmtime automatically returns the date in UTC
#-------------------------------------------------------------------------------------------------------------------------------------------------------12
#Naive objects: Have their tzinfo attribute set to None they do not contain enough information to unambiguously locate themselves relative to other 
# date/time objects
if choose == 12:
    print(time.tzname) #Returns a tuple containing the standard time name and the daylight savings time name
    print(time.timezone) #The offset in seconds west of UTC for standard time
    print(time.altzone) #the offset for daylight savings time
    print(time.daylight)#0 if daylight savings time isnt defined in the system's local time. 1 if it is.
    #Aware objects: Have an attached tzinfo subclass instance where utcoffset() does not return None
    utc_zone = datetime.UTC #Creating a timezone object
    tz_plus4 = datetime.timezone(datetime.timedelta(hours=4), name="+04:00")#creating an offsetted timezone object
    dt = datetime.datetime(2026, 10, 7, 10, 0, 0, tzinfo=tz_plus4)
    print(dt)
    current_utc = datetime.datetime.now(tz_plus4)
    print(current_utc)
    dt = datetime.datetime.fromtimestamp(1572879180.0, tz=tz_plus4)
    print(dt)
    print(dt.astimezone())
    dt_naive = current_utc
    dt_aware = dt_naive.replace(tzinfo=utc_zone)
    dt_naive = dt_aware.replace(tzinfo=None)
    print(dt_naive.tzname()) # returns none as naive timezone objects done have a tzinfo subclass instance
    print(dt_aware.tzname())
#-------------------------------------------------------------------------------------------------------------------13
#using the calendar module
if choose == 13:
    calendar.setfirstweekday(0)#Alters which day appears first in a printed month, represented by 0=Monday to 6=Sunday. The default is monday.
    print(calendar.weekheader(10))#Returns each day of a week in string form. the parameter lets you set a character limit for each weekday name.
    print(calendar.calendar(2008, 2, 1, 6, 3))#Returns the calendar for the year. Needs to be used with print because the ouput is a string
    calendar.prcal(2008, 0,  0, 6, 3)#returns the same thing as the above function without needing print.
    #Parameters of the above functions: w = number of characters allocated to each data cell; l = number of vertical text lines allocated for each week row; 
    #c = horizontal space between months; m = number of months displayed horizontally per row. 
    print(calendar.month(2008, 6, 0, 0))#Returns one single formatted month. w and l do here what they do above. 
    calendar.prmonth(2008, 6, 0, 0)#Does what .month does without the print().
#------------------------------------------------------------------------------------------------------------------------------14
#Instantiaiting calendar objects
if choose == 14:
    cal = calendar.TextCalendar(0)#Subclass of Calendar that outputs a calendar as a simple plain text similar to the UNIX program cal.
    print(cal.formatmonth(2008, 6, 0, 0))#the calendar object can be used with these methods: formatmonth(year, month) → Returns a string for one month.
    #formatyear(year) → Returns a string for the whole year. formatyearpage(year) → Returns a multi-page string for the year (like a wall calendar).
    #prmonth(year, month) → Prints a month directly. pryear(year) → Prints a year directly.
    htmlcal = calendar.HTMLCalendar(0)
    print(htmlcal.formatmonth(2008, 6, True))#Similar to textcalendar but used for web develpment.
    cal2 = calendar.Calendar(0)#Primarily used to iterate through a calendar.
#-------------------------------------------------------------------------------------------------------------------------------------------15
#iterating through calendar objects
if choose == 15:
    cal = calendar.Calendar(0)
    print("\n")
    for day in cal.itermonthdates(2008, 6): #returns the days of the specified month and a few more. 
        print(day, end=", ")
    print("\n")
    for day in cal.itermonthdays(2008, 6):#like itermonthdates but it prints 0 for every day that isnt in the specified month.
        print(day, end=", ")
    print("\n")
    for day in cal.iterweekdays():#simply returns every day of a week. 0=monday, 6=sunday.
        print(day, end=", ")
    print("\n")
    tup_list = list(cal.itermonthdays2(2008, 6))#Can also be iterated through like the others but this puts them side by side instead of on top of each other. end= does not work
    print(tup_list)
    print("\n")
    tup_list2 = list(cal.itermonthdays3(2008, 6))#returns tuples containing the year, month, and day. 
    print(tup_list2)
    print("\n")
    tup_list3 = list(cal.itermonthdays4(2008, 6))#returns tuples containing the year, month, day, and weekday
    print(tup_list3)