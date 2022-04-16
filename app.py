class Hero:
    jumlah = 0
    
    def __init__(self,nama,health,attack,defense,):
        self.nama = nama
        self.health = health
        self.attack = attack
        self.defense = defense
        Hero.jumlah += 1

    def get_nama(self):
        print("nama :{}".format(self.nama))
    def get_health(self):
        print("health :{}".format(self.health))
    def get_attack(self):
        print("attack :{}".format(self.attack))
    def get_defense(self):
        print("defense :{}".format(self.defense))
