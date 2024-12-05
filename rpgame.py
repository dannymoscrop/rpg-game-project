from random import randint
import textwrap
import time

health = 10
start_health = 0
hooded_figure_health = 10
powerul_weapon = 0

def printtext(text):
  wrapped_text = textwrap.wrap(text, width=100)
  for line in wrapped_text:
    print(line)

def wrap_text(width=100):
    return textwrap.fill(width)

def final_battle():
   global health
   global hooded_figure_health


   print(wrap_text("The ruins rise before you, ancient and desolate, cloaked in mist and an eerie silence. You step cautiously into the remains of an ancient temple, its broken walls carved with dark runes that glow faintly with a malevolent light. The air is heavy, charged with the remnants of forgotten magic.."))
   print()
   time.sleep(2)
   print(wrap_text("The rumors of the Hooded Figure's power echo in your mind, mingling with the doubt creeping into your thoughts. Fear and fatigue threaten to cloud your resolve, and you hesitate, uncertain of your next move."))
   print()
   time.sleep(1)        
   print(wrap_text("The choice is yours to make: to fight the shadowy figure and risk everything or retreat and let Denethor fall to darkness forever..."))
   print()
   time.sleep(2)

   print("fight")
   print("retreat")
   print()
   hero_choice = input("What will you do? >").lower()

   if hero_choice == "retreat":
      print()
      print(wrap_text("Overwhelmed by exhaustion and fear, you turn away from the ruins. Doubt gnaws at your resolve, whispering that you are not strong enough."))
      print()
      time.sleep(1)
      print(wrap_text("You take one last look at the crumbling temple, its secrets hidden in shadow, and make your decision. You abandon Denethor to its fate, hoping that someone else might rise to the challenge before it’s too late."))
      print()
      time.sleep(1)
      print(wrap_text("The echoes of your footsteps fade into the silence as the darkness spreads. The kingdom succumbs to the curse, a grim reminder of your choice..."))
      print()
      time.sleep(1)
      print("Game over.")
      exit()
      
   else:
      print(wrap_text("Despite the exhaustion weighing down your body, the fear creeping into your thoughts, and the relentless self-doubt clouding your resolve, you choose to press on. Turning back is not an option—not when the fate of Denethor hangs in the balance."))
      print()
      time.sleep(1)
      print(wrap_text("You are the kingdom's last hope, the final chance to break the curse."))
      print()
      time.sleep(1)
      print(wrap_text("At the center of the crumbling chamber, a Hooded Figure stands waiting, their presence radiating malice. They turn toward you, their voice dripping with contempt."))
      print()
      time.sleep(1)
      print(wrap_text("Hooded Figure: So, you have come at last. Foolish mortal, do you truly believe you can undo the work of centuries? You will find only despair here."))
      print()
      time.sleep(1)
      print(wrap_text("The stage is set. There is no turning back now."))
      print()
      time.sleep(1)
      print(f"Your HP is now {health}")

   while health > 0 and hooded_figure_health > 0:
         
      input("Press Enter to continue")
            
      player_attack_damage = randint(1, 4)
      hooded_figure_health -= player_attack_damage
      print()
      time.sleep(1)
      print(f"You attack hooded figure for {player_attack_damage}")
      print(f"Hooded figure damage is now {hooded_figure_health}")
    
      if hooded_figure_health <= 0:
        break

      hooded_figure_attack = randint(1, 4)
      health -= hooded_figure_attack
      print(f"Hooded figure attacked you for {hooded_figure_attack} ")
      print(f"Your HP is now {health}")
    
      if health <= 0:
        break

   if health > 0 and powerul_weapon == 1:
      print()
      print(wrap_text("With a final blow of your mystical weapon, glowing as it strikes, you vanquish your enemy. The darkness dissipates, and the curse is lifted."))
      print()
      time.sleep(1)
      print(wrap_text("The Kingdom of Denethor is saved, its people free from the shadow that plagued them."))
      print()
   elif health > 0:
      print()
      print(wrap_text("The battle is grueling, each swing of your blade and each spell you cast a desperate attempt to hold your ground. After a tough fight, you defeat the Hooded Figure, but it comes at a cost."))
      print()
      time.sleep(1)
      print(wrap_text("The curse is broken, but its lingering effects leave scars on the kingdom."))
      print()
      time.sleep(1)
      print(wrap_text("Denethor survives, but its lands and people remain forever changed by the darkness."))
      print()
   else:
      print()
      print(wrap_text("Your strength fails, and the Hooded Figure’s dark magic overwhelms you. Their laughter echoes as you fall, powerless to stop the tide of destruction."))
      print()
      time.sleep(1)
      print(wrap_text("The ruins collapse, and darkness engulfs Denethor."))
      print()
      time.sleep(1)
      print(wrap_text("The Kingdom of Denethor is lost, consumed by the Hooded Figure’s evil."))
      print()
      
final_battle()
