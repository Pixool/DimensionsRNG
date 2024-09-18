import os
import time
import random
import math
import decimal

inventory = []
loaded = False
e = False
lii = 1

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
    "Gloomwood Hollow": {"Chance": 0.2, "Desc": "A dark forest where shadows stretch and play tricks on the mind."},
    "Frostvale": {"Chance": 0.05, "Desc": "An eternal winter dimension with ice castles and frozen lakes."},
    "Emberland": {"Chance": 0.02, "Desc": "A volcanic realm with rivers of lava and fire spirits."},
    "Mistshroud": {"Chance": 0.01, "Desc": "A fog-covered dimension where visibility is limited and secrets abound."},
    "Verdant Glade": {"Chance": 0.01, "Desc": "A lush, green realm teeming with magical flora and fauna."},
    "Sundrop Oasis": {"Chance": 0.004, "Desc": "A desert oasis where every drop of water is imbued with healing properties."},
    "Whispering Woods": {"Chance": 0.002, "Desc": "A forest where the trees communicate through soft whispers."},
    "Starlit Cove": {"Chance": 0.002, "Desc": "A tranquil beach that glows under the stars with bioluminescent sand."},
    "Stormspire": {"Chance": 0.001, "Desc": "A dimension dominated by constant storms and powerful winds."},
    "Echo Valley": {"Chance": 0.0004, "Desc": "A canyon where every sound is amplified and creates beautiful melodies."},
    "Crystal Caverns": {"Chance": 0.0002, "Desc": "An underground realm filled with shimmering crystals that have magical properties."},
    "Lost City of Eldoria": {"Chance": 0.0002, "Desc": "An ancient, forgotten city filled with relics of powerful magic."},
    "Galactic Gardens": {"Chance": 0.0001, "Desc": "A cosmic dimension with planets that bloom like flowers in the void."},
    "Phantom Marsh": {"Chance": 0.00004, "Desc": "A haunted swamp where ghostly apparitions roam among the fog."},
    "Timekeeper's Sanctuary": {"Chance": 0.00002, "Desc": "A realm where time flows differently, allowing glimpses into the past and future."},
    "The Astral Cascade": {"Chance": 0.00002, "Desc": "A waterfall that flows with starlight, offering visions of the cosmos."},
    "Nebula Nexus": {"Chance": 0.00001, "Desc": "A swirling mass of colorful cosmic gases and celestial phenomena."},
    "The Shattered Isles": {"Chance": 0.000005, "Desc": "A collection of floating islands that drift through a stormy sky."},
    "The Forgotten Archive": {"Chance": 0.000002, "Desc": "A library dimension containing all knowledge ever lost to time."},
    "Veil of Serenity": {"Chance": 0.000001, "Desc": "A peaceful dimension that calms the mind and soothes the spirit."},
    "Wishing Well Realm": {"Chance": 0.0000005, "Desc": "A place where wishes manifest into tangible forms."},
    "The Abyssal Depths": {"Chance": 0.0000004, "Desc": "An oceanic dimension filled with mythical sea creatures and underwater wonders."},
    "The Clockwork City": {"Chance": 0.0000004, "Desc": "A realm of intricate gears and mechanisms that operate on their own."},
    "The Dreaming Spire": {"Chance": 0.0000002, "Desc": "A towering structure that reaches into the sky, inhabited by dream spirits."},
    "The Banshee's Echo": {"Chance": 0.0000002, "Desc": "A realm where every sound is a haunting melody sung by ethereal beings."},
    "The Realm of Evernight": {"Chance": 0.0000001, "Desc": "A dimension where darkness reigns, illuminated only by glowing flora."},
    "The Enchanted Cavern": {"Chance": 0.0000001, "Desc": "A magical cave that shifts and changes, revealing new paths and treasures."},
    "The Flux Lands": {"Chance": 0.00000004, "Desc": "A dimension where landscapes shift and change at random."},
    "The Shadowed Glens": {"Chance": 0.00000002, "Desc": "A series of hidden valleys where light and dark coexist harmoniously."},
    "The Celestial Bridge": {"Chance": 0.00000002, "Desc": "A luminous pathway that connects various dimensions in the cosmos."},
    "The Forgotten Oasis": {"Chance": 0.00000001, "Desc": "An ancient oasis shrouded in mystery and guarded by mythical beasts."},
    "The Realm of Echoing Dreams": {"Chance": 0.000000005, "Desc": "A dimension where dreams resonate and intertwine with reality."},
    "The Labyrinthine Forest": {"Chance": 0.000000002, "Desc": "A maze-like forest that rearranges itself to confound travelers."},
    "The Celestial Observatory": {"Chance": 0.000000001, "Desc": "A dimension where one can observe the entirety of the multiverse."},
    "The World Beneath the Waves": {"Chance": 0.0000000005, "Desc": "An underwater dimension filled with vibrant ecosystems and hidden wonders."},
    "The Ethereal Plane": {"Chance": 0.0000000004, "Desc": "A realm of pure thought and consciousness, where ideas take form."},
    "The Nexus of Shadows": {"Chance": 0.0000000004, "Desc": "A dark realm where shadows can take on physical forms."},
    "The Rift of Memories": {"Chance": 0.0000000002, "Desc": "A place where lost memories can be rediscovered and experienced."},
    "The Cradle of Creation": {"Chance": 0.0000000002, "Desc": "A dimension where new worlds and realities are born."},
    "The Realm of Tides": {"Chance": 0.0000000001, "Desc": "A dimension where the laws of physics are dictated by the ebb and flow of magical tides."},
    "The Infinite Archive": {"Chance": 0.00000000005, "Desc": "A dimension containing every story ever told, waiting to be discovered."},
    "The Labyrinth of Time": {"Chance": 0.00000000004, "Desc": "A complex maze where time loops and branches unpredictably."},
    "The Veil Between Worlds": {"Chance": 0.00000000004, "Desc": "A thin barrier that separates all dimensions, filled with whispers of the unknown."},
    "The Realm of Forgotten Souls": {"Chance": 0.00000000002, "Desc": "A dimension where lost spirits linger, seeking resolution."},
    "The Cosmic Abyss": {"Chance": 0.00000000002, "Desc": "A vast, dark expanse filled with ancient secrets and cosmic horrors."},
    "Dreamweaver's Domain": {"Chance": 0.00000000002, "Desc": "A realm where dreams are spun into reality by celestial beings."},
    "The Nexus": {"Chance": 0.00000000001, "Desc": "The rarest dimension, existing outside of time and space, where all possibilities converge."},
}

ctx = decimal.Context()
ctx.prec = 20

def float_to_str(f):
    d1 = ctx.create_decimal(repr(f))
    return format(d1, 'f')

Auras2 = [(k, v["Chance"]) for k, v in Auras.items()]
Auras2.sort(key=lambda x: x[1], reverse=True)

segments = []
total = 0
#Add lucky ducky roll when the number they roll can unlock two auras
for _, data in Auras2:
    segments.append((round(total, len(float_to_str(data)) - 2), round(total + data, len(float_to_str(data)) - 2), _))
    total += data

depth = 1000000000000

def has_value(tab, val):
    for i, v in enumerate(tab):
        if v[0] == val:
            return int(i)
    return False

lls = False

def render_frame():
    os.system("cls")
    print("Dimension RNG v0.6")
    print("-----------------------")
    if lls != False:
        print(f"Luck Bonus: {lii * 100 - 100}% left for another {int(time.time() - lls)}")
    else:
        print(f"Luck Bonus: {lii * 100 - 100}%")
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
                if name == 'Error':
                    render_frame()
                    print(f"~ Profile of Error ~")
                    print(f"Rarity: 1/Impossible")
                    print()
                    print("Welp this means I made a coding error, good job you found the 'only' easter egg")
                    print()
                    input("Press enter to return to index main menu ")
                    #If you look at this no good, you spoil the game no no good
                else:
                    render_frame()
                    print(f"~ Profile of {name} ~")
                    print(f"Rarity: 1/{math.ceil(int(1/aura['Chance']))}")
                    print()
                    print(aura["Desc"])
                    print()
                    input("Press enter to return to index main menu ")
            render_frame()
            for i, (name, _) in enumerate(Auras2):
                print(f"[#{i+1}] {name} - 1/{math.ceil(1/Auras[name]['Chance'])}")
            if e == True:
                print(f'[#{len(Auras) + 1}] Error - 1/Impossible')
            print()
            answer = input("Type index or name of dimension to view profile, or m to return to main menu ").lower()
            if answer == "m":
                break
            elif answer.isdigit():
                if int(answer) == len(Auras) + 1:
                    lp('Error', 123)
                else:
                    lp(Auras2[int(answer)-1][0], Auras[Auras2[int(answer)-1][0]])
            else:
                if answer.capitalize() == 'Error':
                    lp('Error', 123)
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
                x /= lii
                x = 1 - x
                tingy = True
                for seg in segments:
                    if seg[0] <= x <= seg[1] and tingy:
                        print(f"{seg[2]} 1/{int(math.ceil(1/Auras[seg[2]]['Chance']))}")
                        tingy = False
                        index = has_value(inventory, seg[2])
                        if index is not False and isinstance(index, int):
                            inventory[index][2] += 1
                        else:
                            inventory.append([seg[2], int(math.ceil(1/Auras[seg[2]]['Chance'])), 1])
                if tingy:
                    print('Error 1/Impossible')
                    print('Check index ;)')
                    e = True
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
        if not loaded: 
            loaded = True
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
                        inventory[has_value(inventory, Auras2[int(id)][0])] = [Auras2[int(id)][0], math.ceil(1/Auras[Auras2[int(id)][0]])['Chance'], inventory[has_value(inventory, Auras2[int(id)][0])][2] + int(number)]
                    else:
                        inventory.append([Auras2[int(id)][0], int(math.ceil(1/Auras[Auras2[int(id)][0]]['Chance'])), int(number)])
                    if finished:
                        break
                render_frame()
                print("Items loaded!")
                print()
                input("Press enter to return to main menu ")
        else:
            render_frame()
            print('Items have already been loaded :)')
            input("Press enter to return to main menu ")
            render_frame()
            print("██████╗░░█████╗░███╗░░██╗██╗████████╗  ██████╗░██╗░░░░░░█████╗░██╗░░░██╗")
            print("██╔══██╗██╔══██╗████╗░██║╚█║╚══██╔══╝  ██╔══██╗██║░░░░░██╔══██╗╚██╗░██╔╝")
            print("██║░░██║██║░░██║██╔██╗██║░╚╝░░░██║░░░  ██████╔╝██║░░░░░███████║░╚████╔╝░")
            print("██║░░██║██║░░██║██║╚████║░░░░░░██║░░░  ██╔═══╝░██║░░░░░██╔══██║░░╚██╔╝░░")
            print("██████╔╝╚█████╔╝██║░╚███║░░░░░░██║░░░  ██║░░░░░███████╗██║░░██║░░░██║░░░")
            print("╚═════╝░░╚════╝░╚═╝░░╚══╝░░░░░░╚═╝░░░  ╚═╝░░░░░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░")
            print()
            print("░██████╗░░█████╗░███╗░░░███╗███████╗░██████╗  ░██╗░░░░░░░██╗██╗████████╗██╗░░██╗  ███╗░░░███╗███████")
            print("██╔════╝░██╔══██╗████╗░████║██╔════╝██╔════╝  ░██║░░██╗░░██║██║╚══██╔══╝██║░░██║  ████╗░████║██╔════╝")
            print("██║░░██╗░███████║██╔████╔██║█████╗░░╚█████╗░  ░╚██╗████╗██╔╝██║░░░██║░░░███████║  ██╔████╔██║█████╗░░")
            print("██║░░╚██╗██╔══██║██║╚██╔╝██║██╔══╝░░░╚═══██╗  ░░████╔═████║░██║░░░██║░░░██╔══██║  ██║╚██╔╝██║██╔══╝░░")
            print("╚██████╔╝██║░░██║██║░╚═╝░██║███████╗██████╔╝  ░░╚██╔╝░╚██╔╝░██║░░░██║░░░██║░░██║  ██║░╚═╝░██║███████╗")
            print("░╚═════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚══════╝╚═════╝░  ░░░╚═╝░░░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝  ╚═╝░░░░░╚═╝╚══════╝")
            time.sleep(1)

#Watcha doing down here?



































#Ummmmm.....














































#So you still just gonna keep on going?


































































































#Wow you determined

























#In update 0.6 this was line 500 :)