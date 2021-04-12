import subprocess
from pathlib import Path

# path variables
hm_exe = "./encoders/HM/bin/umake/gcc-7.5/x86_64/release/TAppEncoder"
hm_encoderConfig = Path("encoders/HM/cfg/encoder_randomaccess_main.cfg")
hm_sequenceConfig = "encoders/videoSourcefiles/"
hm_outputPath = str("encoders/encodingOutput/")


def encode(seqCfg, filename, tbr):
    print("*** HEVC-HM encoding with bitrate " + str(tbr) + "***\n")

    sequenceConfig = hm_sequenceConfig + str(seqCfg)
    binaryOutput = hm_outputPath + str(filename) + "_" + "HM" + "_" + str(int(tbr / 1000)) + "kbps" + "_str.bin"
    recOutput = hm_outputPath + str(filename) + "_" + "HM" + "_" + str(int(tbr / 1000)) + "kbps" + "_rec.yuv"
    logfile = hm_outputPath + str(filename) + "_" + "HM" + "_" + str(int(tbr / 1000)) + "kbps" + "_log.txt"
    targetBitrate = "--TargetBitrate=" + str(tbr)

    log = open(Path(logfile), "w+")
    result = subprocess.run([hm_exe,
                             "-c", hm_encoderConfig,
                             "-c", Path(sequenceConfig),
                             "-b", Path(binaryOutput),
                             "-o", Path(recOutput),
                             targetBitrate,
                             "--PrintMSSSIM=1"],
                            stdout=log,
                            stderr=log
                            )
    log.close()
