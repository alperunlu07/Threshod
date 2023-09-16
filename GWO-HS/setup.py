import numpy as np
import cv2
# import matplotlib.pyplot as plt
import csv
import time
import timeit

import kapur
import otsu

import os
import sys
import gwohs


from Model import Result, Images, Opti, Thresholding, AlgNames, Export, ResultThresh

if __name__ == "__main__":

    imgName = ["barbara", "couple", "boat", "goldhill", "lake", "aerial"]
    optAlgList = ["genetic", "gwolf", "harmoni", "hibrit", "pso", "sa"]
    # sys.argv[1] = "kapur"
    # sys.argv[2] = "1"

    thresAlgName = "otsu"  # sys.argv[1]
    if thresAlgName == "kapur":
        thresAlgorithm = kapur.KapurFonk  # kapur
    if thresAlgName == "otsu":
        thresAlgorithm = otsu.OtsuFonk  # kapur
    # print(sys.argv)
    # imIndex = 0  # int(sys.argv[2])

    alg_ = []

    opt = Opti()
    opt.thresAlgIndex = 0
    for imIndex in range(0, 6):  # 6

        print(imgName[imIndex])

        img = cv2.imread("images/" + imgName[imIndex] + ".png", 0)
        [hist, _] = np.histogram(img, bins=256, range=(0, 255))

        hist = list(hist)
        total_pix = img.size
        for ix in range(len(hist)):
            hist[ix] = hist[ix] / total_pix

        resThresh = ResultThresh()
        imgs = Images(imIndex)
        for i in range(2, 11):  # 11
            # arr_ = []

            # for j in range(2):
            result = 0
            start = timeit.default_timer()
            # [bestVals, bestFitness, bestPositions]
            result = gwohs.init(hist, thresAlgorithm, esik=i)

            stop = timeit.default_timer()

            result_ = Result(result[0], result[1], result[2], stop - start, i)
            # opti.results.append(result_)
            # print(result)
            # print(result_)

            # opti.thres = i
            # print(i)
            # resThresh.optiResults.append(opti)
            # alg_.append(arr_)
            imgs.results.append(result_)
        opt.images.append(imgs)
        # print(resThresh)
        # resThresh.alg = optAlgList[3]
        # writeCSV(imIndex, alg_, algName, thresAlgName)
        # alg_ = []

    Export().Write(opt, thresAlgName+"_result")
