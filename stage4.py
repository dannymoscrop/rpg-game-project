player_hp = 11

def stage_4_cave(player_hp):
    has_key = False
    has_password = "key"

    print("\nStage 4: The Cave")
    print("You arrived at the entrance of dark cave. Inside you find Agnes, the powerful witch. She asks you for password")

    if has_password and has_key:
        print(f"The password is {has_password}. I have also found a key in the swamp, maybe you can tell me what it opens")
        print("She will point at chest in the dark corner of the cave and explains that the key opens the chest.You will get powerful weapon, which  will grant you +2 damage bonus in next stage")
    elif has_password and not has_key:
        print(f"The password is {has_password}.")
        print("As a token  I will grant you healing spell")
        player_hp += 1
        print(f"Your HP is now {player_hp}")
    else:
        print("I have no password")
        print("She distrust you and refused to help you further")

    print("Proceed to stage 5: The Ruins")
    return player_hp

stage_4_cave(player_hp)
