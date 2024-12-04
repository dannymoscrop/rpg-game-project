import time
import textwrap

# empty print() is a line break

def wrap_text(width=100):
    return textwrap.fill(width)

# Defined wrap_text function 

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
        pass  # Placeholder 
    
    # Cave section [Here]

    else:
        print(wrap_text("Invalid choice! Please type [l], [r], or [f] to proceed."))

