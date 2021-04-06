# download and install codecs

import os, subprocess
from pathlib import Path


# git https clone paths
gitHM = "https://vcgit.hhi.fraunhofer.de/jct-vc/HM.git"
gitVTM = "https://vcgit.hhi.fraunhofer.de/jvet/VVCSoftware_VTM.git"
gitVVenC = "https://github.com/fraunhoferhhi/vvenc.git"


# clone the git repositories
print("\n*** encAlot - cloning & building codecs now ***")
os.chdir("encoders")

print("\n*** cloning HEVC-HM git repository ***\n")
subprocess.run(["git", "clone", gitHM])
print("\n*** building HEVC-HM software ***\n")
os.chdir("HM")
subprocess.run(["mkdir", "build"])
os.chdir(Path("build"))
subprocess.run(["cmake", "..", "-DCMAKE_BUILD_TYPE=Release"])
subprocess.run(["make", "-j"])
os.chdir("..")
os.chdir("..")

print("\n*** cloning VVC-VVenC git repository ***\n")
subprocess.run(["git", "clone", gitVVenC])
print("\n*** building VVC-VVenC software ***\n")
os.chdir(Path("vvenc"))
subprocess.run(["make", "install-release"])
os.chdir("..")

print("\n*** cloning VVC-VTM git repository ***\n")
subprocess.run(["git", "clone", gitVTM])
print("\n*** building VVC-VTM software ***\n")
os.chdir(Path("VVCSoftware_VTM"))
subprocess.run(["mkdir", "build"])
os.chdir("build")
subprocess.run(["cmake", "..", "-DCMAKE_BUILD_TYPE=Release"])
subprocess.run(["make"])    # with option -j the make process crashed on my machine
os.chdir("..")
os.chdir("..")

print("\n*** all codecs installed and ready ***")