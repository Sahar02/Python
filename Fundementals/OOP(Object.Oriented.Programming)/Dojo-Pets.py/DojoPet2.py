import DojoPet

class Pet(DojoPet.Ninja):
    def __init__(self, name , type , tricks, noise ):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.energy = 100
        self.health = 100
        self.noise = noise

    def sleep(self):
        self.energy += 25
        return self
    
    def eat(self):
        self.energy += 5
        self.health += 10
        return self
    
    def play(self):
        self.health += 5
        return self
    
    def noise(self):
        print(self.noise)
        return self

truffle = Pet("Truffle","cat","hand shake", "meow")

DojoPet.sam.walk(truffle)
print(truffle.health)