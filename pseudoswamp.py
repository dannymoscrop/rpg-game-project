import textwrap

# empty print() is a line break

def wrap_text(width=70):
    return textwrap.fill(width)

# Defined wrap_text function 

# Swamp Area Intro
print(wrap_text("You step into the murky depths of a dark, gloomy swamp."))
print()
print(wrap_text("The air is thick with the stench of damp earth and rotting vegetation, and an eerie fog clings to the ground, making it difficult to see more than a few feet ahead."))
print()
print(wrap_text("The faint croaking of unseen creatures echoes in the distance, adding to the oppressive silence that weighs on you."))
print()
print(wrap_text("Around you, the twisted silhouettes of gnarled trees loom like silent figures"))
print()
print(wrap_text("The ground beneath your feet is soft and uneven, each step sinking slightly into the soggy muck."))
print()
print(wrap_text("Before you, three paths lie ahead, each one leading deeper into the swamp's heart. The air grows colder as you consider your options."))
print()
print(wrap_text("Do you venture [l]eft into the shadowy unknown, [r]ight towards a distant sound, or [f]orward, where the path seems less treacherous but just as uncertain?"))
print()

# Mutiple choices

while True:   
    direction = input("> ").lower()

# left choice

    if direction == "l":
        print(wrap_text("You turn left."))
        print()
        print(wrap_text("The path ahead grows darker, and you venture deeper into a shadowy section of the swamp."))
        print()
        print(wrap_text("A feeling of unease settles over you as you press on, the sounds of something large moving in the darkness growing louder."))
        print()
        print(wrap_text("Suddenly, you hear a rustling behind you. You spin around just in time to see a pair of glowing red eyes before a massive claw swipes at you."))
        print()
        print(wrap_text("You can't react fast enough. The last thing you hear is the sound of a monstrous roar as everything goes black."))
        print()
        print(wrap_text("You are dead."))
        print()
        break
    
    # End of game

# forward choice

    elif direction == "f":
        print(wrap_text("You walk forward."))
        print()
        print(wrap_text("The swamp seems endless, but your steps lead you to something unexpected—a small, rusted key lying on the damp ground."))
        print()
        print(wrap_text("You decide to pick it up, the cold metal pressing against your palm."))
        print()
        print(wrap_text("You feel a small surge of strength as you gain +1 HP!"))
        print()
        print(wrap_text("Continuing your journey, you eventually spot the entrance to a dark cave looming ahead."))
        print()
        print(wrap_text("You step inside, and your eyes adjust to the dim light, revealing a weathered chest tucked away in the shadows."))
        print()
        pass  # Placeholder
    
    # Cave section [Here]

# right choice

    elif direction == "r":
        print(wrap_text("You turn right."))
        print()
        print(wrap_text("You walk cautiously down a narrow path, the air thick with tension, until you hear a faint cry—someone is in pain."))
        print()
        print(wrap_text("Your heart races as you rush forward, hoping to help, but as you approach, you realize your mistake."))
        print()
        print(wrap_text("The sound was not from a human, but a terrifying swamp beast, its body grotesquely twisted and cursed."))
        print()
        print(wrap_text("Without hesitation, you face the creature, ready to fight, but luck is on your side."))
        print()
        print(wrap_text("The curse has already twisted its host beyond recognition, the flesh rotting and ravaged from weeks of torment."))
        print()
        print(wrap_text("The beast strikes with deadly force, slashing at your arm, but you narrowly dodge the brunt of its attack."))
        print()
        print(wrap_text("The attack reduces your health by 2hp!"))
        print()
        print(wrap_text("Wounded and weakened, the creature roars in frustration before retreating into the murky shadows of the swamp."))
        print()
        print(wrap_text("You exhale deeply, the adrenaline still pumping."))
        print()
        print(wrap_text("With no time to waste, you continue moving forward, knowing there's no turning back."))
        print()
        pass  # Placeholder 
    
    # Cave section [Here]

    else:
        print(wrap_text("Invalid choice! Please type [l], [r], or [f] to proceed."))

