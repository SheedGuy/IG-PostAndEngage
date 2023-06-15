# This file contains several functions for interacting with the SMM panel API
import requests
import keys

secret = keys.PeakerrKey

# Getting all the services
def GetServices():
    resp = requests.post('https://peakerr.com/api/v2?key=' + secret + '&action=services')
    return resp.json()

# Placing a new order for likes
def AddLikes(link, quantity):
    postLink = link
    resp = requests.post("https://peakerr.com/api/v2?key=" + secret 
                         + "&action=add&service=14097&link=" + postLink 
                         + "&quantity=" + str(quantity))
    return resp.json()

def OrderStatus(orderID):
    resp = requests.post("https://peakerr.com/api/v2?key=" + secret 
                         + "&action=status&id=" + str(orderID))
    return resp.json()


# print(AddLikes("https://www.instagram.com/p/CteU-FHLn3R/", 45))
print()

# These all function Properly
# Todo:
# Add a function to add followers
# Create a data struct for services