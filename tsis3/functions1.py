#Ex1 
def grams_to_ounces(grams):
    return 28.3495231 * grams
#Ex2
def fahrenheit_to_celsius(fahrenheit):
    return (5 / 9) * (fahrenheit - 32)
#Ex3
def solve(numheads, numlegs):
    for rabbits in range(numheads + 1):
        chickens = numheads - rabbits
        if (4 * chickens + 2 * rabbits) == numlegs:
            return chickens, rabbits
    return "No solution"
#Ex4
def filter_prime(numbers):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    return [num for num in numbers if is_prime(num)]
#Ex5
from itertools import permutations

def print_permutations(s):
    perms = [''.join(p) for p in permutations(s)]
    for perm in perms:
        print(perm)
#Ex6
def reverse_words(sentence):
    words = sentence.split()
    reversed_sentence = ' '.join(reversed(words))
    return reversed_sentence
#Ex7
def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False
#Ex8
def spy_game(nums):
    code = [0, 0, 7, 'x']
    for num in nums:
        if num == code[0]:
            code.pop(0)
    return len(code) == 1
#Ex9
import math

def sphere_volume(radius):
    return (4/3) * math.pi * radius**3
#Ex10
def unique_elements(lst):
    new_list = []
    for item in lst:
        if item not in new_list:
            new_list.append(item)
    return new_list
#Ex11
def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]
#Ex12
def histogram(numbers):
    for num in numbers:
        print('*' * num)
#Ex13
import random

def guess_the_number():
    print("Hello! What is your name?")
    name = input()
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    secret_number = random.randint(1, 20)
    num_guesses = 0

    while True:
        print("Take a guess.")
        guess = int(input())

        num_guesses += 1

        if guess < secret_number:
            print("Your guess is too low.")
        elif guess > secret_number:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {num_guesses} guesses!")
            break

