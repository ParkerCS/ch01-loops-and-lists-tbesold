#CONDITIONS (15PTS TOTAL)

# PROBLEM 1 (GPA - 4pts)
# Grades are values between 0 and 100
# We will translate grades to letters using:
# http://www.collegeboard.com/html/academicTracker-howtoconvert.html
# Make a variable for your percentage grade.
# Make a series of if/elif/else statements to print the letter grade.
# If the user enters a grade lower than zero or higher than 100, just give an error message.
# Don't worry about making an exception for these right now.

grade = int(input("What is your grade? "))
if grade < 65:
    print("you got an F")
elif grade == 65 or grade == 66:
    print("you got a D")
elif grade >= 67 and grade <= 69:
    print("you got a D+")
elif grade >= 70 and grade <= 72:
    print("you got a C-")
elif grade >= 73 and grade <= 76:
    print("you got a C")
elif grade >= 77 and grade <= 79:
    print("you got a C+")
elif grade >= 80 and grade <= 82:
    print("you got a B-")
elif grade >= 83 and grade <= 86:
    print("you got a B")
elif grade >= 87 and grade <= 89:
    print("you got a B+")
elif grade >= 90 and grade <= 92:
    print("you got an A-")
elif grade >= 93 and grade <= 96:
    print("you got an A")
elif grade >= 97 and grade <= 100:
    print("you got an A+")



# PROBLEM 2 (Vowels - 5pts)
# Ask the user to supply a string.
# Print how many different vowels there are in the string.
# The capital version of a lower case vowel is considered to be the same vowel.
# y is not considered a vowel.
# Try to print proper output (e.g., printing “There are 1 different vowels in the string” is ugly).
# Example: When the user enters the string “It’s Owl Stretching Time,”
# the program should say that there are 3 different vowels in the string.

user_input = str(input("Write something: ")).lower()
vowels = ["a", "e", "i", "o", "u"]
number = 0

for i in vowels:
    if i in user_input:
        number += 1
if number == 1:
    print("there is one vowel in your phrase")
else:
    print("there are", number, "vowels in your phrase")




# PROBLEM 3 (Quadratic Equation - 6pts)
# You can solve quadratic equations using the quadratic formula.
# Quadratic equations are of the form Ax2 + Bx + C = 0.
# Such equations have zero, one or two solutions.
# The first solution is (−B + sqrt(B^22 − 4AC))/(2A).
# The second solution is (−B − sqrt(B^2 − 4AC))/(2A).
# There are no solutions if the value under the square root is negative.
# There is one solution if the value under the square root is zero.
# Write a program that asks the user for the values of A, B, and C,
# then reports whether there are zero, one, or two solutions,
# then prints those solutions.
# Note: Make sure that you also take into account the case that A is zero,
# and the case that both A and B are zero.
import math

a = float(input("enter an A value: "))
b = float(input("enter a B value: "))
c = float(input("enter a C value: "))

if (b**2 - (4 * a * c)) < 0:
    print("there are no real solutions")


elif (b**2 - (4 * a * c)) == 0:
    print("there is only one solution")
    print(((-1 * b)/(2 * a)))

else:
    print("there are two solutions")
    print(float((-1 * b) + (math.sqrt((b**2) - (4 * a * c)))) / (2 * a))
    print(float((-1 * b) - (math.sqrt((b**2) - (4 * a * c)))) / (2 * a))