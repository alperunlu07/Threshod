import math 
import numpy as np 
from numpy import matlib as mb
import random




def init(hist, fitnessFonk, params = [100,100,0.4,0.4,0.2], esik = 3):  


    GN = params[0]
    PN = params[1]

    Inf = math.inf

    alpha = params[2]
    gamma = params[3]
    beta0 = params[4] 

    Dim = esik
    Fonk = fitnessFonk
    Xmin = np.zeros((Dim), dtype=int) 
    Xmax = np.zeros((Dim), dtype=int) 
    for i in range(Dim):
        Xmin[i] = 0
        Xmax[i] = 255

    Fitness = np.zeros((PN),dtype=float)
    x = np.zeros((PN,Dim),dtype=int)
    popFitness = np.zeros((PN),dtype=float)
    popX = np.zeros((PN,Dim),dtype=float)

    bestX = np.zeros((GN,Dim),dtype=float)
    bestFitness = np.zeros((GN),dtype=float)

    # np.random.rand(FoodNumber,D)
    for i in range(Dim):
        x[:,i] = Xmin[i] + np.random.rand(PN)*(Xmax[i] - Xmin[i])
    x = x.astype(int)
    x.sort(axis = 1)
    # Positions[:,1] = Xmin[1] + np.random.rand(1, PN)*(Xmax[1] - Xmin[1])
    # Positions = Positions.astype(int)
    # Positions.sort(axis = 1)
    # a = 2

    for i in range(PN): 
        Fitness[i] = Fonk(x[i,:],hist)
        # Fitness[i] = (4 -2.1 * pow(x[i,0],2) + pow(x[i,0],4) * (1/3)) * pow(x[i,0],2) + x[i,0] * x[i,1] + (-4+4*pow(x[i,1],2))*pow(x[i,1],2)

    alphaRatio = 0.98

    sortIndex = np.argsort( -1* Fitness)[:PN]
    x = x[sortIndex,:]
    Fitness = np.sort(Fitness)[::-1]



    t = 0
    while t < GN:
        for i in range(PN):
            popFitness[i] = 0
            for j in range(i):
                r = math.sqrt(pow((x[i,0]- x[j,0]),2) + pow((x[i,1]- x[j,1]),2))
                if Fitness[j] > Fitness[i]:
                    beta = beta0 * math.exp(-gamma * pow(r,Dim))
                    newX = x[i,:] + beta * (x[j,:] - x[i,:]) + alpha * (random.random() - (0.5))
                    
                    for k in range(Dim):
                        newX[k] = int(max(min(newX[k], Xmax[k]),Xmin[k]))
                    
                    # newFitness = (4 -2.1 * pow(newX[0],2) + pow(newX[0],4) * (1/3)) * pow(newX[0],2) + newX[0] * newX[1] + (-4+4*pow(newX[1],2))*pow(newX[1],2)
                    newFitness = Fonk(newX,hist)

                    if newFitness >= popFitness[i]:
                        popX [i,:] = newX
                        popFitness[i] = newFitness
        Fitness = np.concatenate([Fitness, popFitness])
        x = np.concatenate([x, popX])

        # kucukten buyuge sıralı tese cevir
        sortIndex = np.argsort( -1* Fitness)[:PN]
        x = x[sortIndex,:]
        # Fitness.sort(reverse = True)
        Fitness = np.sort(Fitness)[::-1]

        x = x[0:PN,:]
        Fitness = Fitness[0:PN]

        bestX[t,:] = x[0,:]
        bestFitness[t] = Fitness[0]

        alpha *= alphaRatio

        t += 1

    bestFitnessIndex = np.argmax(bestFitness)
    return([bestFitness[bestFitnessIndex],bestX[bestFitnessIndex,:]])

   

