# download and install codecs

import os, subprocess
from pathlib import Path

# git https clone paths
gitHM = "https://vcgit.hhi.fraunhofer.de/jct-vc/HM.git"
gitVTM = "https://vcgit.hhi.fraunhofer.de/jvet/VVCSoftware_VTM.git"
gitVVenC = "https://github.com/fraunhoferhhi/vvenc.git"

# clone the git repositories
# print("\n*** Cloning & installing codecs now ***")
os.chdir("encoders")


def installHM():
    print("\n*** cloning HEVC-HM git repository ***")
    os.chdir("encoders")
    subprocess.run(["git", "clone", gitHM])
    os.chdir("HM")
    subprocess.run(["mkdir", "build"])
    os.chdir(Path("build"))
    subprocess.run(["cmake", "..", "-DCMAKE_BUILD_TYPE=Release"])
    subprocess.run(["make", "-j"])
# os.chdir("..")
# os.chdir("..")
    print("\n*** HEVC-HM installation complete ***\n")


def installVVenC():
    print("\n*** cloning VVenC git repository ***")
    os.chdir("encoders")
    subprocess.run(["git", "clone", gitVVenC])
    os.chdir(Path("vvenc"))
    subprocess.run(["make", "install-release"])
# os.chdir("..")
    print("\n*** VVC-VVenC installation complete ***\n")


def installVTM():
    print("\n*** cloning VTM git repository ***")
    os.chdir("encoders")
    subprocess.run(["git", "clone", gitVTM])
    os.chdir(Path("VVCSoftware_VTM"))
    subprocess.run(["mkdir", "build"])
    os.chdir("build")
    subprocess.run(["cmake", "..", "-DCMAKE_BUILD_TYPE=Release"])
    subprocess.run(["make", "-j"])
# os.chdir("..")
# os.chdir("..")
    print("\n*** VVC-VTM installation complete ***\n")

# print("\n*** all codecs installed and ready ***")
