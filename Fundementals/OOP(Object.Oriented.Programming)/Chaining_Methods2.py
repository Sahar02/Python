class User:
    
    def __init__(self,first_name,last_name,email,age):
        
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0

    def display_info(self):
        print(f"\n{self.first_name} {self.last_name}\n{self.email}\n{self.age}\n{self.is_rewards_member}\n{self.gold_card_points}")
        return self

    def enroll(self):
        self.is_rewards_member = True
        self.gold_card_points = 500
        return self

    def spend_points(self, amount):
        self.gold_card_points-=amount
        return self

Matt = User("Matt","Von","MattV@CodingDojo.com",18)
Matt.enroll().spend_points(50).display_info()

Layla = User('Layla','Attwood','AttwoodLayla@CodingDojo.com',25)
Layla.enroll().spend_points(80).display_info()

Ben = User('Ben','Jim','BenJ@CodingDojo.com',16)
Ben.display_info()