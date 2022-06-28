# 1.Countdown
def countdown(list):
    list = [0,1,2,3,4,5]
    return (list[::-1])
print(countdown(list))

# 2.Print and Return
def print_and_return():
    list = [5,8]
    print(list[0])
    return (list[1])
print(print_and_return())

#3.First Plus Length
def first_plus_length():
    list = [1,2,3,4,5,6,7]
    x = (list[0]) + len(list)
    return x
print(first_plus_length())

#4.Values Greater than Second
def values_greater_than_second(list):
    if len(list) < 2:
        return False
    values = []
    for i in range(0,len(list)):
        if list[i] > list[2]:
            values.append(list[i])
    print(len(values))
    return  values
print(values_greater_than_second([4,5,6,7,8,9,10]))
print(values_greater_than_second([4]))

#5.This Length, That Value
def length_and_value(size,value):
    list=[]
    for i in range(0, size):
        list.append(value)
    return list
print(length_and_value(4,7))
print(length_and_value(2,5))