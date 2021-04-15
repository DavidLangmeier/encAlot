# encAlot 1.0
# a tool to automate batch encoding of video files and extract metrics from encoder and libVMAF output
# written by David Langmeier

import sys, argparse
import VVenC, VTM, HM

# shared path variables
output_path = "encodingOutput/"
seqCfg_path = "videoSources/"


def parseArgs():
    argparser = argparse.ArgumentParser(description="encAlot 1.0")

    argparser.add_argument("-enc", type=str, required=True, dest="enc",
                           help="Encoder has to be <hm>, <vtm>, <vvenc>, or <all>")
    argparser.add_argument("-sc", type=str, required=True, dest="sc",
                           help="Sequence specific config file <example.cfg>. Has to be at encAlot/videoSources")
    argparser.add_argument("-fn", type=str, required=True, dest="fn",
                           help="Filename prefix for better output identification")
    argparser.add_argument("-tbr", type=int, nargs="+", required=True, dest="tbr",
                           help="Provide 1-n target bitrates in bps <tbr1 tbr2 tbr3 ...>")
    argparser.add_argument("-pre", type=str, required=False, dest="pre",
                           help="vvenc only - preset has to be <faster>, <fast>, <medium>, <slow> or <slower>")
    argparser.add_argument("-thr", type=int, required=False, dest="thr", default=1,
                           help="vvenc only - number of threads, default=1")

    return vars(argparser.parse_args())


def main():
    # Argument parsing
    args = parseArgs()
    encoder = args["enc"]
    seqCfg = seqCfg_path + args["sc"]
    filename = args["fn"]
    targetBitrates = args["tbr"]

    # start the actual encoder
    print("*** encAlot 1.0 started ***\n")

    if encoder == "vvenc":
        encfg = args["pre"]
        threads = 1
        if int(args["thr"]) > 1 and args["thr"] is not None:
            threads = int(args["thr"])
        for i in targetBitrates:
            VVenC.encode(seqCfg, filename, i, encfg, threads, output_path)

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
        if int(args["thr"]) > 1 and args["thr"] is not None:
            threads = int(args["thr"])
        for i in targetBitrates:
            VVenC.encode(seqCfg, filename, int(i), encfg, threads, output_path)
        # VTM
        for i in targetBitrates:
            VTM.encode(seqCfg, filename, int(i), output_path)
        # HM
        for i in targetBitrates:
            HM.encode(seqCfg, filename, int(i), output_path)

    else:
        print("*** ERROR: Something went wrong. Please check if a valid encoder [-enc] was provided or call --help ***")
        return

    print("*** All encodings done ***")


if __name__ == "__main__":
    main()
