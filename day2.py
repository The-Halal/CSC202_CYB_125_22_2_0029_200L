#Data types

#Strings
#Subscript
print('Hello'[3])

print('123'+'345')

#Integers
print(123 + 345)
print(123_345_26)

#Float
print(2.135)

#Boolean
print(True or False)

#type funct
name = input('What is your name?')
print(type(name))

name = len(input('What is your name?'))
print(type(name))

#Type conversion
nam = len(input('What is your name?'))
name = str(nam)
print('Your name has ' + name + ' characters' )

print(70 + float(10.23))

print(str(40) + str(100))


#Day 2 Exercise 1
num = str(input('Type in 2 didgit number'))
first_digit = num[0]
second_digit = num[1]
print(int(first_digit) + int(second_digit))

#Mathematical Operator
print(2 + 2)
print(2 - 2)
print(2 * 2)
print(2 / 2)
print(2 % 2)
print(2 ** 2)
print(2 // 2)
#PEMDAS
#Parentheses
#Exponential
#Multiplication
#Division
#Addition
#Subtraction

print(3 * 3 + 3 / 3 - 3)
print(3 * (3 + 3) / 3  - 3)

#Day 2 Exercise 2
#BMI Calculator
height = float(input('Enter your Height in m:'))
weight = int(input('Enter your weight in Kg:'))
bmi = weight / height ** 2
result = int(bmi)
print(result)

print(round(8 / 3))
print(round(8 / 3, 4))
print(round(8 / 3, 2))


#Manipulation
result = 4 / 2
result /= 2
print(result)

score = 0
#score a point
score += 1
print(score)

data = 35
data -= 14
print(data)

rem = 21
rem %= 3
print(rem)

#f-string
score = 0
#score a point
score += 1
win = True
print(f'Your score is {score}, your winning is {win}')


#Day 2 Exercise 3
age = input('Enter your current age')
years = 90 - int(age)
months = (90 * 12) - int(age) * 12
weeks = (90 * 52 ) - int(age) * 52
days = (90 * 365) - int(age) * 365
print(f'You have {days} days, {weeks} weeks, {months} months and {years} years left')

