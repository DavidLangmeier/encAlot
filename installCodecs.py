# download and install codecs

import wget
import os, ssl, sys, subprocess
from pathlib import Path


# git https clone paths
gitHM = "https://vcgit.hhi.fraunhofer.de/jct-vc/HM.git"
gitVTM = "https://vcgit.hhi.fraunhofer.de/jvet/VVCSoftware_VTM.git"
gitVVenC = "https://github.com/fraunhoferhhi/vvenc.git"

# paths for the codecs
# pathHM = "encoders/HM"
# pathVTM = "encoders/VVCSoftware_VTM"
# pathVVenC = "encoders/vvenc"


# bar_progress method which is invoked automatically from wget
# def bar_progress(current, total, width=80):
#    progress_message = "Downloading: %d%% [%d / %d] bytes" % (current / total * 100, current, total)
#    sys.stdout.write("\r" + progress_message)
#    sys.stdout.flush()


# allow Python to download from websites with https protocol
# if (not os.environ.get('PYTHONHTTPSVERIFY', '') and
#         getattr(ssl, '_create_unverified_context', None)):
#     ssl._create_default_https_context = ssl._create_unverified_context

# download .zip files to codec path
# print("\n*** HEVC-HM download starting... ***")
# wget.download(urlHM, pathHM, bar=bar_progress)
# print("\n*** VVC-VTM download starting... ***")
# wget.download(urlVTM, pathVTM, bar=bar_progress)
# print("\n*** VVC-VVenC download starting... ***")
# wget.download(urlVVenC, pathVVenC, bar=bar_progress)

# clone the git repositories
print("\n*** Cloning & installing codecs now ***")
os.chdir(Path("encoders"))

print("\n*** cloning HEVC-HM git repository ***")
subprocess.run(["git", "clone", gitHM])
# os.chdir(Path("HM"))
# subprocess.run(["make"])
# os.chdir(Path(".."))
# print("Current Working Directory ", os.getcwd())

print("\n*** cloning VTM git repository ***")
subprocess.run(["git", "clone", gitVTM])
# os.chdir(Path("VVCSoftware_VTM"))
# subprocess.run(["make"])
# os.chdir(Path(".."))
# print("Current Working Directory ", os.getcwd())

print("\n*** cloning VVenC git repository ***")
subprocess.run(["git", "clone", gitVVenC])
# os.chdir(Path("vvenc"))
# subprocess.run(["make"])
# os.chdir(Path(".."))
# print("Current Working Directory ", os.getcwd())