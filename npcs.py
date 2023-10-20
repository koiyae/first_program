class NPC: #Base, Pai, Super
    def __init__(self, name, team, strength, ammo):
        self.name=name
        self.team=team
        self.strength=strength
        self.ammo=ammo
        self.alive=True
        self.stamina=100
    def info(self):
        print(f"Nome...: {self.name}")
        print("Time....: " + str(self.team))
        print("Força...: " + str(self.strength))
        print("Munição.: " + str(self.ammo))
        print("Vivo....: " + ("sim" if self.alive else "não"))
        print("Energia.: " + str(self.stamina))
        print("-" * 15)

class Soldier(NPC):
    def __init__(self, name, team):
        self.strength=200
        self.ammo=200
        super().__init__(name, team, self.strength, self.ammo)
class Guard(NPC):
    def __init__(self, name, team):
        self.strength=100
        self.ammo=50
        super().__init__(name, team, self.strength, self.ammo)
class Elite(NPC):
    def __init__(self, name, team):
        self.strength=400
        self.ammo=500
        super().__init__(name, team, self.strength, self.ammo)
    def inf(self):
        super().info()


s1 = Guard("Bruno", 1)
s2 = Elite("Eduardo", 1)
s3 = Soldier("Alan", 1)
s4 = Guard("Luiz", 2)
s5 = Elite("Igor", 2)
s6 = Soldier("Kevin", 2)

#Hokama MORTO
s2.alive=False

s1.info()
s2.info()
s3.info()
s4.info()
s5.info()
s6.info()
