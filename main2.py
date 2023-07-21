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


imgName = ["barbara", "couple", "boat", "goldhill", "lake", "aerial"]
optAlgList = ["genetic", "gwolf", "harmoni", "hibrit", "pso", "sa"]
# genetic gwolf harmoni hibrit pso sa
# thresAlg = "Kapur"


def writeCSV(imIndex, fit, algNameIndex, thresAlgName):

    optAlg = optAlgList[algNameIndex]
    path = "Results/" + thresAlgName
    if not os.path.exists(path):
        os.makedirs(path)
    with open(path + "/" + imgName[imIndex] + "-" + optAlg + "-fitnessVal.csv", "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerows(fit)


if __name__ == "__main__":

    thresAlgName = sys.argv[1]
    if thresAlgName == "kapur":
        thresAlgorithm = kapur.KapurFonk  # kapur
    if thresAlgName == "otsu":
        thresAlgorithm = otsu.OtsuFonk  # kapur
    # print(sys.argv)
    imIndex = int(sys.argv[2])

    print(imgName[imIndex])

    img = cv2.imread(imgName[imIndex] + ".png", 0)
    [hist, _] = np.histogram(img, bins=256, range=(0, 255))

    hist = list(hist)
    total_pix = img.size
    for ix in range(len(hist)):
        hist[ix] = hist[ix] / total_pix

    alg_ = []
    for algName in range(4, 6):
        for i in range(2, 11):
            arr_ = []
            for j in range(50):
                result = 0
                if (algName == 0):
                    result = genetic.init(hist, thresAlgorithm, esik=i)[0]
                elif (algName == 1):
                    result = gwolf.init(hist, thresAlgorithm, esik=i)[0]
                elif (algName == 2):
                    result = harmoni.init(hist, thresAlgorithm, esik=i)[0]
                elif (algName == 3):
                    result = gwolf4.init(hist, thresAlgorithm, esik=i)[0]
                elif (algName == 4):
                    result = pso.init(hist, thresAlgorithm, esik=i)[0]
                elif (algName == 5):
                    result = anneal.init(hist, thresAlgorithm, esik=i)[0]

                arr_.append(result)
            #
            alg_.append(arr_)
        print(optAlgList[algName])
        writeCSV(imIndex, alg_, algName, thresAlgName)
        alg_ = []


# print(harmoni.init(hist,kapur.KapurFonk,esik=esikVal))
# print(harmoniV2.init(hist,kapur.KapurFonk,esik=esikVal))
# print(gwolf.init(hist,kapur.KapurFonk,esik=esikVal))
# print(gwolf4.init(hist,kapur.KapurFonk,esik=esikVal))
