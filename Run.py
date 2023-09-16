import numpy as np
import cv2
# import matplotlib.pyplot as plt
import csv
import time
import timeit

import fitness.otsu as otsu
import fitness.kapur as kapur
import fitness.tsallis as tsallis
import fitness.tsallis2 as tsallis2
import optimisation.genetic as genetic
import optimisation.clonalg as clonalg
import optimisation.difEvol as difEvol
import optimisation.pso as pso
import optimisation.anneal as anneal
import optimisation.abc as abc
import optimisation.gwolf as gwolf
import optimisation.firebee as firebee
import optimisation.harmoni as harmoni
import optimisation.harmoniV2 as harmoniV2

import optimisation.gwolfV2 as gwolf2
import optimisation.gwolfV3 as gwolf3
import optimisation.gwolfV4 as gwolf4

import optimisation.psoV2 as psoV2
import os
import sys


from Model import Result, Images, Opti, Thresholding, AlgNames, Export, ResultThresh

# result1 = Result(0.95, 10.2, [1.2, 2.3, 3.4, 4.5])
# result2 = Result(0.85, 5.7, [2.5, 4.7, 6.3, 8.1])
# result3 = Result(0.78, 8.9, [3.1, 5.6, 9.2, 7.8])

# opti1 = Opti([result1, result2], AlgNames.Genetic)
# opti2 = Opti([result3], AlgNames.Pso)

# image1 = Images(1, [opti1, opti2])
# image2 = Images(2, [opti2])

# thresholding_data = Thresholding()
# thresholding_data.images = [image1, image2]

# ex_ = Export()
# ex_.Write(thresholding_data)

# ex.
if __name__ == "__main__":

    imgName = ["barbara", "couple", "boat", "goldhill", "lake", "aerial"]
    optAlgList = ["genetic", "gwolf", "harmoni", "hibrit", "pso", "sa"]
    # sys.argv[1] = "kapur"
    # sys.argv[2] = "1"

    thresAlgName = "kapur"  # sys.argv[1]
    if thresAlgName == "kapur":
        thresAlgorithm = kapur.KapurFonk  # kapur
    if thresAlgName == "otsu":
        thresAlgorithm = otsu.OtsuFonk  # kapur
    # print(sys.argv)
    imIndex = 0  # int(sys.argv[2])

    print(imgName[imIndex])

    img = cv2.imread(imgName[imIndex] + ".png", 0)
    [hist, _] = np.histogram(img, bins=256, range=(0, 255))

    hist = list(hist)
    total_pix = img.size
    for ix in range(len(hist)):
        hist[ix] = hist[ix] / total_pix

    alg_ = []
    for algName in range(3, 4):
        resThresh = ResultThresh()
        for i in range(2, 11):
            # arr_ = []
            opti = Opti()
            for j in range(2):
                result = 0
                start = timeit.default_timer()
                if (algName == 0):
                    result = genetic.init(hist, thresAlgorithm, esik=i)[0]
                elif (algName == 1):
                    result = gwolf.init(hist, thresAlgorithm, esik=i)[0]
                elif (algName == 2):
                    result = harmoni.init(hist, thresAlgorithm, esik=i)[0]
                elif (algName == 3):
                    result = gwolf4.init(hist, thresAlgorithm, esik=i)
                elif (algName == 4):
                    result = pso.init(hist, thresAlgorithm, esik=i)[0]
                elif (algName == 5):
                    result = anneal.init(hist, thresAlgorithm, esik=i)[0]
                stop = timeit.default_timer()

                result_ = Result(result[0], stop - start, result[1])
                opti.results.append(result_)

                # arr_.append(result)
            #
            opti.thres = i
            # print(i)
            resThresh.optiResults.append(opti)
            # alg_.append(arr_)
        print(resThresh)
        resThresh.alg = optAlgList[3]
        # writeCSV(imIndex, alg_, algName, thresAlgName)
        # alg_ = []
        Export().Write(resThresh)
