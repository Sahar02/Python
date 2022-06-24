#Basic
for x in range(151):
    print(x)

#Multiples of 5
for x in range(5,1005,5):
    print(x)

#Counting The Dojo Way
for x in range(1,101):
    if x%5 == 0:
        print("coding",x)
    else:
        x%10 == 0
        print("Coding Dojo", x)

#Whoa. That Sucker's Huge
for x in range(500000):
    if x % 2 != 0:
        print(x)

#Countdown by Fours
for x in range(2018,0,-4):
    print(x)

#Flexible Counter
lowNum = 6
highNum = 30
mult = 7
for x in range(lowNum,highNum):
    if x%mult == 0:
        print(x)