# A Brief Introduction with Exercises and solutions by Ben Stephenson

## Intro to Programming exercises

## Exercise 1: Mailing Address
# USER_MAILING_ADDRESS = "Randy Jenkins\n12121 Willow Ln\nOverland Park, KS"
# print(USER_MAILING_ADDRESS)
# print(" ")

## Exercise 2: Hello
# user_name = input("Enter your name please: ")
# welcome_message = "Hello"
# print(welcome_message + " " + user_name + ".")
# print(" ")

## Exercise 3: Area of a Room
# first_user_question = float(input("What is the width of the room in feet? "))
# second_user_question = float(input("What is the length of the room in feet? "))
# area = first_user_question * second_user_question
# area = str(area) + " feet"
# print(area)
# print(" ")

## Exercise 4: Area of a Field
# length_field = float(input("What is the length of your field in feet? "))
# width_field = float(input("What is the width of your field in feet? "))
# converted_length = 43_560 / length_field
# converted_width = 43_560 / width_field
# field_area = converted_length * converted_width
# field_area = str(field_area) + " acres"
# print(field_area)

## Function version
# ACRE = 43560
# square_footage = float(input("How many square feet is your tract of land?"))

# def convertToAcres(square_footage):
#     acres_in_tract = square_footage / ACRE
#     print("Your tract is %.2f" % acres_in_tract, "acres")

# convertToAcres(square_footage)

## Exercise 5: Bottle Deposits
above_liter_size = float(input("How many containers are there one liter or larger? "))
below_liter_size = float(input("How many containers are there less than one liter? "))

def bottleDeposits(above_liter_size, below_liter_size):
    above_liter_size = above_liter_size * 0.25
    below_liter_size = below_liter_size * 0.10
    container_cost = above_liter_size + below_liter_size
    print("The cost will be: $ %.2f" % + container_cost)
    print("If you return containers the refund will be: $ %.2f" % + container_cost)

bottleDeposits(above_liter_size, below_liter_size)