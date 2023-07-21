import numpy as np
import math

def TsallisFonk(thx,data):

    if type(thx) is np.ndarray:
        thx = thx.astype(int)
        thx = list(thx)
    # print(thx)
   
    q = 4
    thx.sort()

    hist = list(data)
    # total_pix = 262144

    # for i in range(len(hist)):                                              
    #     hist[i] = hist[i] / total_pix
    
    cumulative_sum = []                                                     # declaractions
    sA = []
    # print(sum(hist))
    sum2 = np.zeros(len(thx)+1,dtype=float)
    total = 0
    
    for i in range(len(thx)-1):
        for j in range (i + 1,len(thx)):
            if thx[i] == thx[j]:
                # print(thx)
                return 0

    nd = len(thx)
    p1 = sum(hist[0:thx[0]])
    if p1<=0 or p1>=1:
        # print("0" + str(thx))
        return 0
    
    n1 = np.power((hist/p1),q)
    
    sum1 = sum(n1[0:thx[0]])
    
    sum2[0] = (1-sum1)/(q-1)
    
    for i in range(1,nd):
        p2 = sum(hist[thx[i-1]:thx[i]])
        if p2<=0 or p2>=1:
            return 0
        n2 = np.power((hist/p2),q)
        sum1 =sum(n2[thx[i-1]:thx[i]])
        sum2[i] = (1-sum1)/(q-1)
       
    pe = sum(hist[thx[nd-1]:256]) 
    if pe<=0 or pe>=1:
        return 0   
    ne = np.power((hist/pe),q)    
    sum1 = sum(ne[thx[nd-1]:256])    
    sum2[i+1] = (1-sum1)/(q-1)

    

    sumFinal = sum(sum2)
    prodFinal = np.prod(sum2)    
    sumprofinal=sumFinal+(1-q)*prodFinal
    return sumprofinal

        # for i in range(len(cumulative_sum)):
        # if cumulative_sum[i] <= 0 or cumulative_sum[i] >= 1:
        #     return 0
  



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