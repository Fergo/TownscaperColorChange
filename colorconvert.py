import argparse
import os
import re

parser = argparse.ArgumentParser(description='Convert colors of Townscaper blocks')
parser.add_argument('saveFile', type=str, help='.scape file to process')
parser.add_argument('mapFile', type=str, help='Text file containing each color to convert (one per line), in the format from:to')

args = parser.parse_args()

if os.path.isfile(args.saveFile) == True and os.path.isfile(args.mapFile):

    # creates a dictionary of the color mapping
    mapping = {}
    with open(args.mapFile, 'r') as mapFile:
        mapFileLines = mapFile.read().splitlines()

        for line in mapFileLines:
            split = line.split(":")
            mapping[split[0]] = split[1]
    
    with open(args.saveFile, 'r') as saveFile:
        saveFileLines = mapFile.read().splitlines()

        corners = []
        currentCorner, currentVoxel = 0, 0
        for lineNo in len(saveFileLines):
            if saveFileLines[lineNo].strip() == "</C>":
                match = re.search(r'<count>(\d+)</count>', saveFileLines[lineNo - 1])
                if match:
                    corners.append(match.group(1))
            
            if saveFileLines[lineNo].strip() == "<V>":
                originalColor = saveFileLines[lineNo + 1].replace("<t>", "").replace("</t>", "").strip()
                if originalColor in mapping:
                    originalColor = re.sub(r'\d+', mapping[originalColor], saveFileLines[lineNo + 1]) 

                currentVoxel += 1