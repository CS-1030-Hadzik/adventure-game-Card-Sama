'''
    DOCSTRING section
Adventure Game
Author: Stephen Yount
Version: 1.0
Description:
This is a text-based adventure game where the player makes choices
to navigate through a mysterious forest.
'''


# Welcome message and introduction
print("Welcome to the Adventure Game!")  
print('Your journey begins here...')

# Ask for the player's name
player_name = input ("what is your name, adventurere? ")

# Concatenate strings to create a personalized message
print("Wlecome " + player_name + ", Your journey begins now!")

# Use an f-string to display the same message in a more readable way
# print(f"Welcome {player_name}, Your journey begins now!")

#Describe the starting area
starting_area ="""
You find yourself in a dark forest.
The sound of rustling leaves fills the air.
A faint path lies ahead, leading deeper into the
unknown...
"""

print(starting_area)

#Ask the player for their first decision
decision = input("Do you wish to take the path? (yes or no): ").lower()

#Respond to player based on choice
if decision == "yes":
    print(f"Brave choice{player_name}! You step onto the path and venture forward!")

#No decision section, goal is to have this section print and cylce back to option or force close game, which eveer one fits better.

elif decision == "no":
    print(player_name+ ", you decide to wait. Perhaps courage will find you later.") # Concatenation example")
    print("Hours pass and the sun sets. You lay down under a tree and wake up the next day faced with a decision...")


#Not valid answer section
else: 
    print("Confused, you stand still, unsure of what to do.")
