# Roller Coaster Ride Height and age Check

print("Welcome to the Rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age < 12: 
        print("Please pay $5 Have Fun!")
    elif age <= 18:
        print("Please pay $7 Have Fun!") 
    else:
        print("Please pay $12 Have Fun!")
else: 
    print("Sorry, you have to grow taller before you can ride.")    