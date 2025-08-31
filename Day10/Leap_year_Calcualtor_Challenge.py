def is_leap_year(year):
    if year %4 == 0:
        if year % 100 == 0:
            if year % 400 == 0: 
                return True
            else:
                return False
        else:
            return True
    else:
        return False

year_to_check = int(input("What Year do you want to check? "))
print(f"{year_to_check} is a Leap Year: {is_leap_year(year_to_check)}")