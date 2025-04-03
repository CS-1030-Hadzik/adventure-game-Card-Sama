'''
    DOCSTRING Section
Adventure Game
Author: Stephen Yount
Version: 1.0
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
    print("\t1. Take the left path into the dark woods.")
    print("\t2. Take the right path toward the mountain pass.")
    print("\t3. Stay where you are.")
#    print("\t4. Go to the entrance of a cave between the paths.")
    print("\tType 'i' to view your inventory.")


    decision = input("What will you do (1,2,3 or I): ").lower()

    if decision == "i":
        print("Inventory" , inventory)
        continue

    if decision == "1":
        print(f"{player.name}, you step into the dark woods."
              "The trees whisper as walk deeper.")
        add_to_inventory("Lantern")
        player.has_lantern = True

    elif decision == "2":
        print(f"{player.name}, you make your way "
              "towards the mountain pass, feeling "
              "the cold wind against your face.")
        add_to_inventory("Map")
        player.has_map = True

    elif decision == "3":
        print("You stay still, listening to the "
              "distant sounds of the forest")
        
    elif decision == "4":
        print("You walk up to the entracne of the cave."
        "It appears to be dark inside.")
        # if player.has_lantern == False:
        #     print("You can not see far enough to salfly travel inside.")
        # if player.has_lantern:
        #     print("You use your lantern to light the way.")

    else:
        print("Invalid choice. Please choose "
              "1, 2, or 3.")

    # Ask if they want to continue
    play_again = input("Do you want to continue "
                       "exploring? (yes or no): ").lower()
    if play_again != "yes":
        print(f"Thanks for playing, {player.name} "
              "See you next time.")
        break # Exit the loop and end the game

