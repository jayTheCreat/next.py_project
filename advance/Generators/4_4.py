def gen_secs():
    for sec in range(60):
        yield sec


def gen_minutes():
    for minute in range(60):
        yield minute


def gen_hours():
    for hour in range(24):
        yield hour


def gen_time():
    for hour in gen_hours():
        for minute in gen_minutes():
            for sec in gen_secs():
                yield "%02d:%02d:%02d" % (hour, minute, sec)


def gen_years(start=2019):
    while True:
        yield start
        start += 1


def gen_months():
    for month in range(1, 13):
        yield month


def gen_days(month, leap_year=True):
    days = 0
    if month in [1, 3, 5, 7, 8, 10, 12]:
        days = 31
    elif month in [4, 6, 9, 11]:
        days = 30
    elif month == 2:
        if leap_year:
            days = 29
        else:
            days = 28
    for day in range(1, days + 1):
        yield day


def is_leap_year(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True


def gen_date():
    for year in gen_years():
        for month in gen_months():
            for day in gen_days(month, is_leap_year(year)):
                for gt in gen_time():
                    yield "%02d/%02d/%04d %s" % (day, month, year, gt)


def main():
    gen = gen_date()
    for i in range(0, 10000000):
        if i % 1000000 == 0:
            print(next(gen))
        else:
            next(gen)


if __name__ == '__main__':
    main()
