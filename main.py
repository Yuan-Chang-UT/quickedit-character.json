import json
import os
import shutil

money_list = ['5449016a4bdc2d6f028b456f',
              "569668774bdc2da2298b4568",
              "5696686a4bdc2da3298b456a"]

known_items_map = {"5449016a4bdc2d6f028b456f": "rubles",
                   "569668774bdc2da2298b4568": "euros",
                   "5696686a4bdc2da3298b456a": "dollars"}

known_levels_map = {1: 0,
                    2: 1000,
                    3: 3743,
                    4: 7742,
                    5: 12998,
                    6: 19492,
                    7: 27150,
                    8: 36001,
                    9: 46026,
                    10: 57124,
                    11: 69350,
                    12: 82686,
                    13: 99500,
                    14: 119424,
                    15: 142477,
                    16: 168760,
                    17: 197979,
                    18: 230024,
                    19: 264490,
                    20: 301534,
                    21: 340696,
                    22: 382188,
                    23: 426190,
                    24: 473090,
                    25: 524580,
                    26: 580660,
                    27: 641330,
                    28: 706590,
                    29: 776440,
                    30: 850840,
                    31: 929870,
                    32: 1013490,
                    33: 1104454,
                    34: 1202762,
                    35: 1308414,
                    36: 1421410,
                    37: 1541750,
                    38: 1669434,
                    39: 1804462,
                    40: 1946834,
                    41: 2096550,
                    42: 2253610,
                    43: 2420768,
                    44: 2598024,
                    45: 2785378,
                    46: 2982830,
                    47: 3190380,
                    48: 3408028,
                    49: 3635774,
                    50: 3873618,
                    51: 4121560,
                    52: 4379600,
                    53: 4651410,
                    54: 4936990,
                    55: 5236340,
                    56: 5549460,
                    57: 5872910,
                    58: 6235021,
                    59: 6604557,
                    60: 6991535,
                    61: 7398709,
                    62: 7828833,
                    63: 8286497,
                    64: 8780881,
                    65: 9330345,
                    66: 9953249,
                    67: 10713853,
                    68: 11749857,
                    69: 13198961,
                    70: 23198961}


def options_list(prompt, lst):
    print(prompt)

    i = 0
    for item in lst:
        print(i, ": ", item)
        i += 1

    selected = -1
    while (selected < 0 or selected >= i):
        selected = int(input())
    # print('\n')

    return lst[selected]


def profile_select(working_directory):
    # LIST PROFILES
    # TODO LIST IN ORDER OF LAST OPENED
    all_profiles = os.listdir("Server\\user\\profiles")

    temp_counter = 0
    for profile in all_profiles:
        char_json_path = working_directory + "\\Server\\user\\profiles\\" + profile + "\\character.json"

        with open(char_json_path, "r", encoding='utf-8') as charjsonfile:
            prof_json = json.load(charjsonfile)

            nickname = "asd"
            nickname = prof_json["Info"]["Nickname"]

        print(temp_counter, ": ", nickname, " - ", profile)

        temp_counter += 1

    selected = -1
    while (selected < 0 or selected >= temp_counter):
        selected = int(input("Enter the number of the profile you wish to edit \n"))

    return all_profiles[selected]


def select_level_get_experience():
    selected = -1

    while (selected < 1 or selected > 70):
        selected = int(input("Enter a level between 1 and 70 (inclusive of both)\n"))

    return known_levels_map[selected]


def max_traderstandings(charjsondata):
    for trader in charjsondata["TraderStandings"]:
        # print(trader)
        trader_dict = data["TraderStandings"][trader]

        # unlock jaeger
        if trader_dict["display"] == "false" and trader == "5c0647fdd443bc2504c2d371":
            trader_dict["display"] == "true"

        # set levels to max
        if len(trader_dict["loyaltyLevels"]) > 1:
            print(trader)

            dict_len = len(trader_dict["loyaltyLevels"])

            dict_len_str = str(dict_len - 1)

            top_level = trader_dict["loyaltyLevels"][dict_len_str]

            trader_dict["currentSalesSum"] = top_level["minSalesSum"]
            trader_dict["currentStanding"] = top_level["minStanding"]
            trader_dict["currentLevel"] = dict_len


def max_hideoutareas(charjsondata):
    # VENTS
    charjsondata["Hideout"]["Areas"][0]["level"] = 3
    # SECURITY
    charjsondata["Hideout"]["Areas"][1]["level"] = 3
    # LABRATORY
    charjsondata["Hideout"]["Areas"][2]["level"] = 3
    charjsondata["Hideout"]["Areas"][3]["level"] = 4
    charjsondata["Hideout"]["Areas"][4]["level"] = 3
    charjsondata["Hideout"]["Areas"][5]["level"] = 3
    charjsondata["Hideout"]["Areas"][6]["level"] = 3
    charjsondata["Hideout"]["Areas"][7]["level"] = 3
    charjsondata["Hideout"]["Areas"][8]["level"] = 3
    charjsondata["Hideout"]["Areas"][9]["level"] = 3
    charjsondata["Hideout"]["Areas"][10]["level"] = 3
    charjsondata["Hideout"]["Areas"][11]["level"] = 3
    charjsondata["Hideout"]["Areas"][12]["level"] = 1
    charjsondata["Hideout"]["Areas"][13]["level"] = 1
    charjsondata["Hideout"]["Areas"][14]["level"] = 1
    charjsondata["Hideout"]["Areas"][15]["level"] = 3
    charjsondata["Hideout"]["Areas"][16]["level"] = 1
    charjsondata["Hideout"]["Areas"][17]["level"] = 1
    charjsondata["Hideout"]["Areas"][18]["level"] = 1
    charjsondata["Hideout"]["Areas"][19]["level"] = 1
    charjsondata["Hideout"]["Areas"][20]["level"] = 3
    charjsondata["Hideout"]["Areas"][21]["level"] = 1




def main():
    working_directory = os.getcwd()
    print("WORKING DIRECTORY: ", working_directory)

    if not os.path.isdir("Server\\user\\profiles"):
        print("Server\\users\\profiles folder not found")
        sys.exit()

    # print(os.listdir("Server\\user\\profiles"))
    # PROFILE SELECT
    profile_id = profile_select(working_directory)

    char_json_path = working_directory + "\\Server\\user\\profiles\\" + profile_id + "\\character.json"
    with open(char_json_path, "r", encoding='utf-8') as charjsonfile:
        charjsondata = json.load(charjsonfile)

    # MAKE A COPY OF character.json for the given profile
    i = 0
    while os.path.exists(
            working_directory + "\\Server\\user\\profiles\\" + profile_id + "\\character_backup_raw%s.json" % i):
        i += 1
    shutil.copyfile(working_directory + "\\Server\\user\\profiles\\" + profile_id + "\\character.json",
                    working_directory + "\\Server\\user\\profiles\\" + profile_id + "\\character_backup_raw%s.json" % i)

    print("\ncharacter.json backed up as ", "character_backup_raw%s.json" % i)



    print("\n=======================================\n")



    # give 99,999,999 MONEY
    selected = options_list("set all money in inventory to 99,999,999?", ["no", "yes"])

    if selected == "yes":
        maxed = []
        # SET RUBLES + EUROS + DOLLARS 99,999,999
        for item in charjsondata["Inventory"]["items"]:
            if (item['_tpl'] in money_list and item["_tpl"] not in maxed):
                item['upd']['StackObjectsCount'] = 99999999

                print(known_items_map[item['_tpl']], " set to 99,999,999")

                maxed.append(item['_tpl'])



    print("\n=======================================\n")


    # change level
    selected = options_list("change player level?", ["no", "yes"])

    if selected == "yes":
        new_experience = select_level_get_experience()
        charjsondata["Info"]["Experience"] = new_experience
        print("Experience changed to: ", new_experience)


    print("\n=======================================\n")


    # change traderstandings
    selected = options_list("Max Trader Levels?", ["no", "yes"])
    if selected == "yes":
        max_traderstandings(charjsondata)

    print("\n=======================================\n")


    # change hideout areas
    selected = options_list("Max Hideout Areas?", ["no", "yes"])
    if selected == "yes":
        max_hideoutareas(charjsondata)

    print("\n=======================================\n")




if __name__ == "__main__":
    main()
