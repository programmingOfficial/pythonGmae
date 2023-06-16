import time
import random


def print_pause(*txt):
    # This function is given a parameter of *txt which means that you can give it any number of strings and it will print them
    for t in txt:
        print(t)
        time.sleep(1)


def door():
    # This function describes what happens when approaching the house and has input validation to give you a chance to choose the correct choice from 1 and 2
    print_pause("Knock knock knock", "Who is knocking the door?")
    print_pause("The door opens", "Who is knocking the door?")
    print_pause("OH NOO!", "IT'S A WITCH!")
    print_pause("You have two options: 1) Attack with the magic wand, 2) Run away")

    while True:
        try:
            d = int(input(""))
            if d in [1, 2]:
                return d
            else:
                raise ValueError
        except ValueError:
            print_pause("Invalid input! Please enter 1 or 2.")


def attack(keyword):
    # This function shows what happens when attacking in the cave or in the house
    # The parameter "keyword" differentiates the house attack from the cave attack
    if keyword == "cave":
        print_pause("Now you threw the magic spell")
        return True
    elif keyword == "house":
        print_pause("Now you are using the magic wand")
        return True
    else:
        return False


def lose(keyword):
    # This function shows what happens after losing in the cave or in the house
    # The parameter "keyword" differentiates the house loss from the cave loss
    # It also has input validation to give you a chance to choose the correct choice from 1 and 2
    print_pause("Now you are running away from", keyword, "and failed to save the village",
                "You lost the game", "Choose 1 to restart, 2 to end the game")

    while True:
        try:
            l = int(input(""))
            if l in [1, 2]:
                return l
            else:
                raise ValueError
        except ValueError:
            print_pause("Invalid input! Please enter 1 or 2.")


def win():
    # This function shows what happens after winning and saving the village
    # It also has input validation to give you a chance to choose the correct choice from 'y' and 'n'
    # The input is converted to lowercase using the "lower()" method
    print_pause("You achieved a great victory and saved the village! Good job!")
    print_pause("Do you want to restart (y/n)?")

    while True:
        w = input("").lower()
        if w == "y" or w == "n":
            return w
        else:
            print_pause("Invalid input! Please enter 'y' or 'n'.")


def cave():
    # This function describes what happens when approaching the cave
    # It has input validation to give you a chance to choose the correct choice from 1 and 2
    print_pause("You cautiously enter the cave")
    print_pause("Finally, you are inside the cave and walking through")
    print_pause("But wait! You found a troll inside the cave!")
    print_pause("Now you have two choices: 1) Run away, 2) Throw a spell")

    while True:
        try:
            c = int(input(""))
            if c in [1, 2]:
                return c
            else:
                raise ValueError
        except ValueError:
            print_pause("Invalid input! Please enter 1 or 2.")


def starting():
    # This function describes your starting place and choices you have to go to the house or a cave
    # It also has input validation
    print_pause("You find yourself standing in an open field, filled with grass",
                "and yellow wildflowers.")
    print_pause("Rumor has it that a wicked fairy is somewhere around here",
                "and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand, you hold your trusty (but not very effective)",
                "magic wand.")
    print_pause("You have two choices:")
    print_pause("1: Knock on the door")
    print_pause("2: Enter the cave")

    while True:
        try:
            ch = int(input("What are you going to do: "))
            if ch in [1, 2]:
                return ch
            else:
                raise ValueError
        except ValueError:
            print_pause("Invalid input! Please enter 1 or 2.")


def spell_casting(keyword):
    # This function randomly chooses your spells and the enemy's spell
    # It decides which spell is stronger
    print_pause("You and the enemy both prepare to cast a spell...")
    player_spell = random.choice(["Fireball", "Ice Shard", "Lightning Bolt"])
    enemy_spell = random.choice(["Cursed Blast", "Dark Beam", "Poison Dart"])
    print_pause("You cast", player_spell)
    print_pause("The enemy casts", enemy_spell)
    if keyword == "cave":
        if attack(keyword):
            print_pause("Your", player_spell, "overpowers the enemy's spell!")
            print_pause("You dealt damage to the enemy!")
            print_pause("The enemy is weakened!")
            return True
        else:
            print_pause("The enemy's spell is stronger!")
            print_pause("You took damage!")
            print_pause("You need to rethink your strategy!")
            return False
    elif keyword == "house":
        if attack(keyword):
            print_pause("Your", player_spell, "overpowers the enemy's spell!")
            print_pause("You dealt damage to the enemy!")
            print_pause("The enemy is weakened!")
            return True
        else:
            print_pause("The enemy's spell is stronger!")
            print_pause("You took damage!")
            print_pause("You need to rethink your strategy!")
            return False
    else:
        print_pause("Invalid keyword!")
        return False


def restart_game():
    # This function restarts the game using the starting function
    starting()


def end_game():
    # This function ends the game
    print_pause("Thanks for playing")


def game_over(score):
    # This function checks if you have lost the game based on your score
    # If your score is 0, it gives the option to restart or end the game
    if score == 0:
        print_pause("You lost the game since your score is " + str(score))
        while True:
            r = input("Do you want to restart (y/n)? ").lower()
            if r == "y":
                restart_game()
                return False
            elif r == "n":
                end_game()
                return True
            else:
                print_pause("Invalid input! Please enter 'y' or 'n'.")
    elif score == 1:
        print_pause("WATCH OUT! Your score is " + str(score) + " and you are approaching from losing the game!")
    return False


def encounter_enemy():
    # This function checks the result of your fight with the enemy
    # It calls the spell_casting function to decide the outcome
    # It also has input validation to give you a chance to choose the correct choice from 1 and 2
    print_pause("You encounter an enemy creature!")
    result = spell_casting("enemy")
    if result:
        return True
    else:
        print_pause("The battle ended in a draw!")
        return False


def play_game():
    # This is the main function that controls the flow of the game
    # It calls other functions based on the player's choices and the outcome of encounters
    score = 5
    while True:
        if game_over(score):
            break
        ch = starting()
        if ch == 1:
            d = door(score)
            if d == 1:
                score += 1
                result = spell_casting("house")
                if result:
                    print("Your score is " + str(score))
                    y = win()
                    if y == "y":
                        restart_game()
                    else:
                        end_game()
                        score = 5
                        break
                else:
                    score -= 1
                    print("Your score is " + str(score))
                    l = lose("house")
                    if l == 1:
                        restart_game()
                    elif l == 2:
                        end_game()
                        score = 5
                        break
            elif d == 2:
                score -= 1
                print("Your score is " + str(score))
                l = lose("house")
                if l == 1:
                    restart_game()
                elif l == 2:
                    end_game()
                    score = 5
                    break
        elif ch == 2:
            c = cave(score)
            if c == 2:
                score += 1
                result = spell_casting("cave")
                if result:
                    print("Your score is " + str(score))
                    y = win()
                    if y == "y":
                        restart_game()
                    else:
                        end_game()
                        score = 5
                        break
                else:
                    score -= 1
                    print("Your score is " + str(score))
                    l = lose("cave")
                    if l == 1:
                        restart_game()
                    elif l == 2:
                        end_game()
                        score = 5
                        break
            elif c == 1:
                score -= 1
                print("Your score is " + str(score))
                l = lose("cave")
                if l == 1:
                    restart_game()
                elif l == 2:
                    end_game()
                    score = 5
                    break


play_game()
