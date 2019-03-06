# Define a function named is_two. It should accept one input and return
# True if the passed input is either the number or the string 2, False otherwise.

# def is_two(one_input):
#     if one_input == 2 or one_input == '2':
#         return True
#     else:
#         return False

# print(is_two(2))

# ------------------------------------------------

# Define a function named is_vowel. It should return True if the passed string is a vowel, False otherwise.

def is_vowel(letter):
    vowels = ['a', 'e', 'i', 'o', 'u']
    if letter.lower() in vowels:
        return True
    else:
        return False
# print(is_vowel('i'))

# ------------------------------------------------

# Define a function named is_consonant. It should return True if the passed string 
# is a consonant, False otherwise. Use your is_vowel function to accomplish this.

def is_consonant(letter):
    if is_vowel(letter) == False:
        return True
    else:
        return False
# print(is_consonant('x'))

# ------------------------------------------------

# Define a function that accepts a string that is a word. 
# The function should capitalize the first letter of the word if the word starts with a consonant.

def word_cap(word):
    if is_consonant(word[0]):
        word = word.capitalize()
    return word

# print(word_cap('uppercase'))

# ------------------------------------------------

# Define a function named calculate_tip. It should accept a tip percentage 
# (a number between 0 and 1) and the bill total, and return the amount to tip.

def calculate_tip(tip_percent, bill):
    tip_amount = bill * tip_percent
    return tip_amount

print(f'${calculate_tip(.2,10):.2f}')

# ------------------------------------------------

# Define a function named apply_discount. It should accept a original price,
# and a discount percentage, and return the price after the discount is applied.

def apply_discount(original_price, discount_percent):
    new_price = original_price - (original_price * discount_percent)
    return new_price

# print(f'Price with discount = ${apply_discount(10.00, .25):.2f}')

# ------------------------------------------------

# Define a function named handle_commas. It should accept a string that is a number
#  that contains commas in it as input, and return a number as output.

def handle_commas(number_with_commas):
    number_without_commas = number_with_commas.replace(',', '')
    return number_without_commas

# print('Your new number without commas is: ',handle_commas('1,500,500,000'))

# ------------------------------------------------

# Define a function named get_letter_grade. It should accept a number 
# and return the letter grade associated with that number (A-F).

def get_letter_grade(number):
    number = int(number)
    grade_test = {
        'A': [90,100],
        'B': [80,89],
        'C': [70,79],
        'D': [60,69],
        'F': [0,59]
    }
    for grade_key in grade_test.keys():

        upper_bound = grade_test[grade_key][1]
        lower_bound = grade_test[grade_key][0]

        if number >= lower_bound and number <= upper_bound:
            return grade_key

# print(get_letter_grade(88))

# ------------------------------------------------

# Define a function named remove_vowels that accepts a string and returns a string with all the vowels removed.

def remove_vowels(word):
    new_word = ''
    word_list = []
    for v in word:
        if is_vowel(v):
            continue
        word_list.append(v)
    return new_word.join(word_list)

# print(remove_vowels('hello'))

# Define a function named normalize_name. It should accept a string and return a valid python identifier, that is:
# anything that is not a valid python identifier should be removed
# leading and trailing whitespace should be removed
# everything should be lowercase
# spaces should be replaced with underscores
# for example:
# Name will become name
# First Name will become first_name
# % Completed will become completed

# ------------------------------------------------

def normalize_name(python_identifier):
    valid_python = python_identifier.strip().lower().replace(' ', '_')
    return valid_python

# print(normalize_name('\nCrazy wORd'))

# ------------------------------------------------

# Write a function named cumsum that accepts a list of numbers and 
# returns a list that is the cumulative sum of the numbers in the list.
# cumsum([1, 1, 1]) returns [1, 2, 3]
# cumsum([1, 2, 3, 4]) returns [1, 3, 6, 10]

def cumsum(number_list):
    cum_num = 0
    new_list =[]
    for i in number_list:
        cum_num = cum_num + i
        new_list.append(cum_num)
    return new_list

# print(cumsum([1, 2, 3]))

# ------------------------------------------------

# Bonus
# Create a function named twelveto24. It should accept a string in the 
# format 10:45am or 4:30pm and return a string that is the representation 
# of the time in a 24-hour format. 

def twelveto24(user_time):
    hours = 0
    minutes = 0
    am_pm = user_time[-2]
    if am_pm == 'p':
        am_pm = 12
        user_time = user_time.replace('pm', '')
    else:
        am_pm == 0
        user_time = user_time.replace('am', '')
    user_time = user_time.split(':')
    hours = user_time[0]
    minutes = user_time[1]
    if am_pm == 12:
        hours = int(hours) + am_pm
        hours = str(hours)
    new_time = f'new time = {str(hours)}:{str(minutes)}'
    return new_time

# print(twelveto24('4:30am'))

# Bonus write a function that does the opposite.

#too easy to just reuse

# Create a function named col_index. It should accept a spreadsheet column name, 
# and return the index number of the column.
# col_index('A') returns 1
# col_index('B') returns 2
# col_index('AA') returns 27

# def col_index(column_letter):
#     letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#     letters = list(letters)
#     col_letters = 


# print(col_index('B'))

def col_index(col_str):
    col_str = col_str.upper()
    expn = 0
    col_num = 0
    for char in reversed(col_str):
        col_num += (ord(char) - ord('A') + 1) * (26 ** expn)
        expn += 1

    return col_num

# print(col_index('aaa'))

def col_index2(col_letter):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alphabet = list(alphabet)
    itty = 0
    for letter in alphabet:
        itty = itty + 1
        if col_letter == letter:
            return itty
    return itty

# def multi_letter(placeholder):

    

# print(col_index2('AA'))
# print(col_index2('I'))
# print(col_index2('O'))
# print(col_index2('Z'))