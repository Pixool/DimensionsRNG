import os
import time
import random

inventory = []

code = [
    "F",
    "G",
    "M",
    "Q",
    "Z",
    "/",
    "(",
    "^",
    "#",
    "~",
]

Auras = {
    "Glimmerwood": {"Chance": 0.5, "Desc": "A forest filled with bioluminescent plants and gentle creatures."},
    "Skyreach": {"Chance": 0.2, "Desc": "A floating island realm where gravity behaves unpredictably."},
    "Frostvale": {"Chance": 0.2, "Desc": "An eternal winter dimension with ice castles and frozen lakes."},
    "Emberland": {"Chance": 0.04, "Desc": "A volcanic realm with rivers of lava and fire spirits."},
    "Mistshroud": {"Chance": 0.04, "Desc": "A fog-covered dimension where visibility is limited and secrets abound."},
    "Verdant Glade": {"Chance": 0.02, "Desc": "A lush, green realm teeming with magical flora and fauna."},
}

Auras2 = [(k, v["Chance"]) for k, v in Auras.items()]
Auras2.sort(key=lambda x: x[1], reverse=True)

segments = []
total = 0
luckboost = 1  # increase value to increase luck
for _, data in Auras2:
    segments.append((total, total + data, _))
    total += data

depth = 100

def has_value(tab, val):
    for i, v in enumerate(tab):
        if v[0] == val:
            return int(i)
    return False

lls = False

def render_frame():
    os.system("cls")
    print("Dimension RNG v0.4")
    print("-----------------------")
    if lls:
        print(f"Luck Bonus: {luckboost * 100 - 100}% left for another {int(time.time() - lls)}")
    else:
        print(f"Luck Bonus: {luckboost * 100 - 100}%")
    print()

def index_of(array, value):
    for i, v in enumerate(array):
        if v == value:
            return i
    return None

while True:
    os.system("cls")
    print("Welcome to Dimension RNG!")
    print("-----------------------")
    print()
    print("Menu:")
    print("R - Roll")
    print("I - Inventory")
    print("B - Index of Dimensions")
    print("S - Shop")
    print("L - Load")
    print("Q - Save and Quit")
    print()
    answer = input("What would you like to do? ").lower()
    if lls:
        if time.time() - lls < 1:
            lls = False
    if answer == 'b':
        while True:
            def lp(name, aura):
                render_frame()
                print(f"~ Profile of {name} ~")
                print(f"Rarity: 1/{int(1/aura['Chance'])}")
                print()
                print(aura["Desc"])
                print()
                input("Press enter to return to index main menu ")
            render_frame()
            for i, (name, _) in enumerate(Auras2):
                print(f"[#{i+1}] {name} - 1/{int(1/Auras[name]['Chance'])}")
            print()
            answer = input("Type index or name of dimension to view profile, or m to return to main menu ").lower()
            if answer == "m":
                break
            elif answer.isdigit():
                lp(Auras2[int(answer)-1][0], Auras[Auras2[int(answer)-1][0]])
            else:
                if answer.capitalize() in Auras:
                    lp(answer.capitalize(), Auras[answer.capitalize()])
    elif answer == 'r':
        while True:
            render_frame()
            number = int(input("How many times would you like to roll? "))
            print()
            for _ in range(number):
                print("Rolling...")
                x = random.randint(0, depth) / depth
                x /= luckboost
                x = 1 - x
                for seg in segments:
                    if seg[0] <= x <= seg[1]:
                        print(f"{seg[2]} 1/{int(1/Auras[seg[2]]['Chance'])}")
                        index = has_value(inventory, seg[2])
                        if index is not False and isinstance(index, int):
                            inventory[index][2] += 1
                        else:
                            inventory.append([seg[2], int(1/Auras[seg[2]]['Chance']), 1])
                print()
                time.sleep(0.75)
            answer = input("Do you want to roll again (enter) or go back to the main menu (m)? ").lower()
            if answer == 'm':
                break
    elif answer == 'i':
        render_frame()
        if not inventory:
            print("You have no items!")
        else:
            inventory.sort(key=lambda x: x[1], reverse=True)
            for i, v in enumerate(inventory):
                print(f"- {v[0]} 1/{v[1]} x{v[2]}")
        print()
        input("Press enter to return to main menu ")
    elif answer == 'q':
        render_frame()
        savestring = ""
        for v in inventory:
            for i in range(len(str(has_value(Auras2, v[0])))):
                savestring += code[int(str(has_value(Auras2, v[0]))[i]) + 1]
            savestring += '.'
            for i in range(len(str(v[2]))):
                savestring += code[int(str(v[2])[i]) + 1]
            savestring += '`'
        print(savestring)
        print()
        input("Copy (Ctrl + Shift + C) or screenshot your save key and paste it into the Aura RNG load tab when playing again. Press enter to close program ")
        break
    elif answer == 'l':
        a = 'c'
        render_frame()
        key = input("Copy (Ctrl + Shift + V) your save key here: ")
        if inventory:
            a = input("You have items in this save, would you like to cancel (q), overwrite (o) or combine (c)? ")
        if a == 'o':
            inventory = []
        if a == 'c' or a == 'o':
            place, id, number, finished = 0, '', '', False
            while True:
                id, number = '', ''
                for i in range(place, len(key) + 1):
                    if place + 1 == len(key) or finished:
                        finished = True
                        break
                    elif key[i] == '.' or key[i] == '`':
                        place += 1
                        break
                    id += str(index_of(code, key[i]) - 1)
                    place += 1
                for i in range(place, len(key) + 1):
                    if place + 1 == len(key) or finished:
                        finished = True
                        break
                    elif key[i] == '.' or key[i] == '`':
                        place += 1
                        break
                    number += str(index_of(code, key[i]) - 1)
                    place += 1
                index = has_value(inventory, Auras2[int(id)][0])
                if index is not False and isinstance(index, int):
                    inventory[has_value(inventory, Auras2[int(id)][0])] = [Auras2[int(id)][0], 1/Auras[Auras2[int(id)][0]]['Chance'], inventory[has_value(inventory, Auras2[int(id)][0])][2] + int(number)]
                else:
                    inventory.append([Auras2[int(id)][0], int(1/Auras[Auras2[int(id)][0]]['Chance']), int(number)])
                if finished:
                    break
            render_frame()
            print("Items loaded!")
            print()
            input("Press enter to return to main menu ")
