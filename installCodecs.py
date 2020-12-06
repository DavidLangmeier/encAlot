# download and install codecs

import os, subprocess
from pathlib import Path


# git https clone paths
gitHM = "https://vcgit.hhi.fraunhofer.de/jct-vc/HM.git"
gitVTM = "https://vcgit.hhi.fraunhofer.de/jvet/VVCSoftware_VTM.git"
gitVVenC = "https://github.com/fraunhoferhhi/vvenc.git"


# clone the git repositories
print("\n*** Cloning & installing codecs now ***")
os.chdir(Path("encoders"))

print("\n*** cloning HEVC-HM git repository ***")
subprocess.run(["git", "clone", gitHM])
os.chdir(Path("HM"))
subprocess.run(["mkdir", "build"])
subprocess.run(["cd", "build"])
subprocess.run(["cmake", "..", "-DCMAKE_BUILD_TYPE=Release"])
subprocess.run(["make -j"])
os.chdir(Path(".."))

print("\n*** cloning VTM git repository ***")
subprocess.run(["git", "clone", gitVTM])
os.chdir(Path("VVCSoftware_VTM"))
subprocess.run(["mkdir", "build"])
subprocess.run(["cd", "build"])
subprocess.run(["cmake", "..", "-DCMAKE_BUILD_TYPE=Release"])
subprocess.run(["make -j"])
os.chdir(Path(".."))

print("\n*** cloning VVenC git repository ***")
subprocess.run(["git", "clone", gitVVenC])
os.chdir(Path("vvenc"))
subprocess.run(["make"])
os.chdir(Path(".."))

print("\n*** all codecs installed and ready ***")