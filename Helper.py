# path of the encoder executable can differ when using different
# make versions etc. - so the executable has to be searched

import os, subprocess, sys


def getEXE(encoderDir, exeName):
    try:
        for root, dirs, files in os.walk(encoderDir):
            if exeName in files:
                return (os.path.join(root, exeName))
    except Exception as e:
        print(e)


