
class Ninja():
    
    def __init__(self, first_name , last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.pet = pet
        self.treats = treats
        self.pet_food = pet_food


    def walk(self,pet):
        pet.play()
        return self
    
    def feed(self,pet):
        pet.play()
        return self
    
    def bath(pet,self):
        pet.noise()
        return self

treats = ["bacon","salmon","chicken"]
pet_food = ["chicken","beef","duck"]

sam = Ninja("Sam", "Jeff",treats, pet_food, "cat" )
