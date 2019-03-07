from function_exercises import is_vowel2
from function_exercises import is_consonant2
from function_exercises import get_letter_grade as glg
import itertools
import json
from pprint import pprint

# How many different ways can you combine the letters from "abc" with the numbers 1, 2, and 3?

# print(list(itertools.product('abc', '123', repeat=1)))

# pprint(list(itertools.permutations('abcd', 4)))

# How many different ways can you combine two of the letters from "abcd"?

# abc = itertools.chain('ABC', 'DEF')

# print(abc)


data = json.load(open('profiles.json'))

# Total number of users
print(f'number of users: {len(data)}')

# Number of active users
active_count = 0
for dictionaries in data:
    if dictionaries['isActive']:
        active_count = active_count + 1
print(f'number of active users: {active_count}')

# Number of inactive users
inactive_count = 0
for dictionaries in data:
    if not dictionaries['isActive']:
        inactive_count = inactive_count + 1
print(f'number of inactive users: {inactive_count}')

# Grand total of balances for all users


def string_to_float(currency):
    currency = currency.replace('$', '')
    currency = currency.replace(',', '')
    return float(currency)


# print(string_to_float('$1,234.55'))
# Average balance per user
grand_total = 0
for dictionaries in data:
    grand_total = grand_total + string_to_float(dictionaries['balance'])
print(f'grand total of balances for all users: ${grand_total:,}')
print(f'average balance per user: ${grand_total / len(data):,.2f}')

# User with the lowest balance
# User with the highest balance
balances = []
for dictionaries in data:
    balances.append(string_to_float(dictionaries['balance']))
# print(f'lowest balance is: ${min(balances):.2f}')
# print(f'lowest balance is: ${max(balances):.2f}')

balance_dict = {}
balance_users = []
lowest = ''
highest = ''
for dictionaries in data:
    if string_to_float(dictionaries['balance']) == min(balances):
        lowest = dictionaries['name']
    if string_to_float(dictionaries['balance']) == max(balances):
        highest = dictionaries['name']

print(f'user with lowest balance: {lowest}')
print(f'user with highest balance: {highest}')

# Most common favorite fruit

fruits = []
strawberry_count = 0
apple_count = 0
banana_count = 0
for dictionaries in data:
    fruits.append(dictionaries['favoriteFruit'])
    strawberry_count = fruits.count('strawberry')
    apple_count = fruits.count('apple')
    banana_count = fruits.count('banana')
fruit_dict = {}
for things in fruits:
    fruit_dict[things['strawberry']] = fruits.count('strawberry')
    fruit_dict[things['apple']] = fruits.count('apple')
    fruit_dict[things['banana']] = fruits.count('banana')

print(max(things))

print(f'{strawberry_count} people like strawberries\n{apple_count} people like apples\n{banana_count} people like bananas')
# Least most common favorite fruit
# Total number of unread messages for all users

# pprint(list(data))
