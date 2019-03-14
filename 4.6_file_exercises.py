# Print out every line in the file
# Print out every line in the file, but add a line numbers
from pprint import pprint

# file = '4.5_import_exercises.py'
# with open(file) as f:
#     lines = f.readlines()

# new_contents = []
# for i in lines:
#     new_contents.append(i)


# print(new_contents)

grocery_list = ['medicine', 'milk', 'apples']


def make_grocery_list():
    with open('my_grocery_list.txt', 'x') as f:
        for i in range(1_000_000):
            f.write('grocery_list' + i + '.txt')


# def show_grocery_list():
