import textwrap
import time

health = 10
start_health = 0
hooded_figure_health = 10
sword_ap = 1

go_to_village = 0
go_to_swamp = 0
answer = 3

def printtext(text):
  wrapped_text = textwrap.wrap(text, width=100)
  for line in wrapped_text:
    print(line)

def village():
  global health
  global answer
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

  return

def STAGE_1():
  
  global health
  global go_to_village
  global go_to_swamp

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

  print ("")
  print ("")
  print("1. Agree to Help")
  print("2. Ask for more information")
  print("3. Refuse")

  read_input = int(input("Please choose an option:   "))
 
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
costs you -2 HP, as you have no prior information. Eventually, you hear a rumour about a monster guarding the parchment that reveals Agnes's location."
    printtext(text)
    print("")
    print("You proceed to the swamp")
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
    print("You proceed to the VILLAGE with +2 HP")
    go_to_village = 1
    health = health + 2
  
  if read_input == 3:
    print("")
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
  #health_exit_1 = health
  if read_input == 1 or read_input == 2 or read_input == 3:
    print("")
  else:  
    print("you have failed to choose correctly")


#START
text = "Stage 1: The Royal Audience"
printtext(text)
print("")
STAGE_1()
print(f"health - {health}")

if go_to_village == 1:
  print(f"to the village we go with {health} points")
  village()
  print(f"exit the village with {health}")

if answer == 1:
  print(f"To the swamp we go with {health} health")
if answer == 0:
  print(f"to the cave we go with {health} health")

if go_to_swamp == 1:
  print(f"to the swamp we go with {health} health")

