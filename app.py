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
