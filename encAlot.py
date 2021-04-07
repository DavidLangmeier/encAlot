# encAlot v.0.5
# a tool to automate batch encoding of video files
# written by David Langmeier

import sys, argparse
import VVenCFF, VTM, HM


def parseArgs():
    argparser = argparse.ArgumentParser(description="encAlot help")

    argparser.add_argument("-enc", type=str, required=True, action="store", dest="enc",
                           help="Encoder can be \'hm\', \'vtm\', \'vvencFF\', or \'all\'")
    argparser.add_argument("-sc", type=str, required=True, action="store", dest="sc",
                           help="Sequence .cfg at /encoders/videoSourcefiles")
    argparser.add_argument("-fn", type=str, required=True, action="store", dest="fn",
                           help="Filename to identify output")
    argparser.add_argument("-tbr", type=int, nargs="+", required=True, action="store", dest="tbr",
                           help="Provide 4 target bitrates in bps \'w x y z\'")
    argparser.add_argument("-pre", type=str, required=False, action="store", dest="pre",
                           help="vvenc only: preset \'faster\', \'fast\', \'medium\', \'slow\' or \'slower\'")
    argparser.add_argument("-thr", type=int, required=False, action="store", dest="thr",
                           help="vvenc only: number of threads")

    return vars(argparser.parse_args())


def main():
    print("*** encAlot 0.5 started ***\n")

    args = parseArgs()
    encoder = args["enc"]
    seqCfg = args["sc"]
    filename = args["fn"]
    n = len(args["tbr"])
    targetBitrates = args["tbr"]

    if encoder == "vvencFF":
        encfg = args["pre"]
        threads = 0
        if int(args["thr"]) > 0 and args["thr"] != None :
            threads = int(args["thr"])
        for i in targetBitrates:
            VVenCFF.encode(seqCfg, filename, i, encfg, threads)

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


if __name__ == "__main__":
    main()
