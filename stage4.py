
import textwrap
import time

health = 10
hooded_figure_health = 10

answer = 1
cave = 0
key = 1
powerful_weapon = 0

def printtext(text):
  wrapped_text = textwrap.wrap(text, width=100)
  for line in wrapped_text:
    print(line)

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

    print(wrap_text("Proceed to stage 5: The Ruins"))
    
stage_4_cave()