import numpy as np
import math

def KapurFonk(thx,data):
    thx = sorted(thx)
    thx = [int(x) for x in thx]
    cdf = data.astype(np.float).cumsum()
        # find histogram's nonzero area
    # valid_idx = np.nonzero(data)[0]
    # first_bin = valid_idx[0]
    # last_bin = valid_idx[-1]
    # max_ent, threshold = 0, 0
    
    thsize = len(thx)

    for i in range(thsize ):

        # 3 durum var 1. ilk threshol 
        if(i==0):
            hist_range = data[:thx[i] + 1]
            hist_range = hist_range[hist_range != 0] / cdf[thx[i]] 
            tot_ent =  -np.sum(hist_range * np.log(hist_range))  

            hist_range = data[thx[i] + 1:thx[i+1]]
            hist_range = hist_range[hist_range != 0] / (cdf[thx[i+1]] - cdf[thx[i]])
            tot_ent -= np.sum(hist_range * np.log(hist_range))  


        elif((i) == (thsize - 1)): # son thrershold
            hist_range = data[thx[i] + 1:256]
            hist_range = hist_range[hist_range != 0] / (cdf[255] - cdf[thx[i]])
            tot_ent -= np.sum(hist_range * np.log(hist_range)) 

        else: # ortadaki thresholdlar 
            hist_range = data[thx[i] + 1:thx[i+1]]
            hist_range = hist_range[hist_range != 0] / (cdf[thx[i+1]] - cdf[thx[i]])
            tot_ent -= np.sum(hist_range * np.log(hist_range))  


    
    return tot_ent
