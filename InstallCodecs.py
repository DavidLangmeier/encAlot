# download and install codecs

import os, subprocess, sys
from pathlib import Path


# git https clone paths
gitHM = "https://vcgit.hhi.fraunhofer.de/jct-vc/HM.git"
gitVTM = "https://vcgit.hhi.fraunhofer.de/jvet/VVCSoftware_VTM.git"
gitVVenC = "https://github.com/fraunhoferhhi/vvenc.git"


def installHM():
    print("\n*** cloning HEVC-HM git repository ***\n")
    try:
        subprocess.run(["git", "clone", gitHM])
    except Exception as e:
        print("\n*** cloning HEVC-HM git repository FAILED ***\n")
        print(e)
        return

    print("\n*** building HEVC-HM software ***\n")
    try:
        os.chdir("HM")
        subprocess.run(["mkdir", "build"])
        os.chdir(Path("build"))
        subprocess.run(["cmake", "..", "-DCMAKE_BUILD_TYPE=Release"])
        subprocess.run(["make", "-j"])
        os.chdir("..")
        os.chdir("..")
    except Exception as e:
        print("\n*** building HEVC-HM software FAILED ***\n")
        print(e)


def installVVenC():
    print("\n*** cloning VVC-VVenC git repository ***\n")
    try:
        subprocess.run(["git", "clone", gitVVenC])
    except Exception as e:
        print("\n*** cloning VVC-VVenC git repository FAILED ***\n")
        print(e)
        return

    print("\n*** building VVC-VVenC software ***\n")
    try:
        os.chdir(Path("vvenc"))
        subprocess.run(["make", "install-release"])
        os.chdir("..")
    except Exception as e:
        print("\n*** building VVC-VVenC software FAILED ***\n")
        print(e)


def installVTM():
    print("\n*** cloning VVC-VTM git repository ***\n")
    try:
        subprocess.run(["git", "clone", gitVTM])
    except Exception as e:
        print("\n*** cloning VVC-VTM git repository FAILED ***\n")
        print(e)
        return

    print("\n*** building VVC-VTM software ***\n")
    try:
        os.chdir(Path("VVCSoftware_VTM"))
        subprocess.run(["mkdir", "build"])
        os.chdir("build")
        subprocess.run(["cmake", "..", "-DCMAKE_BUILD_TYPE=Release"])
        subprocess.run(["make"])  # with option -j the make process crashed on my machine
    except Exception as e:
        print("\n*** building VVC-VTM software FAILED ***\n")
        print(e)


def main():
    print("*** encAlot 1.0 setup started ***\n")

    # clone the git repositories and build software
    os.chdir("codecs")
    installHM()
    installVVenC()
    installVTM()

    print("\n*** setup finished ***")


if __name__ == "__main__":
    main()
