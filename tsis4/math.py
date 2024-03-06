#Exercise 1
import math
degree = 15
radian = math.radians(degree)
print("Input degree:", degree)
print("Output radian:", radian)

#Exercise 2
height = 5
base1 = 5
base2 = 6
area = 0.5 * (base1 + base2) * height
print("Height:", height)
print("Base, first value:", base1)
print("Base, second value:", base2)
print("Expected Output:", area)

#Exercise 3
import math
sides = 4
length = 25
area = (sides * length ** 2) / (4 * math.tan(math.pi / sides))
print("Input number of sides:", sides)
print("Input the length of a side:", length)
print("The area of the polygon is:", area)

#Exercise 4
base_length = 5
height = 6
area = base_length * height
print("Length of base:", base_length)
print("Height of parallelogram:", height)
print("Expected Output:", area)