# # List Practice
# my_favorite_food = ['ice cream', 'cake','pizza']
# friends_food = ['angel food cake','bread','salad']

# my_favorite_food = friends_food[:]

# print(friends_food)

# friends_food.append('crackers')

# print(friends_food)

# print(my_favorite_food)

# my_favorite_food.append('water')

# print(my_favorite_food)

# # Looping Through a Slice
# print("The first three items in the list are: ")
# for friends_foo in friends_food[:3]:
#     print(friends_foo.title())

# # Writing over a Tuple
# dimensions = (200, 250)

# # Will not work (tuple object does not suport item assignment)
# # dimensions[0] = 130

# dimensions = (400, 100)
# print("\nModified dimensions:")
# for dimension in dimensions:
#     print(dimension)

# # Controling proper names 
# print(" ")
# print("Control format of strings.")
# cars = ['audi','bmw','subaru','toyota']
# for car in cars:
#     if car == 'bmw':
#         print(car.upper())
#     else:
#         print(car.title())

# # Conditional Tests
# # Checking for Equality
# print(" ")

# # More tests for equality
# print(" ")
# print("Test for inquality using only if statement.")

# requested_topping = 'mushrooms'
# if requested_topping != 'anchovies':
#     print("Hold the anchovies!")
#     print(' ')

# # Test numbers for inequality
# print(" ")
# print("Test numbers for inequality.")
# answer = 17
# if answer != 42:
#     print("That is not the correct answer. Please try again!")
#     print(" ")

# # Testing for age
# # Parentheses can be used with tests to improve readability
# print(" ")
# print("Checking for correct age.")

# age_0 = 23
# age_1 = 17
# if (age_0 >= 21) and (age_1 >= 21):
#     print("Both are the legal age.")
# else:
#     print("You need two of age to continue.")
#     print(" ")

# # Using or to Check Multiple Condtions
# age_0 = 22
# age_1 = 18
# if age_0 >= 21 or age_1 >= 21:
#     print("At least one is the correct age to continue.")
# else:
#     print("Please locate a guardian for this ride.")

# # Checking Whether a Value is in a list
# print(" ")
# print("Checking a value is not in a list")
# requested_toppings = ['mushrooms','onions','pineapple']
# banned_users = ['marie', 'tim','terry']
# user = 'marie'
# 'pepperoni' in requested_toppings

# if user not in banned_users:
#     print(user.title() + ", you can post a response if you wish.")
# else:
#     print("Access denied.")
#     print(" ")

# # 5-1 Try it yourself Conditional Tests
# print("Conditional Tests:")
# car = 'subaru'
# print("Is car == 'subaru'? I predict True.")
# print(car == 'subaru')
# print(" ")

# print("\nIs car == 'audi'? I predict False.")
# print(car == 'audi')
# print(" ")

# # add user input to dictionary

# rental_properties = {}

# rental_open = True

# while rental_open:
#     username = input("\nWhat is your name? ")
#     rental_property = input("What is the address of the property you would like to rent?")

#     rental_properties[username] = rental_property

#     repeat = input("\nDo you know anyone who might like to rent out a property?")
#     if repeat == 'no':
#         rental_open = False

# print("\n--- Property to rent ---")
# for username, rental_property in rental_properties.items():
#     print(username + " has " + rental_property + " to rent.")

# # Using muliple lists
# from pickle import TRUE


# shop_ingredients = ['pepperoni','pineapple','onions','peppers','sausage']

# requested_ingredients = ['onions','peppers','sausage']

# for requested_ingredient in requested_ingredients:
#     if requested_ingredient in shop_ingredients:
#         print(f"Adding {requested_ingredient}.")
#     else:
#         print("We don't have the requested topping(s)")
#         break

# print(" ")
# print("Finished with this order.")

# # 5-8 Hello Admin
# username_list = ['admin','master','billing','policy','legal']

# login_manager = True

# while login_manager:
#     login_message = "Welcome to the login page."
#     user_login = input("Please enter your username: ")
#     user_logi = user_login
#     report_status = "Nothing new to report."
#     if user_logi in username_list:
#         if user_logi == "admin":
#             print(input(f"Hello {user_logi} would you like to see a status report? "))
#             if 'yes':
#                 print(report_status)
#             else:
#                 print(leave_option)
#         else:
#             print(f"Hello {user_login} thank you for login in again.")
#     else:
#         print("Access denied.")
#     leave_option = input("Do you wish to continue? 'Yes or no'")
#     if leave_option == 'no':
#         login_manager = False
# print("This session is complete.")

# A Object Oriented Programming

# class Car():
#     body = "sedan"
#     color = "blue"
#     wheels = 4
#     wheels_traction = 7
#     windows = 4
#     doors = 4

#     def __init__(self, damage, health):
#         self.damage = damage
#         self.health = health

# chevy = Car(21, 92)

# print(chevy.damage)
# print(chevy.wheels_traction)
# print(chevy.health)

# Chapter 8 review
# 8.3 T-Shirt
# def make_shirt(size = 'l', text = 'I love Python'):
#     print(f"The size of the shirt is {size} and the text is {text}.")

# print("\n8.3 T-Shirt section:")
# make_shirt('sm')
# make_shirt()
# make_shirt(text = 'Die hard')

# #8-4 Large Shirts
# print("\n8.4 Large Shirts section:")
# make_shirt(text= 'I love Python')
# make_shirt(size = 'medium')
# make_shirt(size = 'xxl', text= 'There can be only one!')

# # 8.5 Cities
# def describe_city(city = 'Reykjavik', country = 'Iceland'):
#     print(f'{city} is in {country}.')

# print("\n8.5 Cities section:")
# describe_city()

# Returning a Simple Value
# def get_formatted_name(first_name, last_name):
#     """Return a full name, neatly formatted."""
#     full_name = first_name + ' ' + last_name
#     return full_name.title()

# musician = get_formatted_name('jimi', 'hendrix')
# print(musician)


# def get_formatted_name(first_name, middle_name, last_name):
#     """Receive full name and format."""
#     middle_name = ' '
#     if middle_name:
#         full_name = first_name + ' ' + middle_name + ' ' + last_name
#     else:
#         full_name = first_name + ' ' + last_name
#     return full_name.title()

# username = get_formatted_name('randy', 'bernard', 'jenkins')
# print(username)
# username = get_formatted_name('randy', 'jenkins')
# print(username)

# Returning a Dictionary
# def build_person(first_name, last_name):
#     """Return a dictionary of information about a person."""
#     person = {'first': first_name, 'last': last_name}
#     return person

# musician = build_person('randy', 'jenkins')
# print(musician)

# # Adding Age
# def build_person(first_name, last_name, age=''):
#     person = {'first': first_name, 'last': last_name}
#     if age:
#         person['age'] = age
#     return person

# musician = build_person('jimi', 'hendrix', age=27)
# print(musician)

# Using a function with a while loop
# def get_formatted_name(first_name, last_name):
#     """Return a full name, neatly formatted."""
#     full_name = first_name + ' ' + last_name
#     return full_name.title()

# # This is an infinite loop!
# while True:
#     print("\nPlease tell me your name: (enter 'exit' at any time to quit.)")
#     f_name = input("First name: ")
#     if f_name == 'exit':
#         break

#     l_name = input("Last name: ")
#     if l_name == 'exit':
#         break

#     formatted_name = get_formatted_name(f_name, l_name)
#     print("\nHello, " + formatted_name + "!")

# 8-6 City Names (Try it yourself)
def city_country(city, country):
    """Return a entered city and country."""
    city_name = city + ', ' + country
    return city_name

print("Enter a city and country. (Press exit at any time to leave)")
city = input("Please enter a city: ")
country = input("Please enter a country: ")

formatted_city = city_country(city, country)
print("\nWelcome, we will send you to " + formatted_city + ".")

# 8-7 Album (Try it yourself)





# Creating Multiple Instances Chapter 9

# class Dog:
#     """A simple attempt to model a dog."""
    
#     def _init_(self, name, age):
#         """Initialize name and age attributes."""
#         self.name = name
#         self.age = age

#     def sit(self):
#         """Simulate a dog sitting in repsonse to a command"""
#         print(f"{self.name} is now sitting.")

#     def roll_over(self):
#         """Simulate rolling over in response to a command."""
#         print(f"{self.name} rolled over!")


        
