# #Functions with outputs
#
# def format_name(f_name, l_name):
#     formated_f_name = f_name.title()
#     formated_l_name = l_name.title()
#
#     return f"{formated_f_name} {formated_l_name}"
#
# print(format_name("AnGElA", "Yu"))


def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                # print("Leap year.")
                return True
            else:
                # print("Not leap year.")
                return False
        else:
            # print("Leap year.")
            return True
    else:
        # print("Not leap year.")
        return False


def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    month_days_leap_year = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    year = is_leap(year)
    if year == True:
        days = month_days_leap_year[month - 1]
    else:
        days = month_days[month - 1]
    return days


# 🚨 Do NOT change any of the code below
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
