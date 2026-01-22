# File: 1_random_user_id.py
import random
import string

def random_user_id():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

print(random_user_id())
#Question 2: Function to add two numbers

# File: 2_add_two_numbers.py
def add_two_numbers(a, b):
    return a + b
#Question 3: Function to calculate the area of a circle

# File: 3_area_of_circle.py
import math

def area_of_circle(r):
    return math.pi * r * r
#Question 4: Function to convert Celsius to Fahrenheit

# File: 4_convert_celsius_to_fahrenheit.py
def convert_celsius_to_fahrenheit(c):
    return (c * 9/5) + 32
#Question 5: Function to check the season based on the month

# File: 5_check_season.py
def check_season(month):
    month = month.lower()
    if month in ['december', 'january', 'february']:
        return 'Winter'
    elif month in ['march', 'april', 'may']:
        return 'Spring'
    elif month in ['june', 'july', 'august']:
        return 'Summer'
    elif month in ['september', 'october', 'november']:
        return 'Autumn'
#Question 6: Function to print a list

# File: 6_print_list.py
def print_list(lst):
    for item in lst:
        print(item)
#Question 7: Function to reverse a list

# File: 7_reverse_list.py
def reverse_list(lst):
    reversed_lst = []
    for i in range(len(lst)-1, -1, -1):
        reversed_lst.append(lst[i])
    return reversed_lst

print(reverse_list([1, 2, 3, 4, 5]))  # [5, 4, 3, 2, 1]
print(reverse_list(["A", "B", "C"]))  # ["C", "B", "A"]
#Question 8: Function to capitalize list items

# File: 8_capitalize_list_items.py
def capitalize_list_items(lst):
    return [item.capitalize() for item in lst]
#Question 9: Function to add an item to a list

# File: 9_add_item.py
def add_item(lst, item):
    lst.append(item)
    return lst

food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(add_item(food_staff, 'Meat'))  # ['Potato', 'Tomato', 'Mango', 'Milk', 'Meat']

numbers = [2, 3, 7, 9]
print(add_item(numbers, 5))  # [2, 3, 7, 9, 5]
#Question 10: Function to sum numbers in a range

# File: 10_sum_of_numbers.py
def sum_of_numbers(n):
    return sum(range(1, n + 1))

print(sum_of_numbers(5))  # 15
print(sum_of_numbers(10)) # 55
print(sum_of_numbers(100)) # 5050
#Question 11: Function to sum odd numbers in a range

# File: 11_sum_of_odds.py
def sum_of_odds(n):
    return sum(i for i in range(1, n + 1) if i % 2 != 0)
#Question 12: Function to sum even numbers in a range
# File: 12_sum_of_evens.py
def sum_of_evens(n):
    return sum(i for i in range(1, n + 1) if i % 2 == 0)
#Question 13: Function to count evens and odds in a range
# File: 13_evens_and_odds.py
def evens_and_odds(n):
    evens = sum(1 for i in range(n + 1) if i % 2 == 0)
    odds = n + 1 - evens
    return f"The number of odds are {odds}.\nThe number of evens are {evens}."

print(evens_and_odds(100))
#Question 14: Function to check if a number is prime
# File: 14_is_prime.py
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
#Question 15: Function to check if all items in the list are unique
# File: 15_all_unique.py
def all_unique(lst):
    return len(lst) == len(set(lst))
#Question 16: Function to check if all items in the list are of the same data type
# File: 16_all_same_type.py
def all_same_type(lst):
    return all(isinstance(item, type(lst[0])) for item in lst)
#Question 17: Loop to print a triangle pattern

# File: 17_triangle_pattern.py
for i in range(1, 8):
    print('#' * i)
#Question 18: Loop to print a multiplication table

# File: 18_multiplication_table.py
for i in range(11):
    print(f"{i} x {i} = {i * i}")
#Question 19: Loop to print even numbers from 0 to 100

# File: 19_even_numbers.py
for i in range(0, 101, 2):
    print(i)
#Question 20: Loop to print odd numbers from 0 to 100

# File: 20_odd_numbers.py
for i in range(1, 101, 2):
    print(i)
#Question 21: Function to get user input and provide feedback based on age
# File: 21_check_age.py
def check_age():
    age = int(input("Enter your age: "))
    if age >= 18:
        print("You are old enough to drive.")
    else:
        print(f"You need {18 - age} more years to learn to drive.")
#Question 22: Function to grade students based on scores
# File: 22_grade_student.py
def grade_student(score):
    if 80 <= score <= 100:
        return 'A'
    elif 70 <= score < 80:
        return 'B'
    elif 60 <= score < 70:
        return 'C'
    elif 50 <= score < 60:
        return 'D'
    else:
        return 'F'
#Question 23: Create an empty dictionary called dog

# File: 23_dog_dictionary.py
dog = {}
#Question 24: Add properties to the dog dictionary

# File: 24_dog_properties.py
dog['name'] = 'Buddy'
dog['color'] = 'Brown'
dog['breed'] = 'Labrador'
dog['legs'] = 4
dog['age'] = 5
#Question 25: Create a student dictionary and add keys

# File: 25_student_dictionary.py
student = {
    'first_name': 'John',
    'last_name': 'Doe',
    'gender': 'Male',
    'age': 20,
    'marital_status': 'Single',
    'skills': ['Python', 'JavaScript'],
    'country': 'USA',
    'city': 'New York',
    'address': '123 Main St'
}

#Question 26: Get the length of the student dictionary

# File: 26_student_length.py
len(student)
#Question 27: Get the value of skills and check the data type

# File: 27_check_skills.py
skills = student['skills']
type(skills)
#Question 28: Modify the skills values by adding one or two skills

# File: 28_add_skills.py
student['skills'].append('HTML')
#Question 29: Get the dictionary keys as a list

# File: 29_dictionary_keys.py
keys = list(student.keys())
#Question 30: Get the dictionary values as a list

# File: 30_dictionary_values.py
values = list(student.values())
#Question 31: Create an empty tuple

# File: 31_empty_tuple.py
empty_tuple = ()
#Question 32: Create a tuple containing names of your siblings

# File: 32_siblings_tuple.py
brothers = ('John', 'Mike')
sisters = ('Anna', 'Emily')
#Question 33: Join brothers and sisters tuples and assign to siblings

# File: 33_siblings.py
siblings = brothers + sisters
#Question 34: Modify the siblings tuple and add the name of your parents

# File: 34_family_members.py
family_members = siblings + ('Father', 'Mother')



