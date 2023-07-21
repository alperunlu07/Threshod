import numpy as np
import math

def KapurFonk(thx,data):
    
    
    if type(thx) is np.ndarray:
        thx = thx.astype(int)
        thx = list(thx)
    # print(thx)
   
    thx.append(256)
    thx.insert(0, 0)
    
    thx.sort()

    hist = list(data)
    # total_pix = 262144

    # for i in range(len(hist)):                                              
    #     hist[i] = hist[i] / total_pix
    
    cumulative_sum = []    

    for i in range(len(thx)-1):
        for j in range (i + 1,len(thx)):
            if thx[i] == thx[j]:
                # print(thx)
                return 0

    # try:
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
                    val = ( prob)*(np.log(prob)*-1)
            if math.isnan(val):
                val = 0
            total += val
  
  
    return(total)




