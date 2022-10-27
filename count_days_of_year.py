def is_year_leap(year):
    if year % 4 != 0: return False
    elif year % 100 != 0: return True
    elif year % 400 != 0: return False
    else: return True

def days_in_month(year, month):
    months = [31,28,31,30,31,30,31,31,30,31,30,31]
    month_in_list = month - 1
    if is_year_leap(year) == True:
        months = [31,29,31,30,31,30,31,31,30,31,30,31]
    return months[month_in_list]

def day_of_year(year, month, day):
    months = [31,28,31,30,31,30,31,31,30,31,30,31]
    month_in_list = month - 1
    total_days = 0
    i = 0
    if is_year_leap(year) == True:
        months = [31,29,31,30,31,30,31,31,30,31,30,31]
    while i < month_in_list:
        total_days += months[i]
        i += 1
    total_days += day
    if month <= 12 & day <= 31: return total_days
    else: return

print(day_of_year(2000, 12, 31))
