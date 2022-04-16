class Hero:
    jumlah = 0
    
    def __init__(self,nama,health,attack,defense,):
        self.nama = nama
        self.health = health
        self.attack = attack
        self.defense = defense
        Hero.jumlah += 1