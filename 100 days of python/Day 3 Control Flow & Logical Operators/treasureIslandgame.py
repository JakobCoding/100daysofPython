# Treasure Island game - Choose your Destiny - Can you find the treasure? 

print("Welcome to Treasure Island.")
print("Your mission is to find the Treasure.")

choice1 = input("You have reached a cross road, which direction will you take? left or right?\n").lower()

if choice1 == "left":
    #continue in the game
    choice2 = input("You have reached a lake with an insland in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across to the island.\n").lower()
    if choice2 == "wait":
        #Game will continue
        choice3 = input("Your arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue, which colour do you choose?\n").lower()
        if choice3 == "red":
            print("It's a room full of fire, Game Over.")
        elif choice3 == "yellow":
            print("You found the treasure! You win!!")
        elif choice3 == "blue":
            print("You were attacked by a pack of angry beasts, Game Over.")
        else:
            print("You chose a door that doesn't exist. Game Over.")    
    
    #if choice 2 == swim: Game over - progam will print the following else statement
    else:
        print("You were attacked by a school of angry piranha's! Game Over.")

# if choice1 == right: Game Over - program will print the following else statement
else:
    print("You fell in a hole. Game Over.")