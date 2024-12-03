from random import randint

player_health = 14
hooded_figure_health = 10
game_running = True

def begin_game():
  while game_running:
    print("Hero attack")
        
    if hero_choice == 1:
      player_attack_damage = randint(1, 4)
      print(f"{hero_name} attack for {player_attack_damage}")
      

