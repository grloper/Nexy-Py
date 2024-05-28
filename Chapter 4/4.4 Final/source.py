# Description: This script generates all dates in DD-MM-YYYY HH:MM:SS format.

# Generator functions to generate all:
# seconds, minutes, hours, years, months, days, and dates in a day.

def gen_secs():
    """Generate all seconds in a minute."""
    for second in range(60): # 60 seconds in a minute
        yield second

def gen_minutes():
    """Generate all minutes in an hour."""
    for minute in range(60): # 60 minutes in an hour
        yield minute

def gen_hours():
    """Generate all hours in a day."""
    for hour in range(24): # 24 hours in a day
        yield hour

def gen_time():
    """Generate all times in a day in HH:MM:SS format."""
    for hour in gen_hours():
        for minute in gen_minutes():
            for second in gen_secs():
                yield f"{hour:02d}:{minute:02d}:{second:02d}"


def gen_years(start=2024): # Current year is 2024
    """Generate all years starting from a given year."""
    while True:
        yield start
        start += 1

def gen_months():
    """Generate all months in a year."""
    for month in range(1, 13): # 12 months in a year
        yield month

def gen_days(month, leap_year=False):
    """
    Generate all days in a given month.
    
    Args:
        month (int): The month for which the days are to be generated.
        leap_year (bool): Indicates if the year is a leap year.
    """
    # Days in each month starting from January
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
    if leap_year:
        days_in_month[1] = 29 # update february days to 29
    for day in range(1, days_in_month[month - 1] + 1):
        yield day

def gen_date():
    """Generate all dates in DD-MM-YYYY HH:MM:SS format."""
    for year in gen_years():
        for month in gen_months():
            # boolean value indicating if the year is a leap year
            leap_year = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) 
            for day in gen_days(month, leap_year):
                for time in gen_time():
                    yield f"{day:02d}-{month:02d}-{year:04d} {time}"

def every_million_seconds():
    """Print the output of gen_date every millionth time."""
    count = 0
    for date_time in gen_date():
        if count % 1000000 == 0: # Print every millionth date
            print(date_time)
        count += 1

def main():
    every_million_seconds()

if __name__ == "__main__":
    main()
