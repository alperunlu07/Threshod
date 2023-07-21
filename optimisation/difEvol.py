import numpy as np
import random
import math 
#GN = 100, PN = 100, CO = 0.5, MO = 0.5
def init(hist, fitnessFonk, params = [100,100,0.7,0.5], esik = 3):      
    
    GN = int(params[0])
    PN = int(params[1])
    CR = int(params[2])
    F = int(params[3])

    Dim = esik
    Fonk = fitnessFonk

    Xmin = np.zeros((Dim), dtype=int) 
    Xmax = np.zeros((Dim), dtype=int) 
    for i in range(Dim):
        Xmin[i] = 0
        Xmax[i] = 255
    
    
    Fitness = np.zeros((PN),dtype=float)
    x = np.zeros((PN,Dim),dtype=float)

    x1t = np.zeros((Dim),dtype=float)
    
    bestX = np.zeros((GN,Dim),dtype=float)
    bestFitness = np.zeros((GN),dtype=float)

    for i in range(Dim):
        x[:,i] = Xmin[i] + np.random.rand(PN)*(Xmax[i] - Xmin[i])
    x = x.astype(int)
    x.sort(axis = 1)

    
    for i in range(PN): 
        Fitness[i] = Fonk(x[i,:],hist)

    
    for i in range(GN):
        for j in range(PN):
            
            r1 = math.floor(random.random() * PN)
            r2 = math.floor(random.random() * PN)
            r3 = math.floor(random.random() * PN)
            while r1 == j:
                r1 = math.floor(random.random() * PN)

            while r2 == j or r2 == r1:
                r2 = math.floor(random.random() * PN)

            while r3 == j or r3 == r2 or r3 == r1:
                r3 = math.floor(random.random() * PN)

            for k in range(Dim):
                x1t[k] = x[r3,k] + F * (x[r1,k] - x[r2,k])
            
            x1c = np.zeros((Dim),dtype=float)

            for k in range(Dim):
                c = random.random()
                if c <= CR:
                    x1c[k] = x1t[k]
                else:
                    x1c[k] = x[j,k]

                x1c[k] = max(min(x1c[k],Xmax[k]),Xmin[k])
            x1c = x1c.astype(int)
            x1c.sort()
            # FitC = (4 -2.1 * pow(x1c[0],2) + pow(x1c[0],4)*(1/3)) * pow(x1c[0],2) + x1c[0] * x1c[1] + (-4+4*pow(x1c[1],2))*pow(x1c[1],2)
            FitC = Fonk(x1c,hist)

            if FitC > Fitness[j]:
                for k in range(Dim):
                    x[j,k] = x1c[k]
                    Fitness[j] = FitC
            
        bestFitnessIndex = np.argmax(Fitness)
        bestFitness[i] = Fitness[bestFitnessIndex]
        bestX[i,:] = x[bestFitnessIndex,:]


    bestFitnessIndex = np.argmax(bestFitness)
    return [bestFitness[bestFitnessIndex],bestX[bestFitnessIndex,:]]