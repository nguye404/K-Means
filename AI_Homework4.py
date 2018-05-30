import sys
import operator
from collections import OrderedDict

import numpy as np

def processFile(filename):
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

        listCompactness = curList[2]
        listLength = curList[3]
        listWidth = curList[4]
        #print(D[i])
        i = i + 1
        
        # read the next line in the file    
        currentLine = inFile.readline()

    #X = np.array(list(zip(range(listCompactness), listLength, listWidth)))
    # Number of clusters
    k = 3
    # X coordinates of random centroids
    C_x = np.random.randint(0, max(listCompactness), size=k)
    # Y coordinates of random centroids
    C_y = np.random.randint(0, max(listLength), size=k)
    C_z = np.random.randint(0, max(listWidth), size=k)
    C = np.array(list(zip(C_x, C_y, C_z)), dtype=np.float32)
    print(C)

processFile("seeds_dataset.txt")




