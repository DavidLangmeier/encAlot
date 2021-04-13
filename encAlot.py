# encAlot
# a tool to automate batch encoding of video files
# and extracting metrics from the encoders output and libVMAF files
# written by David Langmeier

import sys, argparse
import VVenCFF, VTM, HM

# shared path variables
output_path = "encoders/encodingOutput/"
seqCfg_path = "encoders/videoSourcefiles/"


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
    argparser.add_argument("-thr", type=int, required=False, action="store", dest="thr", default=1,
                           help="vvenc only: number of threads")

    return vars(argparser.parse_args())


def main():
    print("*** encAlot started ***\n")

    # Argument parsing
    args = parseArgs()
    encoder = args["enc"]
    seqCfg = seqCfg_path + args["sc"]
    filename = args["fn"]
    targetBitrates = args["tbr"]

    # start the actual encoder
    if encoder == "vvencFF":
        encfg = args["pre"]
        threads = 1
        if int(args["thr"]) > 1 and args["thr"] is not None:
            threads = int(args["thr"])
        for i in targetBitrates:
            VVenCFF.encode(seqCfg, filename, i, encfg, threads, output_path)

    elif encoder == "vtm":
        for i in targetBitrates:
            VTM.encode(seqCfg, filename, int(i), output_path)

    elif encoder == "hm":
        for i in targetBitrates:
            HM.encode(seqCfg, filename, int(i), output_path)

    elif encoder == "all":
        # VVenC
        encfg = args["pre"]
        threads = 1
        if int(args["thr"]) > 1 and args["thr"] != None:
            threads = int(args["thr"])
        for i in targetBitrates:
            VVenCFF.encode(seqCfg, filename, int(i), encfg, threads)
        # VTM
        for i in targetBitrates:
            VTM.encode(seqCfg, filename, int(i))
        # HM
        for i in targetBitrates:
            HM.encode(seqCfg, filename, int(i))

    else:
        print("*** ERROR: Something went wrong. Please check if a valid encoder [-enc] was provided or call --help ***")
        return

    print("*** All encodings done ***")


if __name__ == "__main__":
    main()
