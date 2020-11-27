# encAlot v.0.2
# a tool to automate encoding video files
# written by David Langmeier

import sys
import VVenCFF, VTM, HM

# parse arguments
encoder = sys.argv[1]
filename = sys.argv[2]
# parse list of targetbitrates
n = len(sys.argv[3])
targetBitrates = sys.argv[3][1:n - 1]
targetBitrates = targetBitrates.split(',')

print("*** encAlot 0.2 started ***\n")

if encoder == "vvencFF":
    encfg = sys.argv[4]
    threads = 0
    if int(sys.argv[5]) > 0 and sys.argv[5] != None :
        threads = int(sys.argv[5])
    for i in targetBitrates:
        VVenCFF.encode(filename, int(i), encfg, threads)

elif encoder == "vtm":
    for i in targetBitrates:
        VTM.encode(filename, int(i))

elif encoder == "hm":
    for i in targetBitrates:
        HM.encode(filename, int(i))

print("*** encAlot : all encodings done ***")
