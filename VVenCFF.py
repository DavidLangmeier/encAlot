import subprocess
from pathlib import Path

# path variables
vvencFF_exe = "./encoders/vvenc/bin/release-static/vvencFFapp"
vvencFF_encoderCfgPath = str("encoders/vvenc/cfg/randomaccess_")
vvencFF_sequenceConfig = str("encoders/videoSourcefiles/")
vvencFF_outputPath = str("encoders/encodingOutput/")


def encode(seqCfg, filename, tbr, encfg, threads):
    print("*** vvenc encoding started; TargetBitrate = " + str(tbr) + ", preset: " + encfg
          + ", Threads: " + str(threads) + " ***\n")

    sequenceConfig = vvencFF_sequenceConfig + str(seqCfg)
    encoderConfig = vvencFF_encoderCfgPath + str(encfg) + ".cfg"
    BinaryOutput = (vvencFF_outputPath + str(filename) + "_" + "vvencFF" + "_"
                    + str(encfg) + "_" + str(int(tbr / 1000)) + "kbps" + "_str.bin")
    RecOutput = (vvencFF_outputPath + str(filename) + "_" + "vvencFF" + "_"
                 + str(encfg) + "_" + str(int(tbr / 1000)) + "kbps" + "_rec.yuv")
    logfile = (vvencFF_outputPath + str(filename) + "_" + "vvencFF" + "_" + str(threads) + "T_"
               + str(encfg) + "_" + str(int(tbr / 1000)) + "kbps" + "_log.txt")
    targetBitrate = "--TargetBitrate=" + str(tbr)

    options = [vvencFF_exe,
               "-c", Path(encoderConfig),
               "-c", Path(sequenceConfig),
               "-b", Path(BinaryOutput),
               "-o", Path(RecOutput),
               targetBitrate]

    if threads > 1:
        numWppThreads = "--NumWppThreads=" + str(threads)
        wppBitEqual = "--WppBitEqual=1"
        #options.append(numWppThreads)
        #options.append(wppBitEqual)
        options.append("--Threads=" + str(threads))

    log = open(Path(logfile), "w+")
    result = subprocess.run(options,
                            stdout=log,
                            stderr=log
                            )
    log.close()
