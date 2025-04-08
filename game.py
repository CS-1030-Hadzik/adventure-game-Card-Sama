'''
    DOCSTRING Section
Adventure Game
Author: Stephen Yount
Version: 0.4
Description:
This is a text-based adventure game where the player makes choices
to navigate through a mysterious forest.
'''
#
class Player:
    def __init__(self, name):
        self.name = name
        self.inventory = []
        self.health = 100
        self.has_map = False
        self.has_lantern = False

#Player's inventory Section
inventory = []
def add_to_inventory(item):
    # Add an item to the player's inventory
    inventory.append(item)

#--------------------------
# Function: Welcome_player
# Greets the player, asks for their name,
# and returns the name as a string
#--------------------------
def welcome_player():
    # Welcome message and introduction
    print("Welcome to the Adventure Game!")  
    print('Your journey begins here...')


    # Ask for the player's name
    name = input("What is your name, adventurer? ")
    player = Player(name)


    # Concatenate strings to create a personalized message
    print("Welcome " + player.name + ", Your journey begins now!")
    # Use an f-string to display the same message in a more readable way
    # print(f"Welcome {player.name}, Your journey begins now!")
    return player


# Call the welcome_player function and store the player's name
#Describe the starting area
#Function: describe_area
# Print the opening description of the area
player = welcome_player()
def describe_area():
    # Description of the starting area
    starting_area = """
    You find yourself in a dark forest.
    The sound of rustling leaves fills the air.
    A faint path lies ahead, leading deeper into the
    unknown...
    """
    print(starting_area)


# Start the game Loop
while True:
    print("\nYou see mutiple places ahead:")

    print("\t1. You go towards the Dark Woods.")

    print("\t2. Take the left path into the dark woods.")

    print("\t3. Take the right path toward the mountain pass.")

    print("\t4. Go to the entrance of a near by.")

    print("\t5. Search for hidden valley")

    print("\t6. Stay where you are.")

    print("\tType 'i' to view your inventory.")

    decision = input("What will you do (1,2,3, 4, 5, 6 or I): ").lower()


    if decision == "i":
        print("Inventory" , inventory)
        continue

# daek woods choice
    if decision == "1":
        print(f"{player.name}, you step into the dark woods."
              "The trees whisper as you approach.")
        add_to_inventory("Lantern")
        player.has_lantern = True
#def explore_dark_woods():
    print(f"{player.name}, you step into the dark woods...")

    if 'lantern' not in player.inventory:
        add_to_inventory(player,"lantern")
        player.has_lantern == True

    else:
        print("You've already found the lantern here.")


#Forest Choice
    if decision == "2":
        print(f"{player.name}, you step into the dark woods."
              "The trees whisper as walk deeper.")
        add_to_inventory("Lantern")
        player.has_lantern = True


#Mountain choice 
    elif decision == "3":
        print(f"{player.name}, you make your way "
              "towards the mountain pass, feeling "
              "the cold wind against your face.")
        add_to_inventory("Map")
        player.has_map = True


#Cave choice
    elif decision == "4":
        print("You walk up to the entracne of the cave."
        "It appears to be dark inside.")


        # if player.has_lantern:
        if player.has_lantern == True:
            print(f"{player.name} you bravely enter the cave")
            print("Inside the cave, you find a treasure chest!")
            add_to_inventory("Treasure")


        if player.has_lantern == False:
            print("You can't see far enough to travel safely.")
            print("You need a light source to explore further.")


    # Hidden Valley Choice
    elif decision == "5":
        print("You search for a place called hidden valley.")

        if player.has_map == True:
            print("You find a hidden valley, "
                  "a place of beauty and tranquility.")
            print("You can rest here and regain your strength.")
            player.health = 100
            print("Your health is now full.")
            print("You find a treasure chest!")
            add_to_inventory("Rare Herbs")
            print("You have found rare herbs.")

        if player.has_map == False:
            print("You can't seem to find Hidden Valley.")
            print("You may need guidance of some kind.")



#Stay where you are
    elif decision == "6":
        print("You stay still, listening to the "
              "distant sounds of the forest")


    else:
        print("Invalid choice. Please choose "
              "1, 2, 3, 4, 5, 6 or I.")

    # Ask if they want to continue
    play_again = input("Do you want to continue "
                       "exploring? (yes or no): ").lower()
    if play_again != "yes":
        print(f"Thanks for playing, {player.name} "
              "See you next time.")
        break  # Exit the loop and end the game

