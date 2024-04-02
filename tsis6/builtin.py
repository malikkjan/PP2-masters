#1
from functools import reduce

def multiply_list(numbers):
    return reduce(lambda x, y: x * y, numbers)

numbers = [1, 2, 3, 4, 5]
result = multiply_list(numbers)
print("Result of multiplying all numbers in the list:", result)

#2
def count_upper_lower(string):
    upper_count = sum(1 for char in string if char.isupper())
    lower_count = sum(1 for char in string if char.islower())
    return upper_count, lower_count

string = "Hello World"
upper, lower = count_upper_lower(string)
print("Number of uppercase letters:", upper)
print("Number of lowercase letters:", lower)

#3
def is_palindrome(string):
    return string == string[::-1]

string = "radar"
if is_palindrome(string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")

#4
import time
from math import sqrt

def delayed_sqrt(number, milliseconds):
    time.sleep(milliseconds / 1000) 
    return sqrt(number)

number = 25100
milliseconds = 2123
result = delayed_sqrt(number, milliseconds)
print(f"Square root of {number} after {milliseconds} milliseconds is {result}")

#5
def all_true(elements):
    return all(elements)

tuple1 = (True, True, True)
tuple2 = (True, False, True)
print("Are all elements of tuple1 true?", all_true(tuple1))
print("Are all elements of tuple2 true?", all_true(tuple2))