import math
import numpy as np
import random
from numpy.random import randint

def rndarray(size):
    ax = []
    for _ in range(size):
        ax.append(round(random.random(),5))
        #print(ax)
    return ax
def InitiatePopulation(Population,Xmin,Xmax):
    for i in range(Population.shape[0]):
        for j in range(Population.shape[1]):
            Population[i, j] = round(Xmin + round(random.random(),5)*(Xmax-Xmin))
        
        Population[i,:] = np.sort(Population[i,:]) #elemanları siraladı 
    #Population[:, 2] = Xmin[2] + rand[1, PN)*(Xmax(2)-Xmin(2));
    return(Population)
def EvaluateFitness(Population,PN,Fitness,hist,fitnessFonk):
    for j in range(PN):     
        Fitness[j] = fitnessFonk(Population[j,:],hist)      
    return Fitness
def Selection(Population,Fitness,PN):
    Probability = Fitness / sum(Fitness)
    Cumulative = np.cumsum(Probability)
    RandomNum = rndarray(PN)
    #print(Cumulative)
    #print(RandomNum)
    #print(np.where(RandomNum < Cumulative[5]))

    for j in range(PN):
        #print("*")
        #print(np.where(RandomNum < Cumulative[j]))
        ind = np.where(RandomNum < Cumulative[j])
        #print(ind[0])
        #print(len(ind[0]))
        if len(ind[0])>0:        
            #print(j*np.ones(len(ind[0])))
            #print(ind[0][0])
            for k in range(len(ind[0])):
                #print("---")
                #print(RandomNum[ind[0][k]])            
                RandomNum[ind[0][k]] = j

    #print(Population)
    RandomNum = [int(i) for i in RandomNum]
    Population = Population[RandomNum,:]
    return Population
def Crossover(Population, PN, CO, ParNumber):
    RandomCNum = rndarray(PN)
    index=[]
    index = [j for j in range(PN)  if RandomCNum[j] < CO] #np.where(RandomCNum < cox[0])
    CONum = len(index)
    while(CONum<math.ceil(PN*CO)):
        index.append(random.randint(0,PN))
        #if index[CONum]==0:
        #    continue
        CONum = len(index)

    while(CONum > math.ceil(PN*CO)):
        index.pop(CONum-1)
        CONum = len(index)

    while CONum % 2 == 1:
        index.append(random.randint(0,PN))
        #if index[CONum]==0:
        #    continue
        CONum = len(index)

    #print(sum(Population))
    #print(CONum)
    for j in range(round(CONum/2)):
        CrossPoint = math.ceil(random.random() * (ParNumber))-1
        Beta = random.random()
        #print(len(index))
        Param1 = Beta * Population[index[2*j], CrossPoint] + (1 - Beta) * Population[index[2*j+1], CrossPoint]
        Param2 = (1 - Beta) * Population[index[2*j], CrossPoint] + Beta * Population[index[2*j+1], CrossPoint]
        #print(Param1)
        Population[index[2*j], CrossPoint] = Param1
        Population[index[2*j+1], CrossPoint] = Param2
    return Population
def Mutation(Population,PN, ParNumber,MO, Xmin, Xmax):
    RandomMNum = rndarray(PN*ParNumber)
    index = [j for j in range(PN)  if RandomMNum[j] < MO]
    MONum = len(index)
    for j in range(MONum):
        Kromozom = math.ceil(index[j]/ParNumber)
        Konum = index[j] % ParNumber
        if Konum == 0:
            Konum = ParNumber - 1
        xcx = Xmin + random.random() * (Xmax-Xmin)  
        
        Population[Kromozom,Konum] = xcx
    return Population

# 0.95,0.25
def init(hist, fitnessFonk, params = [100,100,0.8,0.3], esik = 3):      
    
    
    GN = int(params[0])
    PN = int(params[1])
    CO = int(params[2])
    MO = int(params[3])
    
    Hassasiyet = 3
    esik_say = int(esik)
    
    Xmin = 15
    Xmax = 245
    
    BestFitness = 0
    ParNumber = esik_say
    Population = np.zeros((PN, ParNumber), dtype = int)
    Fitness = np.zeros((PN, 1), dtype = float)  

 
    BestFitnessArray=[]
    SumFitnessArray=[]
    minFitnessArray=[]

    Population = InitiatePopulation(Population, Xmin, Xmax)
    Fitness = EvaluateFitness(Population,PN,Fitness, hist,fitnessFonk)

    minFitness = max(Fitness)[0] # min max
    minIndex = np.where(Fitness==minFitness)
    BestFitness = minFitness
    BestGN=0
    BestPop=Population
    BestIndex=minIndex
    
    for i in range(GN):
        if(minFitness > BestFitness):  # min max
            BestFitness = minFitness
            BestGN = i
            BestPop = Population
            BestIndex = minIndex
            
        Population = Selection(Population,Fitness,PN)
        try:
            Population = Crossover(Population,PN, CO, ParNumber)
        except:
            break
        if(i < GN):
            # try:
            Population = Mutation(Population, PN, ParNumber, MO, Xmin, Xmax )
            # except:
                # print()
            
        Fitness = EvaluateFitness(Population, PN, Fitness, hist, fitnessFonk)
        minFitness = max(Fitness)[0]  # min max
        minIndex = np.where(Fitness==minFitness)
        
        BestFitnessArray.append(BestFitness)
        SumFitnessArray.append(sum(Fitness))
        minFitnessArray.append(minFitness)


    
    
    # print(BestFitness)
    # print(Population[BestGN,:]) 
    return [BestFitness,Population[BestGN,:]]