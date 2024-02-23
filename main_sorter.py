from ast import arg
import os.path
import cv2
import time
import argparse

startTime = time.time()

argparser = argparse.ArgumentParser()
subp = argparser.add_subparsers(dest='command')
argparser.add_argument('--infile', type=str, required=True, help="Path to Text to be sorted.")
argparser.add_argument('--outfile', type=str, required=False, help="Path to save .txt file, will default to infile path")
argparser.add_argument('--outname', type=str, required=False, help = "Name of the outputted file, will default to 'output.txt'")
args = argparser.parse_args()

input_path = args.infile

if args.outfile is not None:
    output_path = args.outfile

else:
    output_path = os.path.dirname(input_path)

if not output_path.endswith('\\'):
    output_path += '\\'

if args.outname is not None:
    output_name = args.outname + ".txt"

else:
    output_name = "output.txt"

file = open(input_path, "r")
inputText = file.read()

print("Inputted the following text: \n" + "\" " + inputText + " \"")
print("\nsorting proceeds...")

inputLength = len(inputText)
sortedStr = ""

for i in range(inputLength):
    if(inputText[i] == ";"):
        sortedStr += ";\n"
    else:
        sortedStr += inputText[i]

endTime = time.time()
deltaTime = (endTime - startTime) * 1000
deltaTimeStr = str(deltaTime)

# Output finished .txt file:
f = open(output_path + "\\" + output_name, 'w')
f.write(sortedStr)

print("\nsaved the result with the name '" + output_name + "' to '" + output_path + "'!")

f.close()
file.close()

print("\nfinished in " + deltaTimeStr + " ms")
