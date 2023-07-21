import math 
import numpy as np 
from numpy import matlib as mb
import random
 


def init(hist, fitnessFonk, params = [100,100,1,2,0.5], esik = 3):  

    GN = params[0] 
    PN = params[1]

    c1 = params[2]
    c2 = params[3]
    w = params[4]

    Dim = esik
    Fonk = fitnessFonk

    Xmin = np.zeros((Dim), dtype=int) 
    Xmax = np.zeros((Dim), dtype=int) 
    for i in range(Dim):
        Xmin[i] = 0
        Xmax[i] = 255

   
    
    

    x = np.zeros((GN + 1,PN,Dim),dtype=float)
    x_pbest = np.zeros((PN,Dim),dtype=float)
    gbest = np.zeros((Dim),dtype=float)
    x_v = np.zeros((GN + 1,PN, Dim),dtype=float)

    Fitness = np.zeros((GN+1,PN),dtype=float)
    x12Best = np.zeros((GN,Dim),dtype=float)
    FitBest = np.zeros((GN + 1),dtype=float)

    # np.random.rand(FoodNumber,D)
    for i in range(Dim):
        x[0,:,i]  = Xmin[i] + np.random.rand(PN)*(Xmax[i] - Xmin[i])
    x = x.astype(int)
    x.sort(axis = 1)

    x_pbest[:] = x[0,:]

    for i in range(PN): 
        Fitness[0,i] = Fonk(x[0,i,:],hist)

    maxIndex = np.argmax(Fitness[0,:])
    BestFitness = Fitness[0,maxIndex]
    gbest = x[0,maxIndex,:]

    for i in range(GN):
        x.sort(axis = 2)
        PopIndex = np.argmax(Fitness[i,:])
        PopBestFitness = np.max(Fitness[i,:])
        FitBest[i] = PopBestFitness
        x12Best[i] = x[i,PopIndex,:]

        if i == 0:
            for j in range(PN):
                pbestIndex = np.argmax(Fitness[0,j])
                pbest = np.max(Fitness[0,j])
                x_pbest[j,:] = x[pbestIndex,j,:]
        else:
            for j in range(PN):
                pbestIndex = np.argmax(Fitness[0:i,j])
                pbest = np.max(Fitness[0:i,j])
                x_pbest[j,:] = x[pbestIndex,j,:]

        if PopBestFitness > BestFitness:
            BestFitness = PopBestFitness
            gbest = x[i,PopIndex,:]

        for j in range(Dim):
            x_v[i+1,:,j] = w*x_v[i,:,j] + c1 * random.random() * (x_pbest[:,j] - x[i,:,j]) + c2 * random.random() * (gbest[j] - x[i,:,j])

        for j in range(Dim):
            x[i+1,:,j] = x[i,:,j] + x_v[i+1,:,j]
        x = x.astype(int)
        x.sort(axis = 2)
        for j in range(PN):
            for k in range(Dim):
                x[i+1,j,k] = max(min(x[i+1,j,k], Xmax[k]),Xmin[k])
            
        for j in range(PN): 
            Fitness[i] = Fonk(x[i+1,j,:],hist)          
          


    bestFitnessIndex = np.argmax(FitBest)
    return([FitBest[bestFitnessIndex],x12Best[bestFitnessIndex,:]])

   

