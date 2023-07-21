import numpy as np
import math

def OtsuFonk(thx, hist):

    thx = np.around(thx)
    thx = thx.astype(int)
    thx = np.sort(thx)
    for i in range(len(thx)-1):
        if thx[i] == thx[i+1]:
            thx[i] -= 1

    if(max(thx) > 254):
        thx[np.argmax(thx)] = 254
    if(min(thx) < 1):
        thx[np.argmin(thx)] = 1
    
    
    thsize = len(thx)
    wx = np.zeros(thsize + 1)
    mx = np.zeros(thsize + 1)
    sx = np.zeros(thsize + 1)
    # q1 = np.zeros(thsize)

    th = np.zeros(1,dtype=int)
    th = np.concatenate([th,thx])
    thz = np.zeros(1,dtype=int)
    thz[0] = 255
    th = np.concatenate([th,thz])
    i = 0
    px = np.arange(256)
    pi = hist * px
    pt = sum(pi)
    # print(pt)
   
    # aax = np.matmul(hist,px)
    # print(np.dot(hist,px))
    # matmul
    # print(hist[:] * px[:] )
    # print(th)
    for i in range(thsize+ 1):
        
        wx[i] = np.sum(hist[th[i]:th[i+1]])
        if wx[i] == 0:
            mx[i] = 0
        else:
            mx[i] = (1/wx[i]) * (np.sum(pi[th[i]:th[i+1]]))
        sx[i] = wx[i] * pow((mx[i] - pt),2)  
   
   
    return (sum(sx))

def OtsuFonk2(thx, hist):
    #thx = [thi, thj]

    #thx = [82, 147]
    thsize = len(thx)
    #print("--------->"+str(thx))
    wx = np.zeros(thsize + 1)
    mx = np.zeros(thsize + 1)
    # q1 = np.zeros(thsize)
    mt = 0
    maxfitness = 0
    maxiter = []
    thy=0

    ix = 0
    for i in range(thsize + 1):
        if(i==0):
            for j in range(int(thx[0])):
                wx[i] += hist[j]
                mx[i] += j * hist[j]        
        elif((i) == thsize):
            for j in range(thy,256):
                wx[i] += hist[j]
                mx[i] += j * hist[j]
        else:
            for j in range(thy,int(thx[i])):
                wx[i] += hist[j]
                mx[i] += j * hist[j]
        mx[i] = mx[i] / wx[i]
        if (i < thsize): thy = int(thx[i])
            
        mt = mt + wx[i]*mx[i]
        
    fitnes = 0
    for i in range(thsize + 1):
        fitnes = fitnes + wx[i]*(np.power(mx[i]-mt,2))
    # if(fitnes > maxfitness):
    #     maxfitness = fitnes
    #     maxiter = thx;
        # print(maxfitness)
        # print(maxiter)
    if(math.isnan(fitnes)): 
        fitnes=0
    return fitnes 
