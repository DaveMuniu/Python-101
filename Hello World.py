 #  Reverse a String!

string='Hello World'

reverse_string=string[::-1]

print(reverse_string)


#   Check if string is a Palindrome!

string='David'

reverse_string=string[::-1]

is_palindrome=string==reverse_string

print(is_palindrome)


#   Check Number of Vowels in a string!

string='October'

vowels='aeiou'

count_vowels=len([char for char in string if char in vowels])

print(count_vowels)

from math import *

print(sqrt(20))


#    Calculate Area of Rectangle!

Length = float(input("Enter length of rectangle: "))

Width = float(input("Enter width of rectangle: "))

Area = Length * Width

print("Area of Rectangle is : ", Area)


#    Converte Temperatures from Fahrenheit to Celcius!
from math import *

Fahrenheit = float(input("Enter temperature in Fahrenheit: "))

Celcius = (Fahrenheit - 32) * 5/9

print("Temperature in Celcius is: ",Celcius)

#   Returning Square of Sum of Two Numbers!

def sum_of_squares(num1, num2):
    square1 = num1 ** 2  # Square of the first number
    square2 = num2 ** 2  # Square of the second number
    sum_squares = square1 + square2  # Sum of the squares
    return sum_squares

# Example usage
number1 = float(input("Enter First Number: "))
number2 = float(input("Enter Second Number: "))
result = sum_of_squares(number1, number2)
print("Sum of squares:", result)


