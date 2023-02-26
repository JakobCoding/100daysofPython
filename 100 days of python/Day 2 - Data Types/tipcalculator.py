# Tip Calculator Program 

#If the bill was $150.00, split between 5 people, with 12% tip.
#Each person should pay 150.00 * 1.12 / 5
#Round the result to two decimel places 

#welcome people to the tip calculator
print("Welcome to the tip calculator!")

# Get a float input for the total bill 
bill = input("What was the total bill? ")
f_bill = float(bill)

# ask what percentage tip they would like give 10, 12 or 15?
tip = input("What percentage tip would you like to give? 10, 12 or 15? ")

int_tip = int(tip)

# find out how many people will split the bill 

total_ppl = input("How many people to split the bill? ")
int_ppl = int(total_ppl)

tip_percentage = int_tip / 100

actual_tip = f_bill * tip_percentage
total_bill = f_bill + actual_tip

sum = total_bill / int_ppl
sum_round = round(sum, 2)

print(f"Each person should pay: {sum_round:.2f}")