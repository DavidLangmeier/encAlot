import subprocess
from pathlib import Path

# path variables
hm_dir = Path("encoders/HEVC_HM/bin/ninja/msvc-19.27/x86_64/debug")
hm_exe = hm_dir / "TappEncoder.exe"
hm_encoderConfig = Path("encoders/HEVC_HM/cfg/encoder_randomaccess_main.cfg")
hm_sequenceConfig = Path("encoders/HEVC_HM/cfg/per-sequence/BigBuckBunny.cfg")
hm_outputPath = str("encoders/encodingOutput/")


def encode(filename, tbr):
    print("*** multiEnc: HEVC-HM encoding with bitrate " + str(tbr) + "\n")

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
