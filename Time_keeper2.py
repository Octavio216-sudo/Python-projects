class WeekDayError(Exception):
    def __init__(self):
        super().__init__("Invalid day of the week")

class Weeker:
    __validdays = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    def __init__(self, day):
        if day not in Weeker.__validdays:
            raise WeekDayError()
        self.day = day

    def __str__(self):
        return self.day

    def add_days(self, n):
        index_day = Weeker.__validdays.index(self.day)
        days_left = n % 7
        new_index = (index_day + days_left) % 7
        self.day = Weeker.__validdays[new_index]
    def subtract_days(self, n):
        index_day = Weeker.__validdays.index(self.day)
        days_left = n % 7
        new_index = (index_day - days_left) % 7
        self.day = Weeker.__validdays[new_index]
try:
    weekday = Weeker('Mon')
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(23)
    print(weekday)
    weekday = Weeker('Monday')
except WeekDayError:
    print("Sorry, I can't serve your request.")