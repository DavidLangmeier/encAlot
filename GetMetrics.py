# Search values important for evaluation (runtime, bitrate, psnr, ms-ssim, vmaf)
# write values to .csv file for further processing in excel

import os
import os.path
from os import path
import re
import csv

# folder = "encoders/encodingOutput/results720pITT/"
folder = "encoders/encodingOutput/"


def getMetricsFromTXT(filename):
    try:
        with open(folder + filename, "rt") as myfile:
            metrics = []
            bitrate = 2  # default bitrate position for HM, VTM and vvenc
            runtime = 2  # default runtime position for HM

            if "vvenc" in filename or "VTM" in filename:
                runtime = 5

            for line in myfile:
                # search for bitrate
                if " a " in line:
                    split = line.split()
                    print("Bitrate=" + split[bitrate])
                    metrics.append(split[bitrate])

                # search for runtime
                if "Total Time" in line:
                    split = line.split()
                    print("Runtime=" + split[runtime])
                    metrics.append(split[runtime])

            return metrics

    except Exception as e:
        print(e)


def getMetricsFromXML(xmlFilename):
    print("*** Additional metrics exist ***")

    try:
        with open(folder + xmlFilename, 'r') as myfile:
            metrics = []

            for line in myfile:
                if "fyi" in line:
                    split = line.split("\"")
                    print("VMAF=" + split[3])
                    print("PSNR=" + split[5])
                    print("MS-SSIM=" + split[9])
                    metrics.append(split[3])
                    metrics.append(split[5])
                    metrics.append(split[9])

            return metrics

    except Exception as e:
        print(e)


def buildFilename(filename):
    filenameSplit = filename.split("_")
    xmlFilename = ""
    for i in range((len(filenameSplit) - 1)):
        xmlFilename = xmlFilename + filenameSplit[i] + "_"
    xmlFilename += "rec.yuv.xml"
    return xmlFilename


def buildTableEntry(filename):
    filenameSplit = filename.split("_")
    tableEntry = ""
    for i in range((len(filenameSplit) - 2)):
        tableEntry = tableEntry + filenameSplit[i] + "_"
    tableEntry += filenameSplit[len(filenameSplit) - 2]
    return tableEntry


# taken from: https://stackoverflow.com/questions/2669059/how-to-sort-alpha-numeric-set-in-python
def sorted_nicely(input):
    """ Sort the given iterable in the way that humans expect."""
    convert = lambda text: int(text) if text.isdigit() else text
    alphanum_key = lambda key: [convert(c) for c in re.split('([0-9]+)', key)]
    return sorted(input, key=alphanum_key)


def main():
    processedFiles = 0

    try:
        # create csv file with header line
        with open('encoders/encodingOutput/metrics.csv', mode='w') as metrics_csv:
            metrics_writer = csv.writer(metrics_csv, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            metrics_writer.writerow(["Filename", "Bitrate", "Runtime", "VMAF", "PSNR", "MS-SSIM"])

            # iterate over all files in given folder
            for filename in sorted_nicely(os.listdir(folder)):
                csvRow = []

                # get metrics from encoding output and write to csvRow
                if filename.endswith("log.txt"):
                    print("*** Current File: " + filename + " ***")
                    print("TableEntry=" + buildTableEntry(filename))
                    csvRow.append(buildTableEntry(filename))

                    for entry in getMetricsFromTXT(filename):
                        csvRow.append(entry)
                    processedFiles += 1

                    # search for libVMAF output (xml file) with same filename
                    # if it exists get metrics and write to csvRow
                    xmlFilename = buildFilename(filename)
                    if path.exists(folder + xmlFilename):
                        for entry in getMetricsFromXML(xmlFilename):
                            csvRow.append(entry)
                        processedFiles += 1

                # write row to csv file
                if len(csvRow) != 0:
                    print("ROW: " + str(csvRow) + "\n")
                    metrics_writer.writerow(csvRow)

            print("*** Processed " + str(processedFiles) + " files in total ***")

    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
