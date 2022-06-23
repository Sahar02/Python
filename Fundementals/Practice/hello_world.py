print("Hello World")
name = "Sahar"
print("Hello", name)
print("Hello" + name)

num = str(2)
print("Hello" , num)
print("Hello" + num)

favorite_food1 = "Pizza"
favorite_food2 = "Chocolate"
favorite_food3 = "I love to eat %s" % "Pizza,"
favorite_food4 = "and I also love to eat %s" % "Dark Chocolate with Cacao Nibs from Trader Joes."
print("I love to eat {} and {}.".format(favorite_food1, favorite_food2))
print(f"I love to eat {favorite_food1} and {favorite_food2}.")
print("I love to eat %s and %s." % (favorite_food1,favorite_food2))
print(favorite_food3,favorite_food4)
print(favorite_food1,favorite_food2.title())
print(favorite_food3,favorite_food4.title())
print(favorite_food1.upper(),favorite_food2.upper())