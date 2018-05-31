import sys
import operator
from collections import OrderedDict

import numpy as np

def processFile(filename, k):
    inFile = open(filename, "r")

    D = OrderedDict()
    currentLine = inFile.readline()
    currentLine = inFile.readline()
    i = 1
    listCompactness = []
    listLength = []
    listWidth = []
    
    while currentLine != "":
        currentLine = currentLine.rstrip()
        curList = currentLine.split()

        # store (compactness, length, and width) as value so the key doesn't 
        # get replaced when it has same compactness
        D[i] = (float(curList[2]), float(curList[3]), float(curList[4]))

        listCompactness.append(curList[2])
        listLength.append(curList[3])
        listWidth.append(curList[4])
        #print(D[i])
        i = i + 1
        
        # read the next line in the file    
        currentLine = inFile.readline()

    #X = np.array(list(zip(range(listCompactness), listLength, listWidth)))
    print(listCompactness)
    
    maxCompactness = float(max(listCompactness))
    maxLength = float(max(listLength))
    maxWidth = float(max(listWidth))
    print(max(listCompactness), maxLength, maxWidth)
    
    # X coordinates of random centroids
    C_x = np.random.uniform(0.0, maxCompactness, size=k)
    # Y coordinates of random centroids
    C_y = np.random.uniform(0, maxLength, size=k)
    # Z coordinates of random centroids
    C_z = np.random.uniform(0, maxWidth, size=k)
    
    C = np.array(list(zip(C_x, C_y, C_z)), dtype=np.float)
    print(C)

processFile("seeds_dataset.txt", 3)




