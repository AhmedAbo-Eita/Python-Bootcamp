#definition of leap year function
def leap_year(year):
    if year % 4 == 0:
        if year % 100 != 0:
            return "Leap Year"
        else:
            if year % 400 == 0:
                return "Leap Year"
            else:
                return "Not a leap year"
    else:
        return "Not a leap year"
