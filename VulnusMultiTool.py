import math
import os
import json
import yt_dlp
import ffmpeg
from pathlib import Path

# dir variables
outputpath = 'Output'
outputconvertedpath = 'Output/converted.json'
metaconvertedpath = 'Output/meta.json'

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

if not os.path.exists(outputpath):
    os.makedirs(outputpath)

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
    cls()
    optionInput = input("""Please type in which category you would like to choose.
                        
    1. Converters (eg. Sound Space - Vulnus, osu! - Sound Space)

    2. Mapping Tools (eg. Resizer, Randomizer)

    3. Miscellaneous (eg. Audio Downloader, Song Length Checker)

    If you would like to quit the program, type "q"
    If you would like to delete everything in output, type "d"

Input: """)

    # Converter Input Category -------------------------------

    if optionInput == "1":
        cls()
        ConverterInput = input("""Please type in which converter you would like to choose.
                    
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

    elif optionInput == "2":
        cls()
        mappingToolInput = input("""Please type in which Mapping Tool you would like to choose.
                    
1. Map Resizer (Vulnus)

If you would like to go back, type "b"
If you would like to quit the program, type "q"

Input: """)

        if mappingToolInput == "1":
            ssmapdata = open("map.txt")
            vulnusmapdata = open(outputconvertedpath, "w")
            vulnusmapdata.write("the yeah")
            vulnusmapdata.close()
        elif mappingToolInput.casefold() == "b":
            restart = True        
    
    # Mapping Tools Category -------------------------------
    
    elif optionInput == "3":
        cls()
        miscInput = input("""Please type in which Miscellaneous option you would like to choose.
                    
1. Audio Downloader (Youtube)

If you would like to go back, type "b"
If you would like to quit the program, type "q"

Input: """)
        if miscInput == "1":
            cls()
            url = input("""Type in your youtube URL you would like to extract audio from.

Input: """)
            cls()
            filename = input("""Please enter what you want the filename to be (you don't need to include .mp3)

Input: """)
            ydl_opts = {
                'format': 'm4a',
                'outtmpl':'Output/'+filename+'.%(ext)s',
                'postprocessors': [{  # Extract audio using ffmpeg
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                }]
            }  
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                error_code = ydl.download(url)
            os.replace("output.mp3", outputpath)
        elif mappingToolInput.casefold() == "b":
            restart = True
        
    elif optionInput.casefold() == "q":
        break
    
    elif optionInput.casefold() == "d":
        for f in os.listdir(outputpath):
            os.remove(os.path.join(outputpath, f))

    else:
        print("You did not enter a valid option.")    
    
