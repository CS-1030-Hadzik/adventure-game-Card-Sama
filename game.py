'''
    DOCSTRING Section
Adventure Game
Author: Stephen Yount
Version: 1
Description:
This is a text-based adventure game where the player makes choices
to navigate through a mysterious forest.
'''
#------------------------------------------- player
class Player:
    def __init__(self, name):
        self.name = name
        self.inventory = []
        self.health = 10
        self.has_map = False
        self.has_lantern = False

#Player's inventory Section ---------------- i
def add_to_inventory(player, item):
    # Add an item to the player's inventory
    player.inventory.append(item)
    print(f"You picked up {item}!")

#--------------------------
#Player Modifiers
#--------------------------
    #Stay still
def stay_still(player):
    print("You stay still, you feel as if you are being watched.")
    print("It starts to get to you.")
    player.health -= 10
    print(f"{player.name}, your health is now {player.health}.")

#------------
# Areas
#------------
#--------------------------
#          Dark Woods----------------------- 1
#--------------------------
def explore_dark_woods(player):
        print(f"{player.name}, you step into the dark woods."
              "The trees whisper as walk deeper.")
        add_to_inventory(player, "Lantern")
        player.has_lantern = True
#--------------------------
#          Mountain Pass-------------------- 2
#--------------------------
def explore_mountain_pass(player):
        print(f"{player.name}, you make your way "
              "towards the mountain pass, feeling "
              "the cold wind against your face.")
        add_to_inventory(player, "Map")
        player.has_map = True
#--------------------------
#          Cave----------------------------- 3
#--------------------------
def explore_cave(player):
        print("You walk up to the entracne of the cave."
        "It appears to be dark inside.")

                #Yes lantern:
        if player.has_lantern == True:
            print(f"{player.name} you bravely enter the cave")
            print("Inside the cave, you find a treasure chest!")
            add_to_inventory(player, "Treasure")

                #No lantern
        if player.has_lantern == False:
            print("You can't see far enough to travel safely.")
            print("You need a light source to explore further.")
            print("You feel a precence approaching.")
            print("As fear consomes you, you run away.")
            print("You trip from running away")
            player.health -= 10
#--------------------------
#          Hidden Valley-------------------- 4
#--------------------------
def explore_hidden_valley(player):
        print("You search for a place called hidden valley.")

        if player.has_map == True:
            print("You find a hidden valley, "
                  "a place of beauty and tranquility.")
            print("You can rest here and regain your strength.")
            player.health = 100
            print("Your health is now full.")
            print("You find a treasure chest!")
            add_to_inventory(player, "Rare Herbs")
            print("You have found rare herbs.")

        if player.has_map == False:
            print("You can't seem to find Hidden Valley.")
            print("You may need guidance of some kind.")       
            player.health -= 10  
#--------------------------
#          Win/Lose Conditions-----------------------------------------------
#--------------------------
def check_win(player):
    return "Treasure" in player.inventory and "Rare Herbs" in player.inventory

def check_lose(player):
    return player.health <= 0
#--------------------------
# Main Game --------------------------------------------------------------------
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

    print("\t3. Go to the entrance of a near by.")

    print("\t4. Search for hidden valley")

    print("\t5. Stay where you are.")

    print("\tType 'i' to view your inventory.")

    print("\tCurrent Health: {player.health}")

    decision = input("What will you do (1,2,3, 4, 5, I or F): ").lower()


    if decision == "i":
        print("Inventory" , player.inventory)
        continue

# dark woods choice


#Forest Choice
    if decision == "1":
        explore_dark_woods(player)


#Mountain choice 
    elif decision == "2":
        explore_mountain_pass(player)


#Cave choice
    elif decision == "3":
        explore_cave(player)


    # Hidden Valley Choice
    elif decision == "4":
        explore_hidden_valley(player)


#Stay where you are
    elif decision == "5":
        print("You stay still, listening to the "
              "distant sounds of the forest")
        stay_still(player)


    else:
        print("Invalid choice. Please choose "
              "1, 2, 3, 4, 5, I, or F.")

#-------------------------- win 
    if check_win(player):
        print(f"\nCongratulations {player.name}! You have found both the treasure and the rare herbs.")
        print("You are victorious and can now leave the forest.")
        break

#--------------------------- lose
    if check_lose(player):
        print(f"\n{player.name}, you have ran out of health. Your adventure ends here....")
        break





    # Ask if they want to continue
    play_again = input("Do you want to continue "
                       "exploring? (yes or no): ").lower()
    if play_again != "yes":
        print(f"Thanks for playing, {player.name} "
              "See you next time.")
        break  # Exit the loop and end the game

