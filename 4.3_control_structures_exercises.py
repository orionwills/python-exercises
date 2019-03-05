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

# 2. Loop Basics
# While
# Create an integer variable i with a value of 5.
# Create a while loop that runs so long as i is less than or equal to 15
# Each loop iteration, output the current value of i, then increment i by one.
# Your output should look like this:
# 5 6 7 8 9 10 11 12 13 14 15

# i = 5
# while i <= 15:
#     print(i)
#     i += 1

# Create a while loop that will count by 2's starting with
# 0 and ending at 100. Follow each number with a new line.

# i = 0
# while i <= 100:
#     print(i)
#     i += 2

# Alter your loop to count backwards by 5's from 100 to -10.

# i = 100
# while i > -10:
#     print(i)
#     i -= 5

#Create a while loop that starts at 2, and displays the number squared 
# on each line while the number is less than 1,000,000.

# i = 2
# while i < 1_000_000:
#     print(i)
#     i = i * i


# Write a loop that uses print to create the output shown below

# for i in range(100, 0, -5):
#     print(i)

# For Loops
#Write some code that prompts the user for a number, then shows 
# a multiplication table up through 10 for that number.

# user_number = input('Enter a number: ')
# i = 1
# for x in range(i, 11):
#     print(f'{user_number} x {i} = {int(user_number) * x}')
#     i += 1

#Create a for loop that uses print to create the output shown below.
# 1
# 22
# 333
# 4444
# 55555
# 666666
# 7777777
# 88888888
# 999999999

# i = 1
# for x in range(i, 10):
#     print(f'{i}' * i)
#     i+= 1


#break and continue
# Prompt the user for an odd number between 1 and 50. Use a loop 
# and a break statement to continue prompting the user if they 
# enter invalid input. (Hint: use the isdigit method on strings 
# to determine this). Use a loop and the continue statement to 
# output all the odd numbers between 1 and 50, except for the 
# number the user entered.

# user_input = input('Please enter an odd number between 1 and 50 \n')
# for o in user_input:
#     if int(user_input) < 1 or int(user_input) > 50 or int(user_input) % 2 != 0 or not user_input.isdigit():
#         user_input = input('Not a valid number, try again.  Enter an odd number between 1 and 50 \n')
#     else:
#         for p in range(1, 51):
#             print(p)
#             if p % 2 == 0:
#                 break
#             else: 
#                 if p == user_input:
#                     break

# user_input = input('Enter an odd number between 1 and 50: ')
# while not user_input.isdigit() or int(user_input) > 50 or int(user_input) < 1 or int(user_input) % 2 == 0:
#     user_input = input('Not a valid number, try again.  Enter an odd number between 1 and 50 \n')
# print(f'Number to skip is: {user_input}\n')
# for p in range(51):
#     if p == int(user_input):
#         print(f'Yikes! Skipping number: {user_input}')
#         continue
#     if p % 2 == 0:
#         continue
#     print(f'Here is an odd number: {p}')
    
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

# Write a program that prompts the user for a positive integer. 
# Next write a loop that prints out the numbers from the number 
# the user entered down to 1.


# user_number = int(input('Enter a positive number: '))
# if user_number > 0:
#     for n in range(user_number,0,-1):
#         print(n)
# else:
#     print(f'{user_number} is not a positive number.')

# Fizzbuzz
# One of the most common interview questions for entry-level programmers 
# is the FizzBuzz test. Developed by Imran Ghory, the test is designed 
# to test basic looping and conditional logic skills.

# Write a program that prints the numbers from 1 to 100.
# For multiples of three print "Fizz" instead of the number
# For the multiples of five print "Buzz".
# For numbers which are multiples of both three and five print "FizzBuzz".

# for number in range(101):
#     if number % 3 == 0 and number % 5 == 0:
#         print('FizzBuzz')
#     elif number % 3 == 0:
#         print('Fizz')
#     elif number % 5 == 0:
#         print('Buzz')
#     else:
#         print(number)

# Display a table of powers.

# Prompt the user to enter an integer.
# Display a table of squares and cubes from 1 to the value entered.
# Ask if the user wants to continue.
# Assume that the user will enter valid data.
# Only continue if the user agrees to.



# user_number = input('What number would you like to go up to?')
# int_user_number = int(user_number)
# user_number_squared = int_user_number * int_user_number
# user_number_cubed = int_user_number ** int_user_number
# print('Here are your numbers!\n')
# print('number ', '|', ' squared ', '|', ' cubed')
# for i in range(1,int_user_number + 1):
#     print(f'{i} {i * i} {i * i * i}')

# Convert given number grades into letter grades.
# Prompt the user for a numerical grade from 0 to 100.
# Display the corresponding letter grade.
# Prompt the user to continue.
# Assume that the user will enter valid integers for the grades.
# The application should only continue if the user agrees to.
# Grade Ranges:
# A : 100 - 88
# B : 87 - 80
# C : 79 - 67
# D : 66 - 60
# F : 59 - 0

# a =[]
# for i in range(88,99):
#     a.append(i)
# x = 92 #placeholder; will change to input later
# if x in a:
#     print('yes')
# else:
#     print('no')

# user_grade = input('Please enter a numerical grade from 0 to 100: ')
# ugrade = int(user_grade)
# if ugrade >= 99:
#     grade_letter = 'A+'
# elif ugrade >= 88:
#     grade_letter = 'A'
# elif ugrade >= 86:
#     grade_letter = 'B+'
# elif ugrade >= 80:
#     grade_letter = 'B'
# elif ugrade >= 78:
#     grade_letter = 'C+'
# elif ugrade >= 67:
#     grade_letter = 'C'
# elif ugrade >= 65:
#     grade_letter = 'D+'
# elif ugrade >= 60:
#     grade_letter = 'D'
# else:
#     grade_letter = 'F'
# print(f'Your grade letter is: {grade_letter}')


#6. Create a list of dictionaries where each dictionary represents
# a book that you have read. Each dictionary in the list should
# have the keys title, author, and genre. Loop through the list
# and print out information about each book.
#Prompt the user to enter a genre, then loop through your books 
# list and print out the titles of all the books in that genre.

books_i_have_read = [{'title': '12 Rules for Life', 'author': 'Jordan Peterson', 'genre': 'self-help'},
{'title': 'Panda Bear Panda Bear', 'author': 'Eric Carle', 'genre': 'children'},
{'title': 'Jurassic Park', 'author': 'Michael Crichton', 'genre': 'fiction'}]

user_genre = input('Which genre would you like to search for?')

print('Here are the books with the genre of: ', user_genre)
for list in books_i_have_read:
    print('title: {}'.format(list['title']))