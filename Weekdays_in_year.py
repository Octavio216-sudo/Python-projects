import calendar
class MyCalendar:
    def __init__(self, year, weekday):
        self.year = year
        self.weekday = weekday  # 0 = Monday, 6 = Sunday
    def count_weekdays_in_year(self):
        for month in range(1, 13):
            for week in calendar.monthcalendar(self.year, month):
                day_number = week[self.weekday]
                if day_number != 0:
                    yield day_number

sunday_count = list(MyCalendar(2020, 6).count_weekdays_in_year())
print("Number of Sundays in 2020:", len(sunday_count))