#Tip calculator

greetings = 'Welcome to the tip calculator\n'
total_bill = input('What was the total bill? $')
tip = input('what percentage tip would you like to give? 10, 12, 15')
people = input('How many people to split the bill?')
payment = '{:.2f}'. format(float(total_bill + tip) / int(people))
print(f'Each person should pay:${payment}')
