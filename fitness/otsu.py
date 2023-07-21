import numpy as np
import math

def OtsuFonk(thx, hist_,total_pix=262144):

    if type(thx) is np.ndarray:
        thx = thx.astype(int)
        thx = list(thx)
    # print(thx)
   
    thx.append(256)
    thx.insert(0, 0)
    
    thx.sort()

    hist = list(hist_)
    # hist = hist_[:]
    # for i in range(len(hist)):                                              
    #     hist[i] = hist[i] / total_pix
    
    cumulative_sum = []                                                     # declaractions
    cumulative_mean = []
    global_mean = 0
    Sigma = 0
    
    for i in range(len(thx)-1):
        for j in range (i + 1,len(thx)):
            if thx[i] == thx[j]:
                # print(thx)
                return -1

    try:
        for i in range(len(thx)-1):
            cumulative_sum.append(sum(hist[thx[i]:thx[i + 1]]))   # Cumulative sum of each Class

            cumulative = 0
            for j in range(thx[i], thx[i + 1]):
                cumulative = cumulative + (j + 1) * hist[j]
            
            if cumulative_sum[-1] == 0:
                cumulative_sum[-1] = math.inf

            cumulative_mean.append(cumulative / cumulative_sum[-1])             # Cumulative mean of each Class

            global_mean = global_mean + cumulative                              # Global Intensity Mean

        for i in range(len(cumulative_mean)):                                   # Computing Sigma
            Sigma = Sigma + (cumulative_sum[i] * ((cumulative_mean[i] - global_mean) ** 2))
        
        if math.isnan(Sigma) or math.isinf(Sigma):
            return -1
        return(Sigma)
    except:
        # print(thx)
        return -1


