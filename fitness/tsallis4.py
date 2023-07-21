import numpy as np
import math
import cv2

def TsallisFonk(thx,data):

    if type(thx) is np.ndarray:
        thx = thx.astype(int)
        thx = list(thx)
    # print(thx)
   
   
   
    q = 4
    thx.sort()

    hist = list(data)
    total_pix = 262144

    for i in range(len(hist)):                                              
        hist[i] = hist[i] / total_pix
        # print(hist[i])
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
    
    n1 = np.power((hist/p1),q)
    
    sum1 = sum(n1[0:thx[0]])
    
    sum2[0] = (1-sum1)/(q-1)
    
    for i in range(1,nd):
        p2 = sum(hist[thx[i-1]:thx[i]])
        n2 = np.power((hist/p2),q)
        sum1 =sum(n2[thx[i-1]:thx[i]])
        sum2[i] = (1-sum1)/(q-1)

    pe = sum(hist[thx[nd-1]:256])    
    ne = np.power((hist/pe),q)    
    sum1 = sum(ne[thx[nd-1]:256])    
    sum2[i+1] = (1-sum1)/(q-1) 
    sumFinal = sum(sum2)
    prodFinal = np.prod(sum2)    
    sumprofinal=sumFinal+(1-q)*prodFinal
    return sumprofinal
    # # cumulative = 0
    # for i in range(len(thx)-1):
    #     cumulative_sum.append(sum(hist[thx[i]:thx[i + 1]+1]))   # Cumulative sum of each Class
    #     total = 0
    #     for j in range(thx[i], thx[i + 1]):
    #         val = 0
    #         prob = 0
    #         if cumulative_sum[i] != 0:
                
    #             prob = hist[j] / cumulative_sum[i]
    #         if prob != 0:
    #             val = math.pow(prob,q)
    #         # val = np.power(prob,q)
    #         # if math.isnan(val):
    #         #     val = 0
    #         total += val

    #     sA.append((1-total)/(q-1))




img = cv2.imread("./lenaGray.tif",0) 

hist = []
[hist, _] = np.histogram(img, bins=256, range=(0, 256))

hist = [0] * 256               
for i in range(len(img)):
    for j in range(len(img[0])):
        hist[int(img[i][j])] += 1
# 96, 169, 254
# 110,149,187
print(TsallisFonk([99, 100, 167],np.array(hist)))
