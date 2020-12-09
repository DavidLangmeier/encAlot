# encAlot v.0.3
# a tool to automate encoding video files
# written by David Langmeier

import sys
import VVenCFF, VTM, HM

# parse arguments
encoder = sys.argv[1]
seqCfg = sys.argv[2]
filename = sys.argv[3]
# parse list of targetbitrates
n = len(sys.argv[4])
targetBitrates = sys.argv[4][1:n - 1]
targetBitrates = targetBitrates.split(',')

print("*** encAlot 0.3 started ***\n")

if encoder == "vvencFF":
    encfg = sys.argv[5]
    threads = 0
    if int(sys.argv[6]) > 0 and sys.argv[6] != None :
        threads = int(sys.argv[6])
    for i in targetBitrates:
        VVenCFF.encode(seqCfg, filename, int(i), encfg, threads)

elif encoder == "vtm":
    for i in targetBitrates:
        VTM.encode(seqCfg, filename, int(i))

elif encoder == "hm":
    for i in targetBitrates:
        HM.encode(seqCfg, filename, int(i))

elif encoder == "all":
    # run VVenC
    encfg = sys.argv[5]
    threads = 0
    if int(sys.argv[6]) > 0 and sys.argv[6] != None:
        threads = int(sys.argv[6])
    for i in targetBitrates:
        VVenCFF.encode(seqCfg, filename, int(i), encfg, threads)
    # run VTM
    for i in targetBitrates:
        VTM.encode(seqCfg, filename, int(i))
    # run HM
    for i in targetBitrates:
        HM.encode(seqCfg, filename, int(i))

print("*** encAlot : all encodings done ***")
