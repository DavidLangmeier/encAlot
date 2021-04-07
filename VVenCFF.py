import subprocess
from subprocess import PIPE
from pathlib import Path

# path variables
vvencFF_exe = "./encoders/vvenc/install/bin/vvencFFapp"
vvencFF_encoderCfgPath = str("encoders/vvenc/cfg/")
vvencFF_sequenceConfig = str("encoders/videoSourcefiles/")
vvencFF_frcConfig = Path("encoders/vvenc/cfg/frc.cfg")
vvencFF_outputPath = str("encoders/encodingOutput/")


def encode(seqCfg, filename, tbr, encfg, threads):
    print("*** vvencFF encoding started; TargetBitrate = " + str(tbr) + ", encoder Config: " + encfg
          + " Threads: " + str(threads) + " ***\n")

    sequenceConfig = vvencFF_sequenceConfig + str(seqCfg)
    encoderConfig = vvencFF_encoderCfgPath + str(encfg) + ".cfg"
    BinaryOutput = (vvencFF_outputPath + str(filename) + "_" + "vvencFF" + "_"
                    + str(encfg) + "_" + str(int(tbr / 1000)) + "kbps" + "_str.bin")
    RecOutput = (vvencFF_outputPath + str(filename) + "_" + "vvencFF" + "_"
                 + str(encfg) + "_" + str(int(tbr / 1000)) + "kbps" + "_rec.yuv")
    logfile = (vvencFF_outputPath + str(filename) + "_" + "vvencFF" + "_"
               + str(encfg) + "_" + str(int(tbr / 1000)) + "kbps" + "_log.txt")
    targetBitrate = "--TargetBitrate=" + str(tbr)

    options = [vvencFF_exe,
               "-c", Path(encoderConfig),
               "-c", Path(sequenceConfig),
               "-c", vvencFF_frcConfig,
               "-b", Path(BinaryOutput),
               "-o", Path(RecOutput),
               targetBitrate]

    if threads > 0:
        numWppThreads = "--NumWppThreads=" + str(threads)
        wppBitEqual = "--WppBitEqual=1"
        options.append(numWppThreads)
        options.append(wppBitEqual)

    log = open(Path(logfile), "w+")
    result = subprocess.run(options,
                            stdout=log
                            )
    log.close()
