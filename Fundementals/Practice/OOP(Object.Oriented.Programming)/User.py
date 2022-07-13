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

    def enroll(self):
        if self.is_rewards_member:
            print("User already a member")
            return False

        self.is_rewards_member = True
        self.gold_card_points = 500

    def spend_points(self, amount):
        if self.gold_card_points < amount:
            return False
        self.gold_card_points-=amount

Matt = User("Matt","Von","MattV@CodingDojo.com",18)
Matt.enroll()
Matt.spend_points(50)
Matt.display_info()

Layla = User('Layla','Attwood','AttwoodLayla@CodingDojo.com',25)
Layla.enroll()
Layla.spend_points(80)
Layla.display_info()

Ben = User('Ben','Jim','BenJ@CodingDojo.com',16)
Ben.display_info()