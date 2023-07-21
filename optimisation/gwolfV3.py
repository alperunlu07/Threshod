import math 
import numpy as np 
from numpy import matlib as mb
import random

def init(hist, fitnessFonk, params = [100,100,3], esik = 3):  

    GN = params[0]
    PN = params[1]
    a = params[2]
    hist = hist
    Inf = math.inf
    Dim = esik
    bestCount = 3

    Xmin = np.zeros((Dim), dtype=int) 
    Xmax = np.zeros((Dim), dtype=int) 
    for i in range(Dim):
        Xmin[i] = 0
        Xmax[i] = 255


    

    Fitness = np.zeros((PN),dtype=float)
    Positions = np.zeros((PN,Dim),dtype=float)

    kurtFitness = np.zeros((bestCount),dtype=float)
    kurtPosition = np.zeros((Dim, bestCount),dtype=float)
    kurtX = np.zeros((bestCount),dtype=float)

    # alphaFitness = math.inf
    # alphaPosition = np.zeros((Dim),dtype=float)
    # betaFitness = math.inf
    # betaPosition = np.zeros((Dim),dtype=float)
    # deltaFitness = math.inf
    # deltaPosition = np.zeros((Dim),dtype=float)

    bestPositions = np.zeros((GN,Dim),dtype=float)
    bestFitness = np.zeros((GN),dtype=float)

    # np.random.rand(FoodNumber,D)
    for i in range(Dim):
        Positions[:,i] = Xmin[i] + np.random.rand(PN)*(Xmax[i] - Xmin[i])
    # Positions[:,1] = Xmin[1] + np.random.rand(1, PN)*(Xmax[1] - Xmin[1])
    Positions = Positions.astype(int)
    Positions.sort(axis = 1)
    



    for i in range(PN): 
        Fitness[i] = fitnessFonk(Positions[i,:],hist)
        # Fitness[i] = (4 -2.1 * pow(Positions[i,0],2) + pow(Positions[i,0],4) * (1/3)) * pow(Positions[i,0],2) + Positions[i,0] * Positions[i,1] + (-4+4*pow(Positions[i,1],2))*pow(Positions[i,1],2)

    for i in range(bestCount):
        
        minFitnessIndex = np.argmax(Fitness)
        kurtFitness[i] = Fitness[minFitnessIndex]
        kurtPosition[i] = Positions[minFitnessIndex,:]
        Fitness[minFitnessIndex] = -1

    # minFitnessIndex = np.argmax(Fitness)
    # alphaFitness = Fitness[minFitnessIndex]
    # alphaPosition = Positions[minFitnessIndex,:]
    # Fitness[minFitnessIndex] = Inf

    # minFitnessIndex = np.argmax(Fitness)
    # betaFitness = Fitness[minFitnessIndex]
    # betaPosition = Positions[minFitnessIndex,:]
    # Fitness[minFitnessIndex] = Inf

    # minFitnessIndex = np.argmax(Fitness)
    # deltaFitness = Fitness[minFitnessIndex]
    # deltaPosition = Positions[minFitnessIndex,:]

    t = 0
    while t < GN:
        for i in range(PN):
            for j in range(Dim):
                for k in range(bestCount):
                    r1 = random.random()
                    r2 = random.random()
                    A1 = 2 * a * r1 - a
                    C1 = 2 * r2
                    alphaD = abs(C1 * kurtPosition[j, k] - Positions[i,j])
                    kurtX[k] = kurtPosition[j, k] - A1 * alphaD  

                Positions[i,j] = int(np.sum(kurtX) / bestCount)
                # r1 = random.random()
                # r2 = random.random()
                # A1 = 2 * a * r1 - a
                # C1 = 2 * r2
                # alphaD = abs(C1 * alphaPosition[j] - Positions[i,j])
                # X1 = alphaPosition[j] - A1 * alphaD  

                # r1 = random.random()
                # r2 = random.random()
                # A2 = 2 * a * r1 - a
                # C2 = 2 * r2
                # betaD = abs(C2 * betaPosition[j] - Positions[i,j])
                # X2 = betaPosition[j] - A2 * betaD  

                # r1 = random.random()
                # r2 = random.random()
                # A3 = 2 * a * r1 - a
                # C3 = 2 * r2
                # deltaD = abs(C1 * deltaPosition[j] - Positions[i,j])
                # X3 = deltaPosition[j] - A3 * alphaD  

                # #round
                # Positions[i,j] = int((X1 + X2 + X3) / 3)

        Positions.sort(axis = 1)

        a = 2 - t * ((2)/GN)
        for i in range(PN):
            for j in range(Dim):
                Positions[i,j] = int(max(min(Positions[i,j], Xmax[j]),Xmin[j]))
            # Positions[i,1] = max(min(Positions[i,1], Xmax[1]),Xmin[1])

        for i in range(PN): 
            Fitness[i] = fitnessFonk(Positions[i,:],hist)
            # Fitness[i] = (4 -2.1 * pow(Positions[i,0],2) + pow(Positions[i,0],4) * (1/3)) * pow(Positions[i,0],2) + Positions[i,0] * Positions[i,1] + (-4+4*pow(Positions[i,1],2))*pow(Positions[i,1],2)


        for i in range(bestCount):        
            minFitnessIndex = np.argmax(Fitness)
            kurtFitness[i] = Fitness[minFitnessIndex]
            kurtPosition[i] = Positions[minFitnessIndex,:]
            Fitness[minFitnessIndex] = -1

        # minFitnessIndex = np.argmax(Fitness)
        # alphaFitness = Fitness[minFitnessIndex]
        # alphaPosition = Positions[minFitnessIndex,:]
        # Fitness[minFitnessIndex] = Inf

        # minFitnessIndex = np.argmax(Fitness)
        # betaFitness = Fitness[minFitnessIndex]
        # betaPosition = Positions[minFitnessIndex,:]
        # Fitness[minFitnessIndex] = Inf

        # minFitnessIndex = np.argmax(Fitness)
        # deltaFitness = Fitness[minFitnessIndex]
        # deltaPosition = Positions[minFitnessIndex,:]

        # bestPositions[t,:] = alphaPosition
        # bestFitness[t] = alphaFitness
        t = t + 1

    bestFitnessIndex = np.argmax(bestFitness)
    return[bestFitness[bestFitnessIndex],bestPositions[bestFitnessIndex,:]]
    # print(bestPositions[bestFitnessIndex,:])
    # print(bestFitness[bestFitnessIndex])