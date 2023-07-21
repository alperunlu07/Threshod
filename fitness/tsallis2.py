import numpy as np
import math

def TsallisFonk(thx,data):
    data = np.asarray(data)
    thx = sorted(thx)
    thx = [int(a) for a in thx]
    cdf = data.astype(np.float).cumsum()
    # find histogram's nonzero area
    valid_idx = np.nonzero(data)[0]
    first_bin = valid_idx[0]
    last_bin = valid_idx[-1]
    max_ent, threshold = 0, 0
    sa = 0.0
    sb = 0.0
    sc = 0.0
    thsize = len(thx)
    q = 4
    
    for i in range(thsize):

        # 3 durum var 1. ilk threshold 
        if(i==0):
            hist_range = data[:thx[i] + 1]
            hist_range = hist_range[hist_range != 0] / cdf[thx[i]] 
            sa =  np.sum(np.power(hist_range,q))
            
        else: # ortadaki thresholdlar 
            hist_range = data[thx[i -1] + 1:thx[i]]
            hist_range = hist_range[hist_range != 0] / (cdf[thx[i]] - cdf[thx[i - 1]])
            sb +=  np.sum(np.power(hist_range,q))  

    hist_range = data[thx[i] + 1:255]
    hist_range = hist_range[hist_range != 0] / (cdf[255] - cdf[thx[i]])
    sc +=  np.sum(np.power(hist_range,q)) 

    sa = (1-sa)/(q-1)
    sb = (1-sb)/(q-1)
    sc = (1-sc)/(q-1)
    tot_ent = sa + sb + sc + (1 - q) * sa * sb * sc
    
    return tot_ent