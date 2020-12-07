import subprocess
from pathlib import Path

# path variables
hm_exe = "./encoders/HM/bin/umake/gcc-9.3/x86_64/release/TAppEncoder"
hm_encoderConfig = Path("encoders/HM/cfg/encoder_randomaccess_main.cfg")
hm_sequenceConfig = Path("encoders/videoSourcefiles/BigBuckBunny.cfg")
hm_outputPath = str("encoders/encodingOutput/")


def encode(filename, tbr):
    print("*** HEVC-HM encoding with bitrate " + str(tbr) + "***\n")

    binaryOutput = hm_outputPath + str(filename) + "_" + "HM" + "_" + str(int(tbr / 1000)) + "kbps" + "_str.bin"
    recOutput = hm_outputPath + str(filename) + "_" + "HM" + "_" + str(int(tbr / 1000)) + "kbps" + "_rec.yuv"
    logfile = hm_outputPath + str(filename) + "_" + "HM" + "_" + str(int(tbr / 1000)) + "kbps" + "_log.txt"
    targetBitrate = "--TargetBitrate=" + str(tbr)

    result = subprocess.run([hm_exe,
                             "-c", hm_encoderConfig,
                             "-c", hm_sequenceConfig,
                             "-b", Path(binaryOutput),
                             "-o", Path(recOutput),
                             targetBitrate,
                             "--PrintMSSSIM=1"],
                            capture_output=True,
                            text=True
                            )

    print("stderr: ", result.stderr)
    print("stdout: ", result.stdout)
    log = open(Path(logfile), "w+")
    log.write(result.stdout)
    log.close()
