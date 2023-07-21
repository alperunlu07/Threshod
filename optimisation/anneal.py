import numpy as np
import random
import math

def init(hist, fitnessFonk, params = [100,100,10,2], esik = 3):      

    # na = 0.0, p1 = 0.7
    
    # x_start = x_start


    # Number of cycles
    GN = params[0]
    # Number of trials per cycle
    PN = params[1]
    # Number of accepted solutions
    tStart = params[2]
    # Probability of accepting worse solution at the start
    tEnd = params[3]

    frac = (tEnd/tStart)**(1.0/(GN-1.0))

    # Initialize x
    esik = esik
    bound = [0,250]

    x_start = np.random.rand(esik) * 255 
    x_start = x_start.astype(int)
    x_start.sort()

    x = np.zeros((GN+1,esik))
    x[0] = x_start
    xi = np.zeros(esik)
    xi = x_start

    # na = na + 1.0
    # Current best results so far
    xc = np.zeros(esik)
    xc = x[0,:]

    fc = fitnessFonk(xi,hist)

    fs = np.zeros(GN+1)
    fs[0] = fc
    # Current temperature
    t = tStart


    for i in range(GN):
        # print('Cycle: ' + str(i) + ' with Temperature: ' + str(t))
        for j in range(PN):
            # Generate new trial points
            for k in range(esik):
                xi[k] = round(xc[k] + random.randint(0,10) - 5) #xc[k] + random.random() #- 0.5
                xi[k] = max(min(xi[k],bound[1]),bound[0])
            
            xi.sort()
            fxi1 = fitnessFonk(xi,hist)
            DeltaE = fxi1-fc
            if (DeltaE > 0):
                #good
                accept = True
            else:
                #bad
               
                try:
                    w = math.exp(-DeltaE/t)
                    # ans = math.exp(200000)
                except OverflowError:
                    w = float('inf')

                # w = math.exp(dd)
                if (random.random()<w):
                    # accept the worse solution
                    accept = True
                else:
                    # don't accept the worse solution
                    accept = False


            if (accept==True):
                # update currently accepted solution

                for k in range(esik):
                    xc[k] = xi[k]
                
                fc = fxi1

        for k in range(esik):
            x[i+1][k] = xc[k]
        # x[i+1][1] = xc[1]
        # x[i+1][2] = xc[2]
        fs[i+1] = fc
        
        t = frac * t
    index_ = np.argmax(fs)
    return [fs[index_],x[index_]]

