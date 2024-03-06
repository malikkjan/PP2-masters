#Exercise 1
def squares_generator(N):
    for i in range(N):
        yield i ** 2
N = 5
squares = squares_generator(N)
for square in squares:
    print(square)
    
#Exercise 2
def even_numbers(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i

n = int(input("Enter a number: "))
even_numbers = even_numbers(n)
print(','.join(map(str, even_numbers)))

#Exercise 3
def divisor(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i
n = 20
numbers = divisor(n)
for num in numbers:
    print(num)

#Exercise 4
def squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2

a = 3
b = 7
for square in squares(a, b):
    print(square)
    
#Exercise 5
def timer(n):
    while n >= 0:
        yield n
        n -= 1
n = 5
countdown = timer(n)
for num in countdown:
    print(num)