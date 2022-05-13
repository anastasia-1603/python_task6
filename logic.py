import datetime
from calendar import Calendar


def leap_year(year: int):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False


def days_in_month(month: int, year: int):
    if month in {1, 3, 5, 7, 8, 10, 12}:
        return 31
    if month == 2:
        if leap_year(year):
            return 29
        return 28
    return 30


def get_days_list(year: int, month: int):
    return Calendar().monthdayscalendar(year, month)


def month_num_to_name(month: int, language):
    months = []
    if language == "en":
        months = ["January", "February", "March", "April", "May", "June", "July",
                  "August", "September", "October", "November", "December"]
    return months[month-1]


def get_curr_year():
    return datetime.datetime.now().year


def get_curr_month():
    return datetime.datetime.now().month


def get_curr_day():
    return datetime.datetime.now().day


if __name__ == "__main__":
    print(get_curr_year())
