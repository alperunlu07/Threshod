import math 
import numpy as np 
from numpy import matlib as mb
import random
 

#0.85 - 0.3
def init(hist, fitnessFonk,params = [100,100,0.95,0.2], esik = 3):  

    # return (fitnessFonk([29, 75, 155],hist))

    GN = params[0]
    PN = params[1]

    HMCR = params[2]
    PAR = params[3]

    Dim = esik
    Fonk = fitnessFonk

    Xmin = np.zeros((Dim), dtype=int) 
    Xmax = np.zeros((Dim), dtype=int) 
    for i in range(Dim):
        Xmin[i] = 15
        Xmax[i] = 240

   
    BW = 0.02 * (Xmax-Xmin)
    bwRatio = 0.99

    Fitness = np.zeros((PN),dtype=float)
    x = np.zeros((PN,Dim),dtype=float)
    # newFitness = np.zeros((1),dtype=float)
    newX = np.zeros((Dim),dtype=float)
    newFitness = 0
    bestX = np.zeros((GN,Dim),dtype=float)
    bestFitness = np.zeros((GN),dtype=float)

    # np.random.rand(FoodNumber,D)
    for i in range(Dim):
        x[:,i] = Xmin[i] + np.random.rand(PN)*(Xmax[i] - Xmin[i])

    x = x.astype(int)
    x.sort(axis = 1)

    for i in range(PN): 
        Fitness[i] = Fonk(x[i,:],hist)
        # Fitness[i] = (4 -2.1 * pow(x[i,0],2) + pow(x[i,0],4) * (1/3)) * pow(x[i,0],2) + x[i,0] * x[i,1] + (-4+4*pow(x[i,1],2))*pow(x[i,1],2)


    sortIndex = np.argsort( -1* Fitness)[:PN]
    x = x[sortIndex,:]
    Fitness = np.sort(Fitness)[::-1]

    t = 0
    while t < GN:
        # for i in range(PN):
        for j in range(Dim):
            if random.random() < HMCR:
                k = random.randint(0,PN-1)
                newX[j] = x[k, j]
                if random.random() < PAR:
                    newX[j] = int(newX[j] + (random.random() - (0.5)) * BW[j])
                
            else:
                newX[j] = int(Xmin[j] + random.random()*(Xmax[j] - Xmin[j]))

            newX[j] = (max(min(newX[j], Xmax[j]),Xmin[j]))
        
        # newFitness[i] = (4 -2.1 * pow(newX[i,0],2) + pow(newX[i,0],4) * (1/3)) * pow(newX[i,0],2) + newX[i,0] * newX[i,1] + (-4+4*pow(newX[i,1],2))*pow(newX[i,1],2)
        # print()
        newFitness = Fonk(newX[:],hist)
            
    #         if newFitness < Fitness(end)
    #     x(end, :) = xNew;
    #     Fitness(end) = newFitness;
    # end
        if newFitness > Fitness[0]:
            x[0,:] = newX
            Fitness[0] = newFitness
            
        # Fitness = np.concatenate([Fitness, newFitness])
        # x = np.concatenate([x, newX])

        # kucukten buyuge sıralı tese cevir
        # sortIndex = np.argsort( -1* Fitness)[:PN]
        # x = x[sortIndex,:]
        # Fitness.sort(reverse = True)
        sortIndex = np.argsort( -1* Fitness)[:PN]
        x = x[sortIndex,:]
        Fitness = np.sort(Fitness)[::-1]

        bestX[t,:] = x[0,:]
        bestFitness[t] = Fitness[0]

        BW = BW * bwRatio

        t += 1

    bestFitnessIndex = np.argmax(bestFitness)
    return[bestFitness[bestFitnessIndex],bestX[bestFitnessIndex,:]]