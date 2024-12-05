
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
    
    print(wrap_text("Stage 4: The Cave"))
    print()
    print(wrap_text("You arrived at the entrance of dark cave. Inside you find Agnes, the powerful witch. She asks you for password"))
    print()
    time.sleep(2)
    if answer == 1 and key == 1:
        print(wrap_text(f"The password is {password}. I have also found a key in the swamp, maybe you can tell me what it opens"))
        print()
        time.sleep(2)
        print(wrap_text("She will point at chest in the dark corner of the cave and explains that the key opens the chest.You will get powerful weapon, which  will help you to defeat the hooded figure"))
        print()
        time.sleep(2)
        powerful_weapon += 1
        print("You received powerful weapon.")
        print()
        time.sleep(2)
        return
    elif answer == 1 and key == 0:
        print(wrap_text(f"The password is {password}."))
        print()
        time.sleep(2)
        print(wrap_text("As a token  I will grant you healing spell"))
        health = health + 1
        print()
        time.sleep(2)
        print(wrap_text(f"Your HP is now {health}"))
        print()
        time.sleep(2)
        return
    else:
        print(wrap_text("I have no password"))
        print()
        time.sleep
        print(wrap_text("She distrust you and refused to help you further"))
        print()
        time.sleep(1)

    print(wrap_text("Proceed to stage 5: The Ruins"))
    
stage_4_cave()