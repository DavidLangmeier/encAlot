import subprocess
import sys
from pathlib import Path
import Helper

# encoder specific path variables
vtm_root = "codecs/VVCSoftware_VTM"
vtm_exe = "./" + Helper.getEXE(vtm_root, "EncoderApp")
vtm_encoderConfig = Path("codecs/VVCSoftware_VTM/cfg/encoder_randomaccess_vtm_gop16.cfg")


def encode(seqCfg, filename, tbr, output_path):
    print("*** VVC-VTM encoding started; Filename: " + filename + ", TargetBitrate: " + str(tbr) + " ***")

    binaryOutput = output_path + filename + "_" + "VTM" + "_" + str(int(tbr / 1000)) + "kbps" + "_str.bin"
    recOutput = output_path + filename + "_" + "VTM" + "_" + str(int(tbr / 1000)) + "kbps" + "_rec.yuv"
    logfile = output_path + filename + "_" + "VTM" + "_" + str(int(tbr / 1000)) + "kbps" + "_log.txt"
    targetBitrate = "--TargetBitrate=" + str(tbr)

    log = open(Path(logfile), "w+")
    result = subprocess.run([vtm_exe,
                             "-c", vtm_encoderConfig,
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
        print("*** encoding finished ***\n")
