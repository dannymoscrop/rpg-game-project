#Written by JOHN

  # Import a text wrapper and a pause function
import textwrap
import time

  # Variables
health = 10
start_health = 0
hooded_figure_health = 10
player_attack = 1
go_to_village = 0
go_to_swamp = 0
answer = 3
cave = 0
password = "yes"
key = 0
go_to_ruins = 0
powerful_weapon = 0

  # define a text wrapping function
def printtext(text):
  wrapped_text = textwrap.wrap(text, width=100)
  for line in wrapped_text:
    print(line)

# Written by Lucia - tidies up and made to fit by JOHN
def wrap_text(width=100):
    return textwrap.fill(width)

def stage_4_cave():
    global health
    global key
    global answer
    global powerful_weapon
    password = "key"
    
    print(wrap_text("You journey deeper into Denethor and arrive at the entrance of a dark, foreboding cave. The air is thick with magic, and strange symbols shimmer faintly along the jagged walls."))
    print()
    print(wrap_text("As you step inside, the darkness seems to press against you. In the center of the cave, you find Agnes, a powerful sorceress, bound in enchanted chains and slumped against the rocky wall."))
    print()
    print(wrap_text("Her eyes glint with suspicion as you approach cautiously."))
    print()
    time.sleep(2)
    if answer == 1 and key == 1:
        print(wrap_text("You approach and carefully break the chains binding Agnes. She watches you closely, then speaks."))
        print()
        print(wrap_text("Agnes: Only the pure of heart may earn my aid. Speak the password to prove your intentions"))
        print()
        time.sleep(2)
        print(wrap_text(f"You confidently recite the password you learned earlier. the password is a {password}. Agnes nods approvingly."))
        print()
        time.sleep(2)
        print(wrap_text("Agnes: You have my trust. Now, let me see that key you carry."))
        print()
        time.sleep(2)
        print(wrap_text("You hand her the key you found earlier. Agnes examines it with reverence."))
        print()
        time.sleep
        print(wrap_text("Agnes: This unlocks a mystical chest hidden in the ruins. Inside lies a weapon of great power. It will strengthen you for the battle ahead."))
        print()
        time.sleep(2)
        print(wrap_text("A pulse of magic surges through the cave as she raises her hand."))
        print()
        time.sleep(2)
        powerful_weapon += 1
        print("You received powerful weapon.")
        print()
        time.sleep(2)
        print(wrap_text("Agnes gestures toward the path deeper into the ruins: Go now. The ruins await."))
        print()
        time.sleep(2)

        return
    elif answer == 1 and key == 0:
        print(wrap_text("You step forward and break her chains. Agnes gazes at you with curiosity, then demands proof that you are not one of the Dark Figure's followers."))
        print()
        time.sleep(2)
        print(wrap_text("Agnes: Speak the password, or leave me to my fate."))
        print()
        time.sleep(2)
        print(wrap_text(f"You confidently recite the password you learned earlier: The password is a {password}. Agnes nods approvingly."))
        print()
        time.sleep(2)
        print(wrap_text("Agnes:You are true of heart. My gratitude is yours, brave one. Though I have little to offer, take this blessing to aid you."))
        print(wrap_text("She utters a spell, and you feel a surge of vitality."))
        print()
        time.sleep(2)
        health = health + 1
        print(wrap_text(f"Your HP is now {health}"))
        print()
        time.sleep(2)
        print(wrap_text("With a respectful bow, she gestures toward the path leading deeper into the ruins."))
        print()
        time.sleep(2)
        return
    else:
        print(wrap_text("You cautiously break the chains restraining Agnes. She rises slowly, her gaze sharp and full of distrust."))
        print()
        time.sleep
        print(wrap_text("Agnes: You’ve freed me, but actions are not always proof of intent. Speak the password and prove yourself."))
        print()
        time.sleep(1)
        print("You hesitate, unable to answer her demand. Agnes frowns and steps back, her demeanor cold.")
        print()
        time.sleep(2)
        print("Agnes: I cannot trust you. Go, and may fortune guide you, though I can offer you nothing more.")
        print()
        time.sleep(2)
        time.sleep(2)
        print("YWithout another word, she retreats into the shadows. You are left alone to face the dangers ahead...")
        print()
        time.sleep(2)

    
# Written by Daniel - Variables chnged to fit by JOHN
def swamp():
  global health
  global cave
  global key
# Swamp Area Intro
  print(wrap_text("You step into a dark swamp."))
  print()
  time.sleep(1)
  print(wrap_text("The air smells damp and musty. A thick fog covers the ground."))
  print()
  time.sleep(3)
  print(wrap_text("You hear croaking sounds from somewhere."))
  print()
  time.sleep(3)
  print(wrap_text("The trees around you are twisted and dark."))
  print()
  time.sleep(3)
  print(wrap_text("The ground is soft, and your feet sink a little with each step."))
  print()
  time.sleep(3)
  print(wrap_text("There are three paths ahead. The air feels colder as you think about which way to go."))
  print()
  time.sleep(3)
  print(wrap_text("Do you go [l]eft, [r]ight, or [f]orward?"))
  print()

# Mutiple choices

  while True:   
    direction = input("> ").lower()

# left choice

    if direction == "l":
        print(wrap_text("You turn left."))
        time.sleep(1)
        print()
        print(wrap_text("The path gets darker and you feel uneasy."))
        time.sleep(3)
        print()
        print(wrap_text("You hear something move behind you. You turn and see glowing eyes before a claw swipes at you."))
        time.sleep(3)
        print()
        print(wrap_text("You don't move fast enough. Everything goes black."))
        time.sleep(3)
        print()
        print(wrap_text("You are dead."))
        time.sleep(3)
        print()
        break
    
    # End of game

# forward choice

    elif direction == "f":
        print(wrap_text("You walk forward."))
        time.sleep(1)
        print()
        print(wrap_text("You find a rusty key on the ground."))
        time.sleep(3)
        print()
        print(wrap_text("You pick it up."))
        time.sleep(3)
        print()
        print(wrap_text("You gain +1 HP!"))
        time.sleep(3)
        print()
        print(wrap_text("You see a cave ahead."))
        time.sleep(3)
        print()
        print(wrap_text("You enter and find an old chest in the dark."))
        time.sleep(3)
        print()
        cave = 1
        health = health + 1
        key = 1
        return
        pass  # Placeholder
    
    # Cave section [Here]

# right choice

    elif direction == "r":
        print(wrap_text("You turn right."))
        time.sleep(1)
        print()
        print(wrap_text("The path is narrow, and you hear a faint cry."))
        time.sleep(3)
        print()
        print(wrap_text("You rush forward, but it's not a person."))
        time.sleep(3)
        print()
        print(wrap_text("A swamp beast stands in front of you, looking terrible."))
        time.sleep(3)
        print()
        print(wrap_text("It attacks, slashing at your arm."))
        time.sleep(3)
        print()
        print(wrap_text("You lose 2 HP."))
        time.sleep(3)
        print()
        print(wrap_text("The beast runs off into the swamp."))
        time.sleep(3)
        print()
        print(wrap_text("You keep moving forward."))
        time.sleep(3)
        print()
        health = health - 2
        cave = 1
        return
        pass  # Placeholder 
    
    # Cave section [Here]

    else:
        print(wrap_text("Invalid choice! Please type [l], [r], or [f] to proceed."))

#Written by James - code changed in places to fit into game by JOHN
def village():
  global health
  global answer
  global cave
  text = "You head out of the castle and back towards the village. It is eerily quiet apart the the tapping of a \
  blind womans stick. Her glossy eyes seem to peer into your soul. Speaking as if she knows everything you have ever \
  done. Yes… Yes… I see what you will do. Your path diverges here hero. Answer my riddle and I will show you the way forwards."
  printtext(text)

  text = "I open locks yet hold no teeth, Silent I stand, with secrets beneath. Though I am small, I hold great might, \
  To open doors and grant you sight. What am I?"
  printtext(text)

  #while True:

  answer = input(" > ").lower()
  if answer == "key":
    print("Very good. Go down that path through the swamp, there is a key, if you find it you will be able to claim our Kingdoms sacred sword.") 
    answer = 1
    health = health + 1
  else: 
    print("I am afraid not, the cave is down that path. But are you prepared?")
    answer = 0
    health = health - 2
    cave = 1

  return

# Written by JOHN

  # define the stage_1 function

def STAGE_1():
  
  # Make variables used in this function .. global

  global health
  global go_to_village
  global go_to_swamp

  # displayed text with text formtting and wait functions

  text = "The Kingdom of Denethor was once a peaceful and prosperous land, thriving with life and magic. However, \
a mysterious curse now drains its vitality, leaving the kingdom in ruins. The people suffer, and the royal family’s power wanes under the curse’s grip. \
A young adventurer (you) has been summoned by King Denethor to embark on a perilous quest to uncover and defeat the source of the curse. Along the way, \
you will meet allies and enemies, face challenges, and make choices that shape the destiny of Denethor. Will you lift the curse, or will the kingdom fall into eternal darkness? "
  printtext(text)
  time.sleep(1)

  text = "You stand in the grand throne room of Castle Denethor. \
King Denethor, frail and aged, sits on his ornate throne, his crown slightly askew. He looks at you with weary but hopeful eyes. \
King Denethor: We need a hero to face the unknown and save Denethor. Will you take up this burden?"
  printtext(text)

  # User inputs

  print ("")
  print ("")
  print("1. Agree to Help")
  print("2. Ask for more information")
  print("3. Refuse")

  read_input = int(input("Please choose an option:   "))
 
  # If statements to "do something" based off user input

  if read_input == 1:
    print("")
    print("")
    time.sleep(1)
    print("You have chosen option 1:")
    time.sleep(0.5)
    print("")
    print("Your Majesty, I will do all I can to lift this curse.")
    time.sleep(0.5)
    print("")
    text = "The king is relieved, and with his wishes of good luck, you part ways. However, searching for clues \
costs you -2 HP"
    printtext(text)
    print("")
    go_to_swamp = 1
    health = health -2

  if read_input == 2:
    print("")
    print("")
    time.sleep(1)
    print("You have chosen option 2:")
    time.sleep(0.5)
    print("")
    print("What do you know about the curse? Who or what is behind it?")
    time.sleep(0.5)
    print("")
    text = "Outcome: The king explains that the curse began many years ago after the disappearance of Agnes, \
  a powerful sorceress who attempted to combat it. Rumours suggest a Hooded Figure in the eastern ruins is responsible"
    printtext(text)
    print("")
    go_to_village = 1
    health = health + 2
  
  if read_input == 3:
    print("")
    time.sleep(1)
    print("You have chosen option 3:")
    time.sleep(0.5)
    print("")
    print("I’m sorry, Your Majesty. This is too great a task for me")
    time.sleep(0.5)
    print("")
    text = ("The king looks devastated, and you leave the throne room. The kingdom’s fate grows darker without your \
intervention. ")
    printtext(text)
    print("")
    print("END GAME")
    exit(1)

  print(f"You continue your journey with {health} HP")

  if read_input == 1 or read_input == 2 or read_input == 3:
    print("")
  else:  
    print("you have failed to choose correctly")


  # This is where we start. Variables are taken from each defined function as the code progresses

text = "Stage 1: The Royal Audience"
printtext(text)
print("")
STAGE_1()

if go_to_village == 1:
  village()
  print(f"exit the village with {health}")

if answer == 1:
  print(f"To the swamp we go with {health} health")
  swamp()
if answer == 0:
  print(f"to the cave we go with {health} health")

if go_to_swamp == 1:
  print("")
  swamp()

if cave == 1:
  print (f"to the cave we go with {health} health")
  stage_4_cave()
  print (f"to the final battle with {health} health")

print ("")
print("THE GAME HAS ENDED")
