import textwrap

# empty print() is a line break

def wrap_text(width=70):
    return textwrap.fill(width)

# Defined wrap_text function 

# Swamp Area Intro

print(wrap_text("You step into a dark swamp."))
print()
print(wrap_text("The air smells damp and musty. A thick fog covers the ground."))
print()
print(wrap_text("You hear croaking sounds from somewhere."))
print()
print(wrap_text("The trees around you are twisted and dark."))
print()
print(wrap_text("The ground is soft, and your feet sink a little with each step."))
print()
print(wrap_text("There are three paths ahead. The air feels colder as you think about which way to go."))
print()
print(wrap_text("Do you go [l]eft, [r]ight, or [f]orward?"))
print()

# Mutiple choices

while True:   
    direction = input("> ").lower()

# left choice

    if direction == "l":
        print(wrap_text("You turn left."))
        print()
        print(wrap_text("The path gets darker and you feel uneasy."))
        print()
        print(wrap_text("You hear something move behind you. You turn and see glowing eyes before a claw swipes at you."))
        print()
        print(wrap_text("You don't move fast enough. Everything goes black."))
        print()
        print(wrap_text("You are dead."))
        print()
        break
    
    # End of game

# forward choice

    elif direction == "f":
        print(wrap_text("You walk forward."))
        print()
        print(wrap_text("You find a rusty key on the ground."))
        print()
        print(wrap_text("You pick it up."))
        print()
        print(wrap_text("You gain +1 HP!"))
        print()
        print(wrap_text("You see a cave ahead."))
        print()
        print(wrap_text("You enter and find an old chest in the dark."))
        print()
        pass  # Placeholder
    
    # Cave section [Here]

# right choice

    elif direction == "r":
        print(wrap_text("You turn right."))
        print()
        print(wrap_text("The path is narrow, and you hear a faint cry."))
        print()
        print(wrap_text("You rush forward, but it's not a person."))
        print()
        print(wrap_text("A swamp beast stands in front of you, looking terrible."))
        print()
        print(wrap_text("It attacks, slashing at your arm."))
        print()
        print(wrap_text("You lose 2 HP."))
        print()
        print(wrap_text("The beast runs off into the swamp."))
        print()
        print(wrap_text("You keep moving forward."))
        print()
        pass  # Placeholder 
    
    # Cave section [Here]

    else:
        print(wrap_text("Invalid choice! Please type [l], [r], or [f] to proceed."))

