import unittest
from tests.friends_test import *

if __name__ == '__main__':
    unittest.main()

def get_name (person5):
    return person5 ["name"]

def get_favourite_tv_show (person2):
    return person2["favourites"]["tv_show"]

#def person_likes_food__True(person2):
    # fav_food = None 
    # for food in person2 ["favourites"]["snacks"]:
    #     if food ["snacks"] == [1]:
    #         fav_food = food 

    # return fav_food 

def likes_to_eat( person, snack ):
    for food in person["favourites"]["snacks"]:
        if food == snack:
            return True 
    return False 

def add_friend (person, name):
    person["friends"].append (name)

def remove_friend (person, name):
    person["friends"].remove (name)

# total_eggs = 0

# for chicken in chickens:
#     total_eggs += chicken["eggs"]
#     chicken["eggs"] = 0

# print(f"{total_eggs} eggs collected")
# print(chickens)

def total_money(person):
    money = 0
    for money in list:
        money + person["monies"]