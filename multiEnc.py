# multiEnc v.0.1
# a tool to automate encoding video files
# written by David Langmeier

import sys
import VVenC, VTM, HM

# parse arguments
encoder = sys.argv[1]
filename = sys.argv[2]
# parse list of targetbitrates
n = len(sys.argv[3])
targetBitrates = sys.argv[3][1:n-1]
targetBitrates = targetBitrates.split(',')

print("*** multiEnc 0.1 started ***\n")

if encoder == "vvenc":
    preset = sys.argv[4]
    print(preset)
    for i in targetBitrates:
        VVenC.encode(filename, int(i), preset)
elif encoder == "vtm":
    for i in targetBitrates:
        VTM.encode(filename, int(i))
elif encoder == "hm":
    for i in targetBitrates:
        HM.encode(filename, int(i))

print("*** multiEnc : all encodings done ***")
