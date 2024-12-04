import textwrap
import time

health = 0
start_health = 0
hooded_figure_health = 10
sword_ap = 1

def printtext(text):
  wrapped_text = textwrap.wrap(text, width=100)
  for line in wrapped_text:
    print(line)

def STAGE_1(health=10):


  text = "The Kingdom of Denethor was once a peaceful and prosperous land, thriving with life and magic. However, \
a mysterious curse now drains its vitality, leaving the kingdom in ruins. The people suffer, and the royal family’s power wanes under the curse’s grip. \
A young adventurer (you) has been summoned by King Denethor to embark on a perilous quest to uncover and defeat the source of the curse. Along the way, \
you will meet allies and enemies, face challenges, and make choices that shape the destiny of Denethor. Will you lift the curse, or will the kingdom fall into eternal darkness? "
  printtext(text)
  time.sleep(1)

  print("")

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
    health = health + 2
  
  print(f"You continue your journey with {health} HP")
  if read_input == 1 or read_input == 2 or read_input == 3:
    print("")
  else:  
    print("you have failed to choose correctly")

text = "Stage 1: The Royal Audience"
printtext(text)
print("")
STAGE_1()

