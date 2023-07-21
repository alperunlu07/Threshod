import math 
import numpy as np 
from numpy import matlib as mb
import random


def init(hist, fitnessFonk, params = [100, 100, 4], esik = 3):  

    GN = params[0]
    PN = params[1]
    hist = hist
    Limit = params[2]

    FoodNumber = int(PN / 2)
    D = esik
    Xmin = np.zeros((D), dtype=int) 
    Xmax = np.zeros((D), dtype=int) 
    for i in range(D):
        Xmin[i] = 0
        Xmax[i] = 255
  
  

    Foods = np.zeros((FoodNumber,2),dtype=int)
    # aa = Xmax-Xmin

    Range = mb.repmat(Xmax-Xmin,FoodNumber,1)
    Lower = mb.repmat(Xmin,FoodNumber,1)
    Foods = np.random.rand(FoodNumber,D) * Range +  Lower
    Foods = Foods.astype(int)
    Foods.sort(axis = 1)
    Fitness = np.zeros((FoodNumber),dtype=float)
    FitBest = np.zeros((GN),dtype=float)
    x12Best = np.zeros((GN,D),dtype=float)
    # print(Foods)clea
    for i in range(FoodNumber): 
        Fitness[i] = fitnessFonk(Foods[i,:],hist)
        # Fitness[i] = (4 -2.1 * pow(Foods[i,0],2) + pow(Foods[i,0],4) * (1/3)) * pow(Foods[i,0],2) + Foods[i,0] * Foods[i,1] + (-4+4*pow(Foods[i,1],2))*pow(Foods[i,1],2)

    Trial = np.zeros((GN),dtype=float)
    BestInd = np.argmin(Fitness)
    GloabalMin = Fitness[BestInd]
    GlobalParams = Foods[BestInd,:]
    Iterasyon = 0
    while(Iterasyon<GN):
        for i in range(FoodNumber):
            Param2Change = math.floor(random.random() * D) 
            neighbour = math.floor(random.random() * FoodNumber)
            while neighbour == i:
                neighbour = math.floor(random.random() * FoodNumber)

            sol = Foods[i,:]
            sol.sort()
            sol = sol.astype(int)
            sol[Param2Change] = Foods[i,Param2Change] + (Foods[i,Param2Change] - Foods[neighbour,Param2Change] ) * (random.random() - 0.5) * 2
            for j in range(D):
                sol[j] = max(min(sol[j],Xmax[j]),Xmin[j])
            # sol[0] = max(min(sol[0],Xmax[0]),Xmin[0])
            # sol[1] = max(min(sol[1],Xmax[1]),Xmin[1])


            # FitnessSol = (4 -2.1 * pow(sol[0],2) + pow(sol[0],4)*(1/3)) * pow(sol[0],2) + sol[0] * sol[1] + (-4+4*pow(sol[1],2))*pow(sol[1],2)
            FitnessSol = fitnessFonk(sol,hist)

            #min
            if FitnessSol > Fitness[i]:
                Foods[i,:] = sol
                Fitness[i] = FitnessSol
                Trial[i] = 0
            else:
                Trial[i] = Trial[i] + 1
                

        #Olasılık Hesabı 
        probFitness = Fitness + abs(min(Fitness))
        prob = 1 - (probFitness/max(probFitness))
        # GÖZCÜ ARI FAZI##########################
        i = 0 
        t = 0

        while(t<FoodNumber):
            if random.random() < prob[i]:
                t += 1
                Param2Change = math.floor(random.random() * D) 
                neighbour = math.floor(random.random() * FoodNumber)
                while neighbour == i:
                    neighbour = math.floor(random.random() * FoodNumber)

                sol = Foods[i,:]
                # sol = sorted(sol) 
                sol = sol.astype(int)
                sol[Param2Change] = Foods[i,Param2Change] + (Foods[i,Param2Change] - Foods[neighbour,Param2Change] ) * (random.random() - 0.5) * 2
                # sol[0] = max(min(sol[0],Xmax[0]),Xmin[0])
                # sol[1] = max(min(sol[1],Xmax[1]),Xmin[1])

                for j in range(D):
                    sol[j] = max(min(sol[j],Xmax[j]),Xmin[j])
                # FitnessSol = (4 -2.1 * pow(sol[0],2) + pow(sol[0],4)*(1/3)) * pow(sol[0],2) + sol[0] * sol[1] + (-4+4*pow(sol[1],2))*pow(sol[1],2)

                FitnessSol = fitnessFonk(sol,hist)
                #min
                if FitnessSol > Fitness[i]:
                    Foods[i,:] = sol
                    Fitness[i] = FitnessSol
                    Trial[i] = 0
                else:
                    Trial[i] = Trial[i] + 1


            i += 1
            if i == FoodNumber:
                i = 1


        # ind = np.argmin(Fitness)
        ind = np.argmax(Fitness)
        #min
        if Fitness[ind] > GloabalMin:
            GloabalMin = Fitness[ind]
            GlobalParams = Foods[ind,:]

        #KAŞİF ARI FAZI############################################################

        ind = np.argmax(Trial)
        if Trial[ind] > Limit:
            Trial[ind] = 0
            sol = (Xmax - Xmin) * np.random.rand(1,D) + Xmin
            sol.sort()
            sol = sol.astype(int)
            FitnessSol = fitnessFonk(sol[0],hist)
            # FitnessSol = (4 -2.1 * pow(sol[0,0],2) + pow(sol[0,0],4)*(1/3)) * pow(sol[0,0],2) + sol[0,0] * sol[0,1] + (-4+4*pow(sol[0,1],2))*pow(sol[0,1],2)

            Foods[ind,:] = sol[0]
            Fitness[ind] = FitnessSol

        FitBest[Iterasyon] = GloabalMin
        x12Best[Iterasyon,:] = GlobalParams[:]
        Iterasyon += 1

    IterIndex = np.argmin(FitBest)
    return[FitBest[IterIndex],x12Best[IterIndex]]
