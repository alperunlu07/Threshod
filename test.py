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


img = cv2.imread("barbaragray.png", 0)
[hist, _] = np.histogram(img, bins=256, range=(0, 255))

hist = list(hist)
total_pix = img.size
for ix in range(len(hist)):
    hist[ix] = hist[ix] / total_pix

imgName = ["barbara", "couple", "boat", "goldhill", "lake", "aerial"]
optAlgList = ["harmoni", "harmoniV2", "gwolf", "gwolfV2"]


thresAlg = "Kapur"


def writeCSV(imIndex, fit):

    # optAlg = optAlgList[algNameIndex]
    path = "bildiriResults/" + thresAlg
    if not os.path.exists(path):
        os.makedirs(path)
    with open(path + "/"+imgName[imIndex] + "-fitnessVal.csv", "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerows(fit)
        # for r1 in fit:
        #     # for r2 in r1:
        #     writer.writerows(r1)

    # with open(path + "/"+imgName[imIndex] + "-esikVal.csv", "w") as file:
    #     writer = csv.writer(file, delimiter=',')
    #     for r1 in thres:
    #         for r2 in r1:

    #             writer.writerow(r2)

    # with open(path + "/"+imgName[imIndex] + "-timeVal.csv", "w") as file:
    #     writer = csv.writer(file, delimiter=',')
    #     for r1 in times:

    #         writer.writerow(r1)

# genetic
# gwolf
# harmoni
# hibrit
# pso
# sa


esikVal = 7
alg_ = []
for algName in range(6):
    for i in range(2, 11):
        arr_ = []
        for j in range(2):
            result = 0
            if (algName == 0):
                result = genetic.init(hist, kapur.KapurFonk, esik=i)[0]
            elif (algName == 1):
                result = gwolf.init(hist, kapur.KapurFonk, esik=i)[0]
            elif (algName == 2):
                result = harmoni.init(hist, kapur.KapurFonk, esik=i)[0]
            elif (algName == 3):
                result = gwolf4.init(hist, kapur.KapurFonk, esik=i)[0]
            elif (algName == 4):
                result = pso.init(hist, kapur.KapurFonk, esik=i)[0]
            elif (algName == 5):
                result = anneal.init(hist, kapur.KapurFonk, esik=i)[0]

            arr_.append(result)
        #
        alg_.append(arr_)
    print(algName)
writeCSV(0, alg_)


# print(harmoni.init(hist,kapur.KapurFonk,esik=esikVal))
# print(harmoniV2.init(hist,kapur.KapurFonk,esik=esikVal))
# print(gwolf.init(hist,kapur.KapurFonk,esik=esikVal))
# print(gwolf4.init(hist,kapur.KapurFonk,esik=esikVal))
