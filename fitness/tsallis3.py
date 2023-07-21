import numpy as np
import math

def TsallisFonk(thx,data):

    if type(thx) is np.ndarray:
        thx = thx.astype(int)
        thx = list(thx)
    # print(thx)
   
    thx.append(255)
    thx.insert(0, 0)
    q = 4
    thx.sort()

    hist = list(data)
    total_pix = 262144

    for i in range(len(hist)):                                              
        hist[i] = hist[i] / total_pix
    
    cumulative_sum = []                                                     # declaractions
    sA = []
    # print(sum(hist))
 
    total = 0
    
    for i in range(len(thx)-1):
        for j in range (i + 1,len(thx)):
            if thx[i] == thx[j]:
                # print(thx)
                return 0

    # cumulative = 0
    for i in range(len(thx)-1):
        cumulative_sum.append(sum(hist[thx[i]:thx[i + 1]+1]))   # Cumulative sum of each Class
        total = 0
        for j in range(thx[i], thx[i + 1]):
            val = 0
            prob = 0
            if cumulative_sum[i] != 0:
                
                prob = hist[j] / cumulative_sum[i]
            if prob != 0:
                val = math.pow(prob,q)
            # val = np.power(prob,q)
            # if math.isnan(val):
            #     val = 0
            total += val

        sA.append((1-total)/(q-1))

    # Ss = []
    # for i in range(len(sA) - 1):
    #     vall = sA[i] + sA[i + 1] + (1-q)*sA[i]*sA[i+1]
    #     # Ss.append(val)
    #     minVv = (cumulative_sum[i] + cumulative_sum[i+1]) - 1
    #     maxVv = 1 - (cumulative_sum[i] - cumulative_sum[i+1])
    #     if vall > maxVv or vall < minVv:
    #         return 0
        # if
    for i in range(len(cumulative_sum)):
        if cumulative_sum[i] <= 0 or cumulative_sum[i] >= 1:
            return 0

    top = 0
    carp = 1
    for i in range(len(sA)):
        top += sA[i]
        carp *= sA[i]
    
    totalX = top + (1-q) * carp
    return(totalX)


    # carpim = 1
    # for i in range(len(sA)):
    #     carpim *= sA[i]
    # carpim *= (1-q)
    # total = sum(sA) + carpim

    # return(total)


