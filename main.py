from asyncio.windows_events import NULL
import math
import os
import json
from pathlib import Path

# dir variables
outputpath = 'Output'
# variables for vulnus
outputconvertedpath = 'Output/converted.json'
metaconvertedpath = 'Output/meta.json'

settings = Path("settings.json")
if not settings.is_file():
    settingstruejson = {
        "deleteoutputfiles": True,
    }
    settingsfalsejson = {
        "deleteoutputfiles": False,
    }    
    restart = True
    while restart:
        createsettings = input("""Would you like to auto delete everything in the Output folder? (This can be changed at any time by opening the settings.json) Y/N

Input: """)
        restart = False
        if createsettings.casefold() == "y":
            opensettings = open("settings.json", "w")
            json_settings = json.dumps(settingstruejson, indent=4)
            with open("settings.json", "w") as outfile:
                outfile.write(json_settings)
            break
        elif createsettings.casefold() == "n":
            opensettings = open("settings.json", "w")
            json_settings = json.dumps(settingsfalsejson, indent=4)
            with open("settings.json", "w") as outfile:
                outfile.write(json_settings)
            break
        else:
            print("That isn't a valid input option, try again!")
            restart = True

with open("settings.json") as jsonFile:
    jsonBool = json.load(jsonFile)
    jsonFile.close()

deletesettingsjsonoption = jsonBool['deleteoutputfiles']

if deletesettingsjsonoption == True:
    for f in os.listdir(outputpath):
        os.remove(os.path.join(outputpath, f))

restart = True
while restart:
    OptionInput = input("""Please type in which category you would like to choose.
                        
    1. Converters (eg. Sound Space - Vulnus, osu! - Sound Space)

    2. Mapping Tools (eg. Resizer, Randomizer)

    3. Miscellaneous (eg. Audio Downloader, Song Length Checker)

    If you would like to quit the program, type "q"
    If you would like to delete everything in output, type "d"

Input: """)

    # Converter Input Category -------------------------------

    if OptionInput == "1":
        ConverterInput = input("""
----------------------------------------------------------

Please type in which converter you would like to choose.
                    
1. Sound Space ---> Vulnus

If you would like to go back, type "b"
If you would like to quit the program, type "q"

Input: """)
        if ConverterInput == "1":
            ssmapdata = open("map.txt")
            vulnusmapdata = open(outputconvertedpath, "w")
            vulnusmapdata.write("the yeah")
            vulnusmapdata.close()
        elif ConverterInput.casefold() == "b":
            restart = True
        elif ConverterInput.casefold() == "q":
            exit()
    # Mapping Tools Category -------------------------------

    elif OptionInput == "2":
        MappingToolInput = input("""
----------------------------------------------------------

Please type in which Mapping Tool you would like to choose.
                    
1. Map Resizer (Vulnus)

If you would like to go back, type "b"
If you would like to quit the program, type "q"

Input: """)

        if MappingToolInput == "1":
            ssmapdata = open("map.txt")
            vulnusmapdata = open(outputconvertedpath, "w")
            vulnusmapdata.write("the yeah")
            vulnusmapdata.close()
        elif MappingToolInput.casefold() == "b":
            restart = True        
    
    elif OptionInput == "3":
        MiscInput = input("""
----------------------------------------------------------

Please type in which Miscellaneous option you would like to choose.
                    
1. Audio Downloader (Youtube)

If you would like to go back, type "b"
If you would like to quit the program, type "q"

Input: """)
        if MiscInput == "1":
            print("Work In Progress") # god this is probably going to make me fucking kms
        elif MappingToolInput.casefold() == "b":
            restart = True     
        
    elif OptionInput.casefold() == "q":
        break
    
    elif OptionInput.casefold() == "d":
        for f in os.listdir(outputpath):
            os.remove(os.path.join(outputpath, f))

    else:
        print("You did not enter a valid option.")    
    
