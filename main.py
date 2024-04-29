import random
import time
attributes = ["strength", "dexterity", "intelligence", "wisdom", "charisma", "constitution", "perception"]
attributes_dict = {
  "strength": 0,
  "dexterity": 0,
  "intelligence": 0,
  "wisdom": 0,
  "charisma": 0,
  "constitution": 0,
  "perception": 0
}
#Start of the game
print("WELCOME TO THE DUNGEON\n\n")
print("Home of the evil wizard," "MRS NELSON")
print("And his accomplice," "JAMES MEADOWS\n")
print( "The villiage has tasked you with entering the dungeon and slaying the wizard to stop him from terrorizing the villiage.  You, the brave adventurer, have accepted this task.")
print("\nLoading...\n")
time.sleep(5)
print("\nIt is time to create your character.")
#Gets the name
name = input("\nFirst, what would you like to name your character? ")
print(f"\nGreetings, {name.title()}. It is now time to determine your traits. First you will roll a  20-sided die, and then you will assign it to a certain trait.")
def assign_choice(response):
  if int(response) < 8:
    if attributes_dict[attributes[int(response.strip()) - 1]] == 0:
        attributes_dict[attributes[int(response.strip()) - 1]] = choice
        print(f"So your character's {attributes[int(response.strip()) - 1]} will be {choice}")
        time.sleep(0.8)
        print("\nRolling next dice...\n")
        time.sleep(0.8)
    else:
      second_response = input(f"You already have a value for {attributes[int(response.strip()) - 1]}. Choose another: ")
      assign_choice(second_response)
  else:
    third_response = input("Please choose a number between 1 and 7: ")
    assign_choice(third_response)
# Rendering the list of attributes
print("\nHere are the attributes you can choose from: ")
for i in range(len(attributes_dict)):
  print(f"{i + 1}. {attributes[i].title()}")
for i in range(len(attributes_dict)):
  choice = roll(9, 18)
  if i < len(attributes_dict) - 1:
    if i == 0:
      print(f"\nONLY ENTER NUMBERS 1 - 7!")
      print("\nRolling first dice...\n")
    time.sleep(0.8)
    print(f"You rolled {choice}.")
  else:
    print(f"Your final roll is {choice}.")
    last_attribute = ""
    for i in range(len(attributes_dict)):
      if attributes_dict[attributes[i]] == 0:
        last_attribute = attributes[i]
        attributes_dict[attributes[i]] = choice
    print(f"Your last available attribute is {last_attribute}. {choice} assigned to {last_attribute}.")
    break
  response = input(f"To which trait would you like to assign {choice} to? ")
  assign_choice(response)
# Rendering the assigned attributes
print("\nYour attributes are:\n")
for i in range(len(attributes_dict)):
  print(f"{attributes[i].title()}: {attributes_dict[attributes[i]]}")

