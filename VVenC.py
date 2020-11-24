import subprocess
from pathlib import Path

# path variables
vvenc_dir = Path("C:/vvenc-master/out/build/x64-Debug/source/App/vvencFFapp/")
vvenc_exe = vvenc_dir / "vvencFFapp.exe"
vvenc_encoderConfig = Path("C:/vvenc-master/cfg/randomaccess_faster.cfg")
vvenc_sequenceConfig = Path("C:/vvenc-master/cfg/BigBuckBunny.cfg")
vvenc_rfcConfig = Path("C:/vvenc-master/cfg/frc.cfg")
vvenc_outputPath = str("C:/EncodingResults/automated/")


def encode(filename, tbr, preset):
    print("*** multiEnc - VVC-VVenC encoding started; TargetBitrate = " + str(tbr) + ", preset: " + preset + " ***\n")

    BinaryOutput = vvenc_outputPath + str(filename) + "_" + "VVenC" + "_" + str(preset) + "_" + str(int(tbr / 1000)) + "kbps" + "_str.bin"
    RecOutput = vvenc_outputPath + str(filename) + "_" + "VVenC" + "_" + str(preset) + "_" + str(int(tbr / 1000)) + "kbps" + "_rec.yuv"
    logfile = vvenc_outputPath + str(filename) + "_" + "VVenC" + "_" + str(preset) + "_" + str(int(tbr / 1000)) + "kbps" + "_log.txt"
    targetBitrate = "--TargetBitrate=" + str(tbr)

    result = subprocess.run([vvenc_exe,
                             "-c", vvenc_encoderConfig,
                             "-c", vvenc_sequenceConfig,
                             "-c", vvenc_rfcConfig,
                             "-b", Path(BinaryOutput),
                             "-o", Path(RecOutput),
                             targetBitrate],
                            capture_output=True,
                            text=True
                            )

    print("stderr: ", result.stderr)
    print("stdout: ", result.stdout)
    log = open(Path(logfile), "w+")
    log.write(result.stdout)
    log.close()
