# #Conditional statement
# water_level = 50
# if water_level > 80:
#     print('Drain water')
# else: 
#     print('Continue')

# print('Welcome to the Rollercoaster')
# height = int(input('enter your height in cm'))
# if height > 120:
#     print('Can ride')
# else:
#     print('Can\'t ride')

# #Day 3 Exercise 1
# #Even or Odd
# num = int(input('Which numder do you want to check'))
# even = num % 2
# if even == 0:
#     print('Even')
# else:
#     print('Odd')

# print('Welcome to the Rollercoaster')
# height = int(input('Enter your height'))
# if height >= 120:
#     print('You can ride')
#     age = int(input('Enter your age'))
#     if age < 12:
#         print('Please pay $5.')
#     elif age <=18:
#         print('Please pay $7')
#     else: 
#         print('Please pay $12.')
# else: 
#     print('You need to grow taller to ride')


# #Day 3 Exercise 2
# #Bmi calculator
# height = float(input('Enter your heightin m:'))
# weight = float(input('Enter your weight in kg:'))
# bmi = weight / height **2
# if bmi < 18.5:
#     print('You are underweight')
# elif bmi == 18.5 < 25:
#     print(f'Your bmi is {bmi},You have a normal weight')
# elif bmi == 25 < 30:
#     print(f'Your bmi is {bmi},They are overweight')
# elif bmi == 30 < 35:
#     print(f'Your bmi is {bmi},You are obese')
# else:
#     print(f'Your bmi is {bmi},They are clinically obese')       

# #Day 3 Exercise 3
# #Leap year check
# year = int(input('Enter the year you want to check'))
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print('It is Leap year')
#         else: 
#             print('Not a Leap Year')
#     else:
#         print('It is a Leap year')
# else: 
#     print('Not a Leap Year')

# #Multiple if
# print('Welcome to the Rollercoaster')
# height = int(input('Enter your height'))
# if height >= 120:
#     print('You can ride')
#     age = int(input('Enter your age'))
#     if age < 12:
#         bill = 5
#         print('Children tickets are $5.')
#     elif age <=18:
#         bill = 5
#         print('Youth tickets are $7')
#     else: 
#         bill = 12
#         print('Adult tickets $12.')
#     wants_photo = input('Do you want photo taken? Y or N')
#     if wants_photo == 'Y':
#         bill += 3
#         print(f'Your bill is $ {bill}')
# else: 
#     print('You need to grow taller to ride')


# #Day 3 Exercise 4
# #Pizza Order Exercise
# print('Welcome to Python Pizza Deliveries')
# size = input('What size of Pizza do you want? S or M or L')
# add_pepperoni = input('Do you want pepperoni? Y or N')
# extra_cheese = input('Do you want extra cheese? Y or N')
# bill = 0

# if size == 'S':
#     bill += 15
# elif size == 'M':
#     bill += 20
# else:
#     bill += 25
# if add_pepperoni == 'Y':
#     if size == 'S':
#         bill += 2
#     else:
#         bill += 3
#         print(f'Your bill is ${bill}')

# #Logical Operators
# a = 12
# b = a > 10 and a < 15
# print(b)

# c = 15
# d = c > 12 and c > 50
# print(d)

# e = 8
# f = not e > 12
# print(f)


# print('Welcome to the Rollercoaster')
# height = int(input('Enter your height'))
# if height >= 120:
#     print('You can ride')
#     age = int(input('Enter your age'))
#     if age < 12:
#         bill = 5
#         print('Children tickets are $5.')
#     elif age <=18:
#         bill = 5
#         print('Youth tickets are $7')
#     elif age >= 45 and age <= 55:
#         bill = 0
#         print('Everything is going to be fine. Have a free ride on us')
#     else: 
#         bill = 12
#         print('Adult tickets $12.')
#     wants_photo = input('Do you want photo taken? Y or N')
#     if wants_photo == 'Y':
#         bill += 3
#         print(f'Your bill is $ {bill}')
# else: 
#     print('You need to grow taller to ride')


#Day 3 Exercise 5
print('Welcome to love calculator!')
name_1 = input('What is your name?/n')
name_2 = input('What is their name?/n')
name = name_1 + name_2

name_lower = name.lower()
t = name_lower.count('t')
r = name_lower.count('r')
u = name_lower.count('u')
e = name_lower.count('e')
total = str(t + r + u + e)

l = name_lower.count('l')
o = name_lower.count('o')
v = name_lower.count('v')
e = name_lower.count('e')
love = str(l + o + v + e)
love_score = total + love
int_score = int(love_score)

if (int_score < 10) or (int_score > 90):
    print(f'Your Love Scores is {love_score}, you go together like Coke and Mentos')
elif (int_score == 40) or (int_score <= 50):
    print(f'Your Love Scores is {love_score}, you are alright together')
else:
    print(f'Your Love Scores is {love_score}')




















