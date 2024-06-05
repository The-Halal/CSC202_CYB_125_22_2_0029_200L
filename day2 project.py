#Tip calculator
greetings = 'Welcome to the tip calculator\n'
bill = int(input('What was the total bill? \n$'))
tip = int(input('what percentage tip would you like to give? 10, 12, 15\n'))
people = int(input('How many people to split the bill?'))
bill_tip = tip / 100 * bill 
total_bill = bill + bill_tip
bill_per_person = total_bill / people
final_amount = '{:.2f}'.format(bill_per_person)
print(f'Each person should pay: ${final_amount} ')
