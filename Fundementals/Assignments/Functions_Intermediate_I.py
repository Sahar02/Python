# #1 Update Values in Dictionaries and Lists
# from typing import List


# x = [ [5,2,3], [10,8,9] ]
# students = [
#      {'first_name':  'Michael', 'last_name' : 'Jordan'},
#      {'first_name' : 'John', 'last_name' : 'Rosales'}
# ]
# sports_directory = {
#     'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
#     'soccer' : ['Messi', 'Ronaldo', 'Rooney']
# }
# z = [ {'x': 10, 'y': 20} ]

# # Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ]
# x[1][0]= 15

# # Change the last_name of the first student from 'Jordan' to 'Bryant'
# students[0]['last_name'] = 'Bryant'

# # In the sports_directory, change 'Messi' to 'Andres'
# sports_directory['soccer'][0] = 'Andres'

# # Change the value 20 in z to 30
# z[0]['y'] = 30


# # 2.Iterate Through a List of Dictionaries
# """Create a function *iterateDictionary(some_list)* that, given a list of dictionaries, 
# the function loops through each dictionary in the list and prints each key
# and the associated value. For example, given the following list: """
# List = [
#             {'num':'1', 'first_name':'John'},
#             {'num':'2', 'name':'Sara'},
#             {'num':'3', 'name': 'Kelly'},
#             {'num':'4','name':'Kim'}
# ]
# def iterateDictionary(List):
#     for dict in List:
#         for key,val in dict.items():
#             key + val
#             print(f'\n{key} - {val}')
# print(iterateDictionary(List))

#3. Get Values From a List of Dictionaries
"""Create a function --iterateDictionary2(key_name, some_list)-- that,
given a list of dictionaries and a key name, 
the function prints the value stored in that key for each dictionary. 
For example, iterateDictionary2('first_name', students) should output:"""
# Burke_Virginia = [
#     {'Closet_City':'Annandale, VA'},
#     {'Closet_City':'Centreville, VA'},
#     {'Closet_City':'Arlington, VA'},
#     {'Closet_City':'Dale City, VA'},
#     {'Closet_City':'Alexandria, VA'},
#     {'Closet_City':'Reston, VA'},
#     {'Closet_City':'Washington, DC'},
#     {'Closet_City':'Silver Spring, MD'},
# ]
# def iterateDictionary2(Burke_Virginia):
#     for dict in Burke_Virginia:
#         for values in dict.values():
#             print(values)
# print(iterateDictionary2(Burke_Virginia))

# # 4.Iterate Through a Dictionary with List Values
# """Create a function ---printInfo(some_dict)--- that given a dictionary whose values are all lists,
# prints the name of each key along with the size of its list,
# and then prints the associated values within each key's list."""
# Planets = {
#     'Major_Planets' : ['Earth','Moon','Mercury','Jupiter','Saturn','Uranus','Neptune','Pluto'],
#     'Where?' : ['We live on earth', 'Moon is in the sky...natures nightlight,', 
#                 'Everything else is Far in the solar system... looks small.']
# }
# def printInfo(Planets):
#     print(len(Planets['Major_Planets']),"MAJOR PLANETS")
#     for v in Planets['Major_Planets']:
#         print(v)
        
#     print("\nWHERE?")
#     for v in Planets['Where?']:
#         print(v)
# print(printInfo(Planets))