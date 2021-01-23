# Townscaper Color Changer

## Description

This is a very simple Python script that enables you to change the colors of the buldings in Townscaper

**Before**

![Before](/screenshots/before.png?raw=true "Before")

**After**

![Before](/screenshots/after.png?raw=true "After")

## Usage

Simply call the python script passing the save file you want to change and color mapping

```colorconvert.py save.scape mappings.txt```

The save files are located in the following folder;

```C:\Users\[your username]\AppData\LocalLow\Oskar Stalberg\Townscaper\Saves```

After processing, a new file with ```_colored``` appended to its name will be created in the same directory as the original. If it's already in the ```Save``` directory, you can simply open it in game (see the remarks below regarding the save thumbnail)

## Mapping

The script uses the ```mapping.txt``` file to know which color should replace which. It's a simple list where each line represents a pattern in the format ```fromColor:toColor```. Colors go from 0 to 14 in the same order as they appear in game, from top to bottom (ie. Red = 0, White = 14).

## Remarks

The script doesn't change the ```SaveString``` neither the encoded JPG inside the save file, used as the thumbnail when loading a game. Those will be correctly overriten by the game itself on your next save.
