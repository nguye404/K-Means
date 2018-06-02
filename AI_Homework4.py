import sys
import operator
from collections import OrderedDict
import numpy as np
import copy

def processFile(filename, k):
    inFile = open(filename, "r")

    D = OrderedDict()
    currentLine = inFile.readline()

    i = 0
    listCompactness = []
    listLength = []
    listWidth = []
    
    while currentLine != "":
        currentLine = currentLine.rstrip()
        curList = currentLine.split()

        # store (compactness, length, and width) as value so the key  
        # doesn't get replaced when it has same compactness
        D[i] = (float(curList[2]), float(curList[3]), float(curList[4]))
        listCompactness.append(curList[2])
        listLength.append(curList[3])
        listWidth.append(curList[4])
        #print(D[i])
        i = i + 1
        
        # read the next line in the file    
        currentLine = inFile.readline()

    print("length of dataset D = ", len(D))
    
    maxCompactness = float(max(listCompactness))
    maxLength = float(max(listLength))
    maxWidth = float(max(listWidth))
    print("max in each dimenstion: ", max(listCompactness), maxLength, maxWidth)

    # pick k random points in dataset D and make them centroids
    randIndex = -1
    C = []
    for i in range(0, k):
        randIndex = np.random.randint(0, len(D))
        coordinate = [D[randIndex][0], D[randIndex][1], D[randIndex][2]]
        if coordinate not in C:
            C.append(coordinate)
        
    C = np.array(C)
    print("initial centroids = ", C)


    dictSizeCluster = {}
    new = {}
    xyz = {} # key = centroid, value = sum of all distances to that centroid
    for i in range(0, k):
        dictSizeCluster[i] = 0
        new[i] = 0
        xyz[i] = (0, 0, 0)

    time = 0
    clusterSizeChange = True
    while(clusterSizeChange == True or time == 1000000):
        time = time + 1
        for i in range(0, len(D)):
            distDict = {}
            #print(D[i][0], "  ", D[i][1],"  ", D[i][2])
            for j in range(0, k):
                #print(float(C[j][0])**2)
                #print(C[j][0], "  ", C[j][1],"  ", C[j][2])   
                distDict[j] = (C[j][0] - D[i][0])**2 + (C[j][1] - D[i][1])**2 + (C[j][2] - D[i][2])**2
                #print(distDict[j])
            C_min = min(distDict.items(), key=operator.itemgetter(1))[0]
            new[C_min] = new[C_min] + 1
            #print("C_min[", C_min, "] = ", new[C_min])
            xyz[C_min] = (xyz[C_min][0] + D[i][0], xyz[C_min][1] + D[i][1],
                          xyz[C_min][2] + D[i][2])
        print("Iteration ", time, "\t Size of each cluster = ", new)    
        clusterSizeChange = compareClusterSize(dictSizeCluster, new, k)
        
        # update the old sizes of clusters with the new ones since it changes
        if (clusterSizeChange == True):
            dictSizeCluster = copy.deepcopy(new)

        # create a new centroid
        for i in range(0, k):
            #print(i, "cluster size = ", new[i])
            C[i] = [xyz[i][0] / new[i], xyz[i][1] / new[i], xyz[i][2] / new[i]]
            #print("C[", i, "]", C[i])
            new[i] = 0
            xyz[i] = (0, 0, 0)
        print("\n")

    print("center of each cluster ", C)

    if not clusterSizeChange:
        print("\n****Converge****")
    else:
        print("\n****Not converge****")


def compareClusterSize(prev, new, k):
    for i in range(0, k):
        if prev[i] != new[i]:
            return True
    return False
        

processFile("seeds_dataset.txt", 3)




