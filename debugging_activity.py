# Debugging - Alvert Lin - 07/19/25

# Syntax Errors
# Runtime Errors
# Logical Errors






print("Code Snippet 2: ----------")
# Index Error - Fixed by printing index i instead of i+1
numbers = [1, 2, 3, 4, 5]
for i in range(len(numbers)):
   print(numbers[i])

print("Code Snippet 3")
# Syntax Error - Fixed by adding colon in front of (radius)
def calculate_area(radius):
   area = 3.14 * radius ** 2
   return area
 
radius = 5
print(calculate_area(radius))

print("Code Snippet 4")
# Syntax Error - Fixed by adding colon in front of 0 and else
def is_even(number):
   if number % 2 == 0:
       return True
   else:
       return False
 
print(is_even(4))
print(is_even(7))

print("Code Snippet 5")
# Syntax Error - Fixed by adding colon in front of range(5) 
for i in range(5):
   print(i)

print("Code Snippet 6")
# Syntax error - needed to add + sign 
def greet(name):
   return "Hello, " + name
 
print(greet("Alice"))

print("Code Snippet 7")
# Indentation Error - indent "sum" 
numbers = [1, 2, 3, 4, 5]
sum = 0
for number in numbers:
    sum += number
print("Sum of numbers:", sum)

print("code snippet 8")
# Recursion Error - Switch + in (n+1) to -
def factorial(n):
   if n == 0:
       return 1
   else:
       return n * factorial(n-1)
 
print(factorial(5))

# Factorial example: 3! = 3x2x1x0

print("Code Snippet 9")
# Runtime Error - fixed by adjusting "if" statement
name = input("Enter your name: ")
if name == "Alice" or name == "Bob":
   print("Hello, " + name)
else:
   print("Hello, stranger!")

print("Code Snippet 10")
# zero Division Error - Fixed by having "num2" be set to integer 1 or any real number
def divide_numbers(x, y):
   result = x / y
   return result
 
num1 = 10
num2 = 1
print(divide_numbers(num1, num2))


