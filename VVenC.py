import subprocess
import sys
from pathlib import Path
import Helper

# encoder specific path variables
vvencFF_root = "codecs/vvenc"
vvencFF_exe = "./" + Helper.getEXE(vvencFF_root, "vvencFFapp")
vvencFF_encoderCfgPath = "codecs/vvenc/cfg/randomaccess_"


def encode(seqCfg, filename, tbr, preset, threads, output_path):
    print("*** vvenc encoding started; Filename: " + filename + ", TargetBitrate: " + str(tbr) + ", preset: " + preset
          + ", Threads: " + str(threads) + " ***")

    encoderConfig = vvencFF_encoderCfgPath + preset + ".cfg"
    BinaryOutput = output_path + filename + "_" + "vvencFF" + "_" \
                   + preset + "_" + str(int(tbr / 1000)) + "kbps" + "_str.bin"
    RecOutput = output_path + filename + "_" + "vvencFF" + "_" \
                + preset + "_" + str(int(tbr / 1000)) + "kbps" + "_rec.yuv"
    logfile = output_path + filename + "_" + "vvencFF" + "_" + str(threads) + "T_" \
              + preset + "_" + str(int(tbr / 1000)) + "kbps" + "_log.txt"
    targetBitrate = "--TargetBitrate=" + str(tbr)

    options = [vvencFF_exe,
               "-c", Path(encoderConfig),
               "-c", Path(seqCfg),
               "-b", Path(BinaryOutput),
               "-o", Path(RecOutput),
               targetBitrate]

    if threads > 1:
        options.append("--Threads=" + str(threads))

    log = open(Path(logfile), "w+")
    result = subprocess.run(options,
                            stdout=log,
                            stderr=sys.stdout
                            )
    log.close()

    if result.returncode == 0:
        print("*** encoding finished ***\n")
