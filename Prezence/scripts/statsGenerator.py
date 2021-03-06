import os
import numpy
import csv
import itertools

numericMetrics = [
    "clarity",
    "volume",
    "head_gaze",
    "speed"
]

gestures = [
    "covering_mouth",
    "poor_posture",
    "turning_away",
    "folding_arms",
    "looking_down"
]

# below is old style
def getMeans(folders):
    allData = {}
    for folder in folders:
        print "Folder: " + folder
        allData[folder] = {}
        for nm in numericMetrics:
            allData[folder][nm] = { "data": [], "mean": 0, "median": 0, "sd": 0, "variance": 0}
            data = []
            file = open(folder+"/"+nm+".txt", "r")
            for line in file:
                data.append(float(line.rstrip("\n").split()[1]))
            file.close()
            allData[folder][nm]["data"] = data
            allData[folder][nm]["mean"] = numpy.mean(data)
            allData[folder][nm]["median"] = numpy.median(data)
            allData[folder][nm]["sd"] = numpy.std(data)
            allData[folder][nm]["variance"] = numpy.var(data)
            print nm
            print allData[folder][nm]["mean"]
    return allData

def getResultsFolders():
    folders = []
    for folder in os.listdir("results"):
        folders.append("results/"+folder)
    return folders

def numericDataToFiles(folders):
    for metric in numericMetrics:
        dataByMetric = {}
        for folder in folders:
            if folder == "results/.DS_Store":
                continue
            name = folder.split("/")[1]
            dataByMetric[name] = []

            file = open(folder+"/"+metric+".txt", "r")
            for line in file:
                dataByMetric[name].append(float(line.rstrip("\n").split()[1]))
            file.close()

        with open('scripts/results/data_by_person_'+metric+'.csv', 'wb') as f:
            writer = csv.writer(f)
            writer.writerow(dataByMetric.keys())
            writer.writerows(itertools.izip_longest(*dataByMetric.values()))

def gesturesToFiles(folders):
    for gesture in gestures:
        dataByGesture = {}
        for folder in folders:
            if folder == "results/.DS_Store":
                continue
            name = folder.split("/")[1]
            dataByGesture[name] = []

            file = open(folder+"/gesture.txt", "r")
            for line in file:
                newG = line.rstrip("\n").split()[1]
                if newG == gesture:
                    dataByGesture[name].append(1)
                else:
                    dataByGesture[name].append(0)
            file.close()

        with open('scripts/results/data_by_person_'+gesture+'.csv', 'wb') as f:
            writer = csv.writer(f)
            writer.writerow(dataByGesture.keys())
            writer.writerows(itertools.izip_longest(*dataByGesture.values()))



def main():
    folders = getResultsFolders()
    numericDataToFiles(folders)
    gesturesToFiles(folders)

main()