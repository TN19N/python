from sys import argv
import numpy as np
from matplotlib import pyplot as plt 
from random import uniform
from math import sqrt

markes = ['.', '^', '2', '*', 'x', '>', '<', 'v']

class KmeansClustering:
    
    def __init__(self, max_iter=20, ncentroid=5):
        self.ncentroid = ncentroid # number of centroids
        self.max_iter = max_iter # number of max iterations to update the centroids 
        self.centroids = [] # values of the centroids

    def fit(self, X): 
        """
        Run the K-means clustering algorithm.
        For the location of the initial centroids, random pick ncentroids from the dataset.
        Args:
        -----
          X: has to be an numpy.ndarray, a matrice of dimension m * n.
        Return:
        -------
          None.
        Raises:
        -------
          This function should not raise any Exception.
        """
        max = X.max(axis=0)
        min = X.min(axis=0)
        for _ in range(0, self.ncentroid) :
            point = []
            for mx,mn in zip(max,min) :
                point.append(uniform(mn, mx))
            self.centroids.append(point)
            
        for _ in range(0, self.max_iter) :
            clusters = [[] for _ in range(0, self.ncentroid)]
            for x in X :
                minDest = None
                minIndex = None
                for index,centroid in enumerate(self.centroids) :
                    dest = sqrt(sum((e1 - e2)**2 for e1,e2 in zip(x, centroid)))
                    if minDest == None or dest < minDest :
                        minDest = dest
                        minIndex = index
                clusters[minIndex].append(x)
            for index,centroid in enumerate(self.centroids) :
                newX = sum([x[0] for x in clusters[index]])/len(clusters[index])
                newY = sum([x[1] for x in clusters[index]])/len(clusters[index]) 
                newZ = sum([x[2] for x in clusters[index]])/len(clusters[index]) 
                self.centroids[index] = [newX, newY, newZ]


    def predict(self, X): 
        """
        Predict from wich cluster each datapoint belongs to.
        Args:
        -----
          X: has to be an numpy.ndarray, a matrice of dimension m * n.
        Return:
        -------
          the prediction has a numpy.ndarray, a vector of dimension m * 1.
        Raises:
        -------
          This function should not raise any Exception.
        """
        res = np.array([], dtype=str)
        for x in X :
            minDest = None
            minIndex = None
            for index,centroid in enumerate(self.centroids) :
                dest = sqrt(sum((e1 - e2)**2 for e1,e2 in zip(x, centroid)))
                if minDest == None or dest < minDest :
                    minDest = dest
                    minIndex = index
            res = np.append(res, markes[minIndex % len(markes)])
        return res

if __name__ == '__main__' :
    
    info = {'filepath': None, 'ncentroid': None, 'max_iter': None}
    data = None

    try :
        for key,value in (arg.split('=') for arg in argv[1:]) :
            if   key == 'filepath'                      :	info[key] = value
            elif key == 'ncentroid' and int(value) >= 0 :	info[key] = int(value)
            elif key == 'max_iter' and int(value) >= 0  :	info[key] = int(value)
        if len(argv) != 4 or any(value == None for value in info.values()) is True :
            raise Exception()
    except :
        print("Usage: python Kmeans.py filepath='../path/to/file' ncentroid=[number] max_iter=[number]")
        exit(1)

    with open(info['filepath'], 'r') as file :
        data = file.readlines()
        data = [line.split(',') for line in data]
        data = np.array([[word.strip() for word in line][1:] for line in data][1:], dtype=float)
        
    kmeans = KmeansClustering(info['max_iter'], info['ncentroid'])
    kmeans.fit(data)
    marks = kmeans.predict(data)
    
    fig = plt.figure()
    fig.set_size_inches(18.5, 10.5)
    fig.savefig('Kmeans.png', dpi=100)
    ax = fig.add_subplot(projection='3d')
    for point,k in zip(data, marks) :
        ax.scatter(*point, marker=k)
    ax.set_xlabel('height')
    ax.set_ylabel('weight')
    ax.set_zlabel('bone_density')
    plt.show()