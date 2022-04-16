class Hero:
    jumlah = 0
    
    def __init__(self,name,health,attack,defense,):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        Hero.jumlah += 1

    def get_name(self):
        print("name :{}".format(self.name))
    def get_health(self):
        print("health :{}".format(self.health))
    def get_attack(self):
        print("attack :{}".format(self.attack))
    def get_defense(self):
        print("defense :{}".format(self.defense))

    def serang(self,lawan):
        print(f"{self.name} menyerang {lawan.name}")
        lawan.health -= (self.attack - lawan.defense)
        print(f"serangan terasa {self.attack}")
        print(f"sisa nyawa : {lawan.health}")
        if lawan.health < 0:
            print("Hero sudah mati")
        else:
            pass
    
    @classmethod
    def jumlah_hero(cls):
        return cls.jumlah

class Strength(Hero):
    def __init__(self,name,health,attack,defense,strength):
        Hero.__init__(self,name,health,attack,defense)
        self.strength = strength

class Agility(Hero):
    def __init__(self,name,health,attack,defense,agility):
        Hero.__init__(self,name,health,attack,defense)
        self.agility = agility

class Intelligence(Hero):
    def __init__(self,name,health,attack,defense,intelligence):
        Hero.__init__(self,name,health,attack,defense)
        self.intelligence = intelligence

rikimaru = Hero("Rikimaru",1000,500,10)
mortred = Hero("mortred",1500,50,30)
rikimaru.serang(mortred)

balanar = Strength("Balanar",2000,200,50,25)
balanar.serang(mortred)