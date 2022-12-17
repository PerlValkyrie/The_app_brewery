# Check for leap year

# input_year = int(input("Enter a year: "))

# def is_leap(year):
#     if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
#         return True
#     else:
#         return False

# if is_leap(input_year):
#     print("It is a leap year.")
# else:
#     print("It is not a leap year.")

leap_year = int(input("Enter year: "))

if leap_year % 4 == 0:
    if leap_year % 100 == 0:
        if leap_year % 400 == 0:
            print("Leap year")
        else:
            print("Not a leap year.")
    else:
        print("Leap year.")
else:
    print("Not a leap year.")

      