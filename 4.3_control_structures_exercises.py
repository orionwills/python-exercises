# prompt the user for a day of the week, print out whether the day is Monday or not

# day_chosen = input('Choose a day of the week: ')
# if day_chosen == 'Monday':
#     print(day_chosen)

# 2. prompt the user for a day of the week, print out whether the day is a weekday or a weekend

# day_chosen = input('Choose a day of the week: ')
# if day_chosen == 'Saturday' or day_chosen == 'Sunday':
#     print('This is a weekend.')
# else:
#     print('This is a weekday.')

# weekend_days = ['saturday', 'sunday', 'sat', 'sun']
# weekday = input('Enter a weekday: ')
# if weekday.lower() in weekend_days:
#     print('Weekend')
# else:
#     print('Weekday')

# 3. create variables for
#
# - the number of hour worked in one week
# - the hourly rate
# - how much the week's paycheck will be

# write the python code that calculates the weekly paycheck. You get paid time
# and a half if you work more than 40 hours

# weekly_hours_worked = int(input('How many hours did you work? \n'))
# hourly_rate = float(input('What is your hourly rate? \n'))
# if weekly_hours_worked > 40:
#     overtime_hours = weekly_hours_worked - 40
#     weekly_hours_worked = 40
# else:
#     overtime_hours = 0
# print(f'Your paycheck should be ${(weekly_hours_worked * hourly_rate) + ((1.5 * hourly_rate) * overtime_hours)}.')

# 1. The input function can be used to prompt for input 
# and use that input in your python code. Prompt the user 
# to enter a positive number and write a loop that counts 
# from 0 to that number. (Hints: first make sure that the 
# value the user entered is a valid number, also note that the 
# input function returns a string, so you'll need to convert 
# this to a numeric type.)

# user_number = int(input('Enter a positive number: '))
# if user_number > 0:
#     for n in range(0,user_number):
#         print(n)
# else:
#     print(f'{user_number} is not a positive number.')

# 2. Write a program that prompts the user for a positive integer. 
# Next write a loop that prints out the numbers from the number 
# the user entered down to 1.


# user_number = int(input('Enter a positive number: '))
# if user_number > 0:
#     for n in range(user_number,0,-1):
#         print(n)
# else:
#     print(f'{user_number} is not a positive number.')

#Create a list of dictionaries where each dictionary represents
# a book that you have read. Each dictionary in the list should
# have the keys title, author, and genre. Loop through the list
# and print out information about each book.

books_i_have_read = [{'title': '12 Rules for Life', 'author': 'Jordan Peterson', 'genre': 'self-help'},
{'title': 'Panda Bear Panda Bear', 'author': 'Eric Carle', 'genre': 'children'},
{'title': 'Jurassic Park', 'author': 'Michael Crichton', 'genre': 'fiction'}]

for list in books_i_have_read:
    print('{} was the genre.'.format(list['genre']))

