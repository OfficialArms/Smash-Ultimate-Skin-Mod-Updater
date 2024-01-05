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
    currentSlot = input("\nWhat skin slot do you want to update? [Expected Value Between 0-7] \n ~Note: Leave blank for auto (Don't do this if there is more than 1 skin!)\n")
    if currentSlot != "" and not bool(pattern.match(currentSlot)):
        print("\""+currentSlot+"\" is not valid input. Must be a number between [0-7], or empty\n")
        currentSlot = None

autoRename = currentSlot == ""

while newSlot == None:
    newSlot = input("\nWhat skin slot do you want this skin to move to? [Expected Value Between 0-7]\n")
    if not bool(pattern.match(newSlot)):
        print("\""+newSlot+"\" is not valid input. Must be a number between [0-7]\n")
        newSlot = None

# Manipulate each folder
#==============================================================

# All switch conditions
# 
# 1 - Character Folder: The folder is named c0x
# 2 - UI Files:         The file ends with _0x.bntx
# 3 - Sound Files:      The file ends in _c0x
# 4 - Config File:      The config.json

# Note. If it's a folder with the c0x name you don't need to go deeper
# Bonus Note: Kind of an unnecessary optimization tbh


# Update the patterns based on user input
#---------------------------------------------------------------
if autoRename:
    oldFolderPattern = re.compile("c0[0-7]")
else: 
    oldFolderPattern = re.compile("c0"+currentSlot)
    
newFolderName = "c0"+newSlot

configName = "config.json"

# Note: only apply these to the last 7 and 13 characters of the file names, respectively
if autoRename: 
    uiCharaPattern = re.compile("0\d\.bntx")  
else:
    uiCharaPattern = re.compile("0"+currentSlot+".bntx")

if autoRename:
    soundPattern = re.compile("c0\d\.nus3audio") 
else:  
    soundPattern = re.compile("c0"+currentSlot+".nus3audio")


print("\n[***DEBUG***]:\nPath: "+path)
print("currentSlot: "+currentSlot)
print("newSlot: "+newSlot)
print("autoRename: "+str(autoRename)+"\n")

print("---Patterns: ")
print("oldFolderPattern: "+str(oldFolderPattern))
print("newFolderName: "+str(newFolderName))
print("uiCharaPattern: "+str(uiCharaPattern))
print("soundPattern: "+str(soundPattern))
print("\n========================================")
print("            End of Program")
print("========================================")

input("\nPress enter to end this script")