months = {"Jan": 31,
          "Feb": 28,
          "Mar": 31,
          "Apr": 30,
          "May": 31,
          "Jun": 30,
          "Jul": 31,
          "Aug": 31,
          "Sep": 30,
          "Oct": 31,
          "Nov": 30,
          "Dec": 31}


def CountingSundays():
    day = 2  # 1st jan 1901------------->tuesday
    No_of_sundays = 0

    for year in range(1901, 2001):

        for mont in months:

            day = day + months[mont]
            if year % 4 == 0 and mont == "February":  # Condition for leap year
                day += 1
            if day % 7 == 0:  # Sunday conidtion : starting from tueday at day=2, Each sunday falls on this condition
                No_of_sundays += 1
    return No_of_sundays


No_of_sundays = CountingSundays()
print(No_of_sundays)
