# This script will change all the files it's coded to expect to need to be changed
# If I get new skins in the future that have new file structures this will need to 
# be updated.
# 
# Currently this file only supports the following root folders & files:
# NULL


import os
import re

path = None
currPath = None
files = os.listdir(path)
pattern = re.compile("[0-7]")
currentSlot = None
newSlot = None
autoRename = False


# Functions
#=============================================================
def getNewSlotName(slotName):
    return slotName.replace("c0"+currentSlot, "c0"+newSlot)




# Main
#============================================================


# Get input from the user on what
#  values they want to change and where to change them
#-------------------------------------------------------------
path = input("Please paste the path to the skin [If the script is in the root of the skin folder just press enter]\n")
if path == "":
    path = "./"

while currentSlot == None:
    currentSlot = input("What skin slot do you want to update? [Expected Value Between 0-7] \nLeave blank for auto (Don't do this if there is more than 1 skin!)\n")
    if currentSlot != "" and not bool(pattern.match(currentSlot)):
        print("\""+currentSlot+"\" is not valid input. Must be a number between [0-7], or empty\n")
        currentSlot = None

autoRename = currentSlot == ""

while newSlot == None:
    newSlot = input("What skin slot do you want this skin to move to? [Expected Value Between 0-7]\n")
    if not bool(pattern.match(newSlot)):
        print("\""+newSlot+"\" is not valid input. Must be a number between [0-7]\n")
        newSlot = None


print("\n========================================")
print("            End of Program")
print("========================================")