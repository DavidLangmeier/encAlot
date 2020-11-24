import subprocess
from pathlib import Path

# path variables
vtm_dir = Path("C:/VVCSoftware_VTM-master/bin/ninja/msvc-19.27/x86_64/debug")
vtm_exe = vtm_dir / "EncoderApp.exe"
vtm_encoderConfig = Path("C:/VVCSoftware_VTM-master/cfg/encoder_randomaccess_vtm_gop16.cfg")
vtm_sequenceConfig = Path("C:/VVCSoftware_VTM-master/cfg/per-sequence/BigBuckBunny.cfg")
vtm_outputPath = str("C:/EncodingResults/automated/")


def encode(filename, tbr):
    print("*** multiEnc - VVC-VTM encoding started; TargetBitrate = " + str(tbr))

    binaryOutput = vtm_outputPath + str(filename) + "_" + "VTM" + "_" + str(int(tbr / 1000)) + "kbps" + "_str.bin"
    recOutput = vtm_outputPath + str(filename) + "_" + "VTM" + "_" + str(int(tbr / 1000)) + "kbps" + "_rec.yuv"
    logfile = vtm_outputPath + str(filename) + "_" + "VTM" + "_" + str(int(tbr / 1000)) + "kbps" + "_log.txt"
    targetBitrate = "--TargetBitrate=" + str(tbr)

    result = subprocess.run([vtm_exe,
                             "-c", vtm_encoderConfig,
                             "-c", vtm_sequenceConfig,
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
