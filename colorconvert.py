import argparse
import os
import re

parser = argparse.ArgumentParser(description = 'Convert colors of Townscaper blocks')
parser.add_argument('saveFile', type = str, help = '.scape file to process')
parser.add_argument('mapFile', type = str, help = 'Text file containing each color to convert (one per line), in the format from:to')

args = parser.parse_args()

if os.path.isfile(args.saveFile) and os.path.isfile(args.mapFile):

    # creates a dictionary of the color mapping
    mapping = {}
    with open(args.mapFile, 'r') as mapFile:
        mapFileLines = mapFile.read().splitlines()

        for line in mapFileLines:
            split = line.split(":")
            mapping[split[0]] = split[1]
    
    # open save file
    with open(args.saveFile, 'r') as saveFile:
        saveFileLines = saveFile.read().splitlines()

        # iterate on each line
        for lineNo in range(len(saveFileLines)):
            match = re.match(r'<t>(\d+)</t>', saveFileLines[lineNo].strip())

            # if it matches a voxel type, replace its color (if exists in the mapping)
            if match:
                originalColor = match.group(1)
                if originalColor in mapping:
                    saveFileLines[lineNo] = re.sub(r'\d+', mapping[originalColor], saveFileLines[lineNo]) 

        # dump the updated file
        fileName = os.path.splitext(os.path.basename(args.saveFile))[0]
        with open(args.saveFile.replace(fileName, fileName + "_colored"), 'w') as outFile:
            outFile.writelines(s + '\n' for s in saveFileLines)