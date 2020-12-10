import subprocess
from subprocess import PIPE
from pathlib import Path

# path variables
vtm_exe = "./encoders/VVCSoftware_VTM/bin/umake/gcc-9.3/x86_64/release/EncoderApp"
vtm_encoderConfig = Path("encoders/VVCSoftware_VTM/cfg/encoder_randomaccess_vtm_gop16.cfg")
vtm_sequenceConfig = "encoders/videoSourcefiles/"
vtm_outputPath = str("encoders/encodingOutput/")


def encode(seqCfg, filename, tbr):
    print("*** VVC-VTM encoding started; TargetBitrate = " + str(tbr))

    sequenceConfig = vtm_sequenceConfig + str(seqCfg)
    binaryOutput = vtm_outputPath + str(filename) + "_" + "VTM" + "_" + str(int(tbr / 1000)) + "kbps" + "_str.bin"
    recOutput = vtm_outputPath + str(filename) + "_" + "VTM" + "_" + str(int(tbr / 1000)) + "kbps" + "_rec.yuv"
    logfile = vtm_outputPath + str(filename) + "_" + "VTM" + "_" + str(int(tbr / 1000)) + "kbps" + "_log.txt"
    targetBitrate = "--TargetBitrate=" + str(tbr)

    log = open(Path(logfile), "w+")
    result = subprocess.run([vtm_exe,
                             "-c", vtm_encoderConfig,
                             "-c", Path(sequenceConfig),
                             "-b", Path(binaryOutput),
                             "-o", Path(recOutput),
                             targetBitrate,
                             "--PrintMSSSIM=1"],
                            stdout=log,
                            stderr=PIPE
                            )
    log.close()
