from random import randint

player_hp = 14
monster_hp = 10
game_running = player_hp > 0 and monster_hp > 0

def final_battle(player_hp, monster_hp):
  while game_running:
    
    input("Press Enter to continue")
            
    player_attack = randint(1, 4)
    monster_hp -= player_attack
    print(f"You attack hooded figure for {player_attack}")
    print(f"Hooded figure damage is now {monster_hp}")
    
    if monster_hp <= 0:
      break

    monster_attack = randint(1, 4)
    player_hp -= monster_attack
    print(f"Hooded figure attacked you for {monster_attack} ")
    print(f"Your HP is now {player_hp}")
    
    if player_hp <= 0:
      break

if player_hp > 4:
  print("It's a win")
elif player_hp <= 0:
  print("Defeat")
else:
  print("It's a win, but...")
