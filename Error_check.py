# # Check code here
# class ShoppingBag():

#     def __init__(self, handles, capacity, items):
#         self.handles = handles
#         self.capacity = capacity
#         self.items = items

#     def showShoppingBag(self):
#         print(" ")
#         print("You have items in your bag!")
#         for item in self.items:
#             print(item)

#         print(" ")

#     def showCapacity(self):
#         print(f'Your capacity is: {self.capacity}')

#     def addToShoppingBag(self):
#         products = input('What would you like to add? ')
#         self.items.append(products)

#     def changeBagCapacity(self, capacity):
#         self.capacity = capacity

#     def increaseCapacity(self, changed_capacity = 10):
#         if self.capacity == isinstance(self.capacity, str):
#             print("We can't add that here.")
#         else:
#             self.capacity += changed_capacity

# wholeFoods_bag = ShoppingBag(2, 10, [])

# def run():
#         while True:
#             response = input('What do you want to do? add/show/quit ~')

#             if response.lower() == 'quit':
#                 wholeFoods_bag.showShoppingBag()
#                 print('Thanks for shopping')
#                 break
#             elif response.lower() == 'add':
#                 wholeFoods_bag.addToShoppingBag()
#             elif response.lower() == 'show':
#                 wholeFoods_bag.showShoppingBag()
#             else:
#                 print('Try another command')

# run()

# def my_function(damage):
#     damage = str(damage)
#     print("money" + damage)

# my_function(-10)

# import turtle

# Regex
# Allows us to take strings and sort through them.

import re
# Using functions with regex


# Sets practice

pattern_int = re.compile('[0-7]')
random_numbers = pattern_int.search('67383')
print(random_numbers)