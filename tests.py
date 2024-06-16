import sys
import os

dir = "./traindata/dataset/"
classesCount = {0: 0, 1:0, 2:0, 3:0, 4:0}

fileCount = {}

takeFiles = []
result =  {0: 0, 1:0, 2:0, 3:0, 4:0}

# go through all files in dir

for file in os.listdir(dir):

    if file.endswith(").txt"):
        fileClassesCount = {0: 0, 1:0, 2:0, 3:0, 4:0}

        with open(dir + file, 'r') as f:
            while True:
                line = f.readline()
                if not line:
                    break

                fileClassesCount[int(line.split(" ")[0])] += 1
                classesCount[int(line.split(" ")[0])] += 1

        fileCount[file] = fileClassesCount


for file in fileCount.keys():
    if result[0] < 280:
        if fileCount[file][0] > 0:
            takeFiles.append(file)
            result[0] += fileCount[file][0]
            result[1] += fileCount[file][1]
            result[2] += fileCount[file][2]
            result[3] += fileCount[file][3]
            result[4] += fileCount[file][4]
        continue

    if result[2] < 200:
        if fileCount[file][2] > 0:
            takeFiles.append(file)
            result[0] += fileCount[file][0]
            result[1] += fileCount[file][1]
            result[2] += fileCount[file][2]
            result[3] += fileCount[file][3]
            result[4] += fileCount[file][4]
        continue

    if result[1] < 60:
        if fileCount[file][1] > 0:
            takeFiles.append(file)
            result[0] += fileCount[file][0]
            result[1] += fileCount[file][1]
            result[2] += fileCount[file][2]
            result[3] += fileCount[file][3]
            result[4] += fileCount[file][4]
        continue

    if result[3] < 55:
        if fileCount[file][3] > 0:
            takeFiles.append(file)
            result[0] += fileCount[file][0]
            result[1] += fileCount[file][1]
            result[2] += fileCount[file][2]
            result[3] += fileCount[file][3]
            result[4] += fileCount[file][4]
        continue

    if result[4] < 40:
        if fileCount[file][4] > 0:
            takeFiles.append(file)
            result[0] += fileCount[file][0]
            result[1] += fileCount[file][1]
            result[2] += fileCount[file][2]
            result[3] += fileCount[file][3]
            result[4] += fileCount[file][4]
        continue

    break

print(classesCount)
takeFiles.sort()
print(takeFiles)
print(result)