import random


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Person:
    def __init__(self, name, hp, mp, atk, df, magic, items):
        self.name = name
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.atkl = atk - 10
        self.atkh = atk + 10
        self.df = df
        self.magic = magic
        self.items = items
        self.actions = ["Attack", "Magic", "Items"]

    def generate_damage(self):
        return random.randrange(self.atkl, self.atkh)

    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def heal(self, dmg):
        self.hp += dmg
        if self.hp > self.maxhp:
            self.hp = self.maxhp

    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.maxhp

    def get_mp(self):
        return self.mp

    def get_max_mp(self):
        return self.maxmp

    def reduce_mp(self, cost):
        self.mp -= cost

    def choose_action(self):
        i = 1
        print("\n" + bcolors.OKBLUE + bcolors.BOLD + self.name + bcolors.ENDC)
        print("\n" + bcolors.OKBLUE + bcolors.BOLD + "ACTIONS:" + bcolors.ENDC)
        for item in self.actions:
            print("    " + str(i) + ":", item)
            i += 1

    def choose_magic(self):
        i = 1
        print("\n" + bcolors.OKBLUE + bcolors.BOLD + self.name + bcolors.ENDC)
        print("\n" + bcolors.OKBLUE + bcolors.BOLD + "MAGIC:" + bcolors.ENDC)
        for spell in self.magic:
            print("    " + str(i) + ":", spell.name, "(cost:", str(spell.cost) + ")")
            i += 1

    def choose_item(self):
        i = 1
        print("\n" + bcolors.OKBLUE + bcolors.BOLD + self.name + bcolors.ENDC)
        print("\n" + bcolors.OKGREEN + bcolors.BOLD + "ITEMS:" + bcolors.ENDC)
        for item in self.items:
            print("    " + str(i) + ":", item["item"].name, ":", item["item"].description, " x(" + str(item["qty"]) + ")")
            i += 1

    def get_bar(self, current, max, length, divider):
        bar = ""
        bar_ticks = (current / max) * 100 / divider

        while bar_ticks > 0:
            bar += "█"
            bar_ticks -= 1

        while len(bar) < length:
            bar += " "

        return bar

    def get_hp_string(self):
        hp_string = str(self.hp) + "/" + str(self.maxhp)
        hp_string_max_length = len(str(self.maxhp) + "/" + str(self.maxhp))

        while len(hp_string) < hp_string_max_length:
            hp_string = " " + hp_string

        return hp_string

    def get_mp_string(self):
        mp_string = str(self.mp) + "/" + str(self.maxmp)
        mp_string_max_length = len(str(self.maxmp) + "/" + str(self.maxmp))

        while len(mp_string) < mp_string_max_length:
            mp_string = " " + mp_string

        return mp_string

    def get_stats(self):
        print("                _________________________           __________ ")
        print(self.name + " " + self.get_hp_string() + " |"
              + bcolors.OKGREEN + self.get_bar(self.hp, self.maxhp, 25, 4)
              + bcolors.ENDC + "|   " + self.get_mp_string() + " |"
              + bcolors.OKBLUE + self.get_bar(self.mp, self.maxmp, 10, 10)
              + bcolors.ENDC + "|")
