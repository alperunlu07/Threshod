import numpy as np
import math

def TsallisFonk(thx,data):

    if type(thx) is np.ndarray:
        thx = thx.astype(int)
        thx = list(thx)
    # print(thx)
   
    thx.append(256)
    thx.insert(0, 0)
    q = 4
    thx.sort()

    hist = list(data)
    total_pix = 262144

    for i in range(len(hist)):                                              
        hist[i] = hist[i] / total_pix
    
    cumulative_sum = []                                                     # declaractions
    sA = []
    # global_mean = 0
    # Sigma = 0

    # q = 0.5

    for i in range(len(thx)-1):
        for j in range (i + 1,len(thx)):
            if thx[i] == thx[j]:
                # print(thx)
                return -100

    # try:
    total = 0
    # cumulative = 0
    # saTotal = 0
    # for i in range(len(thx)-1):
    #     cumulative_sum.append(sum(hist[thx[i]:thx[i + 1]]))   # Cumulative sum of each Class

    #     # val = 0
    #     prob = 0

    #     for j in range(thx[i], thx[i + 1]):
            
    #         if cumulative_sum[i] != 0:
                
    #             prob += np.power((hist[j] / cumulative_sum[i]),q)


    #             # if prob != 0:
    #             #     val = (1 - np.power(prob,q))/(q-1)
    #                 # ( prob)*(np.log(prob)*-1)
    #         # if math.isnan(val):
    #         #     val = 0
    #         # saTotal += val

    #     # print(prob)
    #     sA.append((1 - math.pow(prob,q))/(q-1))
    #         # total += val
    
    # # print(sA)

    # total = sum(sA) + (1 - q) * np.prod(np.array(sA))

    total = 0

    # cumulative = 0
    for i in range(len(thx)-1):
        cumulative_sum.append(sum(hist[thx[i]:thx[i + 1]]))   # Cumulative sum of each Class

        for j in range(thx[i], thx[i + 1]):
            val = 0
            prob = 0
            if cumulative_sum[i] != 0:
                
                prob = hist[j] / cumulative_sum[i]
                if prob != 0:
                    val = math.pow( prob,q)
            if math.isnan(val):
                val = 0
            total += val

        sA.append((1-total)/(q-1))

    top = 0
    carp = 1
    for i in range(len(sA)):
        top += sA[i]
        carp *= sA[i]
    
    total = top + (1-q)*carp
    return(total)


    # carpim = 1
    # for i in range(len(sA)):
    #     carpim *= sA[i]
    # carpim *= (1-q)
    # total = sum(sA) + carpim

    return(total)



    # thx = sorted(thx)
    # thx = [int(a) for a in thx]
    # cdf = data.astype(np.float).cumsum()
    # # find histogram's nonzero area
    # valid_idx = np.nonzero(data)[0]
    # first_bin = valid_idx[0]
    # last_bin = valid_idx[-1]
    # max_ent, threshold = 0, 0
    # sa = 0.0
    # sb = 0.0
    # sc = 0.0
    # thsize = len(thx)
    # q = 0.5
    
    # for i in range(thsize):

    #     # 3 durum var 1. ilk threshold 
    #     if(i==0):
    #         hist_range = data[:thx[i] + 1]
    #         hist_range = hist_range[hist_range != 0] / cdf[thx[i]] 
    #         sa =  np.sum(np.power(hist_range,q))
            
    #     else: # ortadaki thresholdlar 
    #         hist_range = data[thx[i -1] + 1:thx[i]]
    #         hist_range = hist_range[hist_range != 0] / (cdf[thx[i]] - cdf[thx[i - 1]])
    #         sb +=  np.sum(np.power(hist_range,q))  

    # hist_range = data[thx[i] + 1:255]
    # hist_range = hist_range[hist_range != 0] / (cdf[255] - cdf[thx[i]])
    # sc +=  np.sum(np.power(hist_range,q)) 

    # sa = (1-sa)/(q-1)
    # sb = (1-sb)/(q-1)
    # sc = (1-sc)/(q-1)
    # tot_ent = sa + sb + sc + (1 - q) * sa * sb * sc
    
    # return tot_ent