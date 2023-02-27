#My first Attempt - Below

# small_pizza = 15 
# medium_pizza = 20
# large_pizza = 25


# print("Welcom to Python Pizza Deliveries!")
# size = input('What size pizza do you want? S, M, or L ')
# add_pepperoni = input("Do you want pepperoni? Y or N ")
# cheese = input("Do you want extra cheese? Y or N")

# bill = 0 


# if add_pepperoni == "Y":
#     if size == "S":
#         bill += 2 
#     if size == "M":
#         bill += 3
#     if size == "L":
#         bill += 3
#     if cheese == "Y":
#         bill += 1 
        
 
# if size == "S":
#     bill += 15
#     if size == "M":
#         bill += 20
#         if size == "L":
#             bill += 25

          
        
# total_bill = bill + add_pepperoni + size 


# print(total_bill)    


#My Second Attempt 

print("Welcome to Python Pizza Deliveries!")
size = input('What size pizza do you want? S, M, or L ')
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

# Set the bill to 0 at the beginning of the program
bill = 0 

# If statement to determin size of Pizza 
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else: 
    bill += 25
    
# if statement to determine if the customer wants to add pepporoni   
if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

# if statement to determine if the customer wants extra cheese        
if extra_cheese == "Y":
    bill += 1

# Calculate the total amount of the customers bill
print(f"Your final bill is: ${bill}.")


# Logical Operators 
