import subprocess
import sys
from pathlib import Path
import Helper

# encoder specific path variables
hm_root = "encoders/HM"
hm_exe = "./" + Helper.getEXE(hm_root, "TAppEncoder")
hm_encoderConfig = Path("encoders/HM/cfg/encoder_randomaccess_main.cfg")


def encode(seqCfg, filename, tbr, output_path):
    print("*** HEVC-HM encoding started, Filename: " + filename + ", TargetBitrate: " + str(tbr) + " ***")

    binaryOutput = output_path + filename + "_" + "HM" + "_" + str(int(tbr / 1000)) + "kbps" + "_str.bin"
    recOutput = output_path + filename + "_" + "HM" + "_" + str(int(tbr / 1000)) + "kbps" + "_rec.yuv"
    logfile = output_path + filename + "_" + "HM" + "_" + str(int(tbr / 1000)) + "kbps" + "_log.txt"
    targetBitrate = "--TargetBitrate=" + str(tbr)

    log = open(Path(logfile), "w+")
    result = subprocess.run([hm_exe,
                             "-c", hm_encoderConfig,
                             "-c", Path(seqCfg),
                             "-b", Path(binaryOutput),
                             "-o", Path(recOutput),
                             targetBitrate,
                             "--PrintMSSSIM=1"],
                            stdout=log,
                            stderr=sys.stdout
                            )
    log.close()

    if result.returncode == 0:
        print("*** encoding finished successfully ***\n")
