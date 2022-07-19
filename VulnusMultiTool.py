import math
import os
import json
from tkinter import W
import yt_dlp
import ffmpeg
from pathlib import Path

# dir variables
outputpath = 'Output'
outputconvertedpath = 'Output/vConvertedData.json'
outputmetapath = 'Output/meta.json'

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

# Sound Space Parsing Variables
map = open("map.txt")
mapData = map.read()
ssMap = mapData.split(',')
ssMapLength = len(ssMap)

# Vulnus Parsing Variables
vMapData = open(outputconvertedpath, "w")
vMetadata = open(outputmetapath, "w")
vMap = mapData.split('{"_time": ')
vMapAttr = vMap[0].split(' "_')
vMapLength = len(vMap)

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

2. osu! ---> Vulnus

If you would like to go back, type "b"
If you would like to quit the program, type "q"

Input: """)
        if ConverterInput == "1":
            map = open("map.txt") #opens "map.txt"
            mapData = map.read() #reads "map.txt" for map data

            ssMapDataSplit = mapData.split(',') #splits the data at "," to receive each individual x, y and time stamp
            ssMapDataLength = len(ssMapDataSplit) #finds the length of the split data
            
            vConvertedData = open(outputconvertedpath, "w") #opens the "vConvertedData.json" file located in the 'Output' folder
            vMetaData = open(outputmetapath, "w") #opens the "meta.json" file located in the 'Output' folder

            musicArtist = str(input("\nMusic Artist: "))
            mapMappers = str(input("\nMap Mapper(s): "))
            mapMusic = str(input("\nMusic Filename: "))
            mapTitle = str(input("\nMap Title: "))

            vMetaData.write('{"_artist": "'+musicArtist+'", "_difficulties": ["vConvertedData.json"], "_mappers": ["'+mapMappers+'"], "_music": "'+mapMusic+'", "_title": "'+mapTitle+'", "_version": 1}')
            #line above writes all the data the user just inputted into the "meta.json" file
            vMetaData.close()
            #line above closes the "meta.json" file to save its contents

            mapApproachDistance = int(input("\nApproach Distance: "))
            mapApproachTime = int(input("\nApproach Time (s): "))
            mapName = str(input("\nMap Name: "))
            mapOffset = int(input("\nMap Offset (ms): "))

            vConvertedData.write('{"_approachDistance": '+str(mapApproachDistance)+', "_approachTime": '+str(mapApproachTime)+', "_name": "'+mapName+'", "_notes": [{"_time": ')
            #line above writes all the data the user just inputted into the "vConvertedData.json" file
            for pos in range(1, ssMapDataLength): #loops through the list of positions and times throughout the map data
                ssMapDataParsed = ssMapDataSplit[pos].split("|") #splits the map data at "|"
                ssX = ssMapDataParsed[0] #sets the first item in the list of parsed data equal to ssX (first item will be the x coordinate of the note)
                ssY = ssMapDataParsed[1] #sets the second item in the list of parsed data equal to ssY (second item will be the y coordinate of the note)
                ssTime = ssMapDataParsed[2] #sets the third item in the list of parsed data equal to ssTime (third item will be the time stamp of the note)
                if pos == 1: #checks to see whether it is the first  
                    vConvertedData.write(str(round((int(ssTime)+mapOffset)/1000, 3))+', ')
                else:
                    vConvertedData.write('{"_time": '+str(round((int(ssTime)+mapOffset)/1000, 3))+', ')
                if ssX == "0":
                    vConvertedData.write('"_x": -1, ')
                elif ssX == "1":
                    vConvertedData.write('"_x": 0, ')
                elif ssX == "2":
                    vConvertedData.write('"_x": 1, ')
                else:
                    vConvertedData.write('"_x": '+str(float(ssX)-1)+', ')     
                if ssY == "0" and pos == ssMapLength-1:
                    vConvertedData.write('"_y": -1}]}')
                elif ssY == "0":
                    vConvertedData.write('"_y": -1}, ')
                elif ssY == "1" and pos == ssMapLength-1:
                    vConvertedData.write('"_y": 0}]}')
                elif ssY == "1":
                    vConvertedData.write('"_y": 0}, ')
                elif ssY == "2" and pos == ssMapLength-1:
                    vConvertedData.write('"_y": 1}]}')
                elif ssY == "2":
                    vConvertedData.write('"_y": 1}, ')
                elif isinstance(float(ssY), float) and pos == ssMapLength-1:
                    vConvertedData.write('"_y": '+str(float(ssY)-1)+'}]}')
                else:
                    vConvertedData.write('"_y": '+str(float(ssY)-1)+'}, ')
            vConvertedData.close()
            
        if ConverterInput == "2": # osu to vulnus
            # osu metadata parsing
            audio = mapData.split("AudioFilename: ")[1].split('\n')[0]
            songTitle = mapData.split("Title:")[1].split('\n')[0]
            songArtist = mapData.split("Artist:")[1].split('\n')[0]
            mapper = mapData.split("Creator:")[1].split('\n')[0]
            difficultyName = mapData.split("Version:")[1].split('\n')[0]
            
            hitObjects = mapData.split("[HitObjects]\n")[1]
            
            # metadata writer
            
            vMetadata.write('{"_artist": "'+songArtist+'", "_difficulties": ["'+difficultyName+'.json"], "_mappers": ["'+mapper+'"], "_music": "'+audio+'", "_title": "'+songTitle+'", "_version": 1}')
            vMetadata.close() 
            
            # hitobject parser + calculator
            

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
            map = open("map.txt")
            vMapData = open(convertedoutput, "w")
            vMapData.write("the yeah")
            vMapData.close()
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
    
