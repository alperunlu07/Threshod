import math
import numpy as np
from numpy import matlib as mb
import random
import cv2

import matplotlib.pyplot as plt
import codecs
import json


def init(hist, fitnessFonk, params=[100, 100, 2], esik=3, name=""):

    GN = params[0]
    PN = params[1]
    a = params[2]
    bestVals = []
    hist = hist
    Inf = math.inf
    Dim = esik

    Xmin = np.zeros((Dim), dtype=int)
    Xmax = np.zeros((Dim), dtype=int)
    for i in range(Dim):
        Xmin[i] = 0
        Xmax[i] = 255

    Fitness = np.zeros((PN), dtype=float)
    Positions = np.zeros((PN, Dim), dtype=float)

    Pi = np.zeros((Dim), dtype=float)

    alphaFitness = math.inf
    alphaPosition = np.zeros((Dim), dtype=float)
    betaFitness = math.inf
    betaPosition = np.zeros((Dim), dtype=float)
    deltaFitness = math.inf
    deltaPosition = np.zeros((Dim), dtype=float)

    newFitness = np.zeros((PN), dtype=float)
    newPositions = np.zeros((PN, Dim), dtype=float)

    bestPositions = np.zeros((GN, Dim), dtype=float)
    bestFitness = np.zeros((GN), dtype=float)

    # np.random.rand(FoodNumber,D)
    for i in range(Dim):
        Positions[:, i] = Xmin[i] + np.random.rand(PN)*(Xmax[i] - Xmin[i])
    # Positions[:,1] = Xmin[1] + np.random.rand(1, PN)*(Xmax[1] - Xmin[1])
    Positions = Positions.astype(int)
    Positions.sort(axis=1)

    for i in range(PN):
        Fitness[i] = fitnessFonk(Positions[i, :], hist)
        # Fitness[i] = (4 -2.1 * pow(Positions[i,0],2) + pow(Positions[i,0],4) * (1/3)) * pow(Positions[i,0],2) + Positions[i,0] * Positions[i,1] + (-4+4*pow(Positions[i,1],2))*pow(Positions[i,1],2)

    stepEnd = 2
    stepStart = 10
    stepSize = stepStart
    frac = (stepEnd/stepStart)**(1.0/(GN-1.0))

    minFitnessIndex = np.argmax(Fitness)
    alphaFitness = Fitness[minFitnessIndex]
    alphaPosition = Positions[minFitnessIndex, :]
    Fitness[minFitnessIndex] = -1
    aIndex = minFitnessIndex
    minFitnessIndex = np.argmax(Fitness)
    betaFitness = Fitness[minFitnessIndex]
    betaPosition = Positions[minFitnessIndex, :]
    Fitness[minFitnessIndex] = -1
    bIndex = minFitnessIndex
    minFitnessIndex = np.argmax(Fitness)
    deltaFitness = Fitness[minFitnessIndex]
    deltaPosition = Positions[minFitnessIndex, :]
    dIndex = minFitnessIndex
    Fitness[minFitnessIndex] = -1

    bestVals.append(alphaFitness)
    for i in range(10):
        # Alpha
        for k in range(Dim):
            # xc[k] + random.random() #- 0.5
            Pi[k] = round(alphaPosition[k] + stepSize *
                          (random.random() - 0.5))
            Pi[k] = max(min(Pi[k], Xmax[k]), Xmin[k])

        fxi1 = fitnessFonk(Pi, hist)
        if (alphaFitness < fxi1):
            alphaFitness = fxi1
            alphaPosition = Pi
            Positions[aIndex, :] = Pi
            Fitness[aIndex] = fxi1
        # Beta
        for k in range(Dim):
            # xc[k] + random.random() #- 0.5
            Pi[k] = round(betaPosition[k] + stepSize * (random.random() - 0.5))
            Pi[k] = max(min(Pi[k], Xmax[k]), Xmin[k])

        fxi1 = fitnessFonk(Pi, hist)
        if (betaFitness < fxi1):
            betaFitness = fxi1
            betaPosition = Pi
            Positions[bIndex, :] = Pi
            Fitness[bIndex] = fxi1
        # Delta
        for k in range(Dim):
            # xc[k] + random.random() #- 0.5
            Pi[k] = round(deltaPosition[k] + stepSize *
                          (random.random() - 0.5))
            Pi[k] = max(min(Pi[k], Xmax[k]), Xmin[k])

        fxi1 = fitnessFonk(Pi, hist)
        if (deltaFitness < fxi1):
            deltaFitness = fxi1
            deltaPosition = Pi
            Positions[dIndex, :] = Pi
            Fitness[dIndex] = fxi1

    t = 0
    while t < GN:
        for i in range(PN):
            for j in range(Dim):
                r1 = random.random()
                r2 = random.random()
                A1 = 2 * a * r1 - a
                C1 = 2 * r2
                alphaD = abs(C1 * alphaPosition[j] - Positions[i, j])
                X1 = alphaPosition[j] - A1 * alphaD

                r1 = random.random()
                r2 = random.random()
                A2 = 2 * a * r1 - a
                C2 = 2 * r2
                betaD = abs(C2 * betaPosition[j] - Positions[i, j])
                X2 = betaPosition[j] - A2 * betaD

                r1 = random.random()
                r2 = random.random()
                A3 = 2 * a * r1 - a
                C3 = 2 * r2
                deltaD = abs(C1 * deltaPosition[j] - Positions[i, j])
                X3 = deltaPosition[j] - A3 * alphaD

                # round
                newPositions[i, j] = int((X1 + X2 + X3) / 3)

        newPositions.sort(axis=1)

        a = 2 - t * ((2)/GN)
        for i in range(PN):
            for j in range(Dim):
                newPositions[i, j] = int(
                    max(min(newPositions[i, j], Xmax[j]), Xmin[j]))
            # Positions[i,1] = max(min(Positions[i,1], Xmax[1]),Xmin[1])

        for i in range(PN):
            newFitness[i] = fitnessFonk(Positions[i, :], hist)
            # Fitness[i] = (4 -2.1 * pow(Positions[i,0],2) + pow(Positions[i,0],4) * (1/3)) * pow(Positions[i,0],2) + Positions[i,0] * Positions[i,1] + (-4+4*pow(Positions[i,1],2))*pow(Positions[i,1],2)

        Fitness = np.concatenate([Fitness, newFitness])
        Positions = np.concatenate([Positions, newPositions])

        # kucukten buyuge sýralý tese cevir
        sortIndex = np.argsort(-1*Fitness)[:PN]
        Positions = Positions[sortIndex, :]

        Fitness = Fitness[sortIndex]

        Positions = Positions[0:PN, :]
        Fitness = Fitness[0:PN]

        minFitnessIndex = np.argmax(Fitness)
        alphaFitness = Fitness[minFitnessIndex]
        alphaPosition = Positions[minFitnessIndex, :]
        Fitness[minFitnessIndex] = -1
        aIndex = minFitnessIndex

        minFitnessIndex = np.argmax(Fitness)
        betaFitness = Fitness[minFitnessIndex]
        betaPosition = Positions[minFitnessIndex, :]
        Fitness[minFitnessIndex] = -1
        bIndex = minFitnessIndex

        minFitnessIndex = np.argmax(Fitness)
        deltaFitness = Fitness[minFitnessIndex]
        deltaPosition = Positions[minFitnessIndex, :]
        Fitness[minFitnessIndex] = -1
        dIndex = minFitnessIndex

        for i in range(10):
            # Alpha
            for k in range(Dim):
                # xc[k] + random.random() #- 0.5
                Pi[k] = round(alphaPosition[k] + stepSize *
                              (random.random() - 0.5))
                Pi[k] = max(min(Pi[k], Xmax[k]), Xmin[k])

            fxi1 = fitnessFonk(Pi, hist)
            if (alphaFitness < fxi1):
                alphaFitness = fxi1
                alphaPosition = Pi
                Positions[aIndex, :] = Pi
                Fitness[aIndex] = fxi1
            # Beta
            for k in range(Dim):
                # xc[k] + random.random() #- 0.5
                Pi[k] = round(betaPosition[k] + stepSize *
                              (random.random() - 0.5))
                Pi[k] = max(min(Pi[k], Xmax[k]), Xmin[k])

            fxi1 = fitnessFonk(Pi, hist)
            if (betaFitness < fxi1):
                betaFitness = fxi1
                betaPosition = Pi
                Positions[bIndex, :] = Pi
                Fitness[bIndex] = fxi1
            # Delta
            for k in range(Dim):
                # xc[k] + random.random() #- 0.5
                Pi[k] = round(deltaPosition[k] + stepSize *
                              (random.random() - 0.5))
                Pi[k] = max(min(Pi[k], Xmax[k]), Xmin[k])

            fxi1 = fitnessFonk(Pi, hist)
            if (deltaFitness < fxi1):
                deltaFitness = fxi1
                deltaPosition = Pi
                Positions[dIndex, :] = Pi
                Fitness[dIndex] = fxi1

        stepSize = frac * stepSize

        bestPositions[t, :] = alphaPosition
        bestFitness[t] = alphaFitness
        if (bestVals[len(bestVals) - 1] < alphaFitness):
            bestVals.append(alphaFitness)
        t = t + 1

    # bestFitnessIndex = np.argmax(bestFitness)
    # print(bestVals)
    bestFitness_ = bestFitness.tolist()
    bestPositions_ = bestPositions.tolist()
    return [bestVals, bestFitness_, bestPositions_]
    # plt.plot(bestVals)
    # plt.title(name)
    # # plt.show()
    # plt.savefig(name)
    # plt.close()


# imgName = ["barbara", "couple", "boat", "goldhill", "lake", "aerial"]
# imIndex = 0
# img = cv2.imread(imgName[imIndex] + ".png", 0)
# [hist, _] = np.histogram(img, bins=256, range=(0, 255))

# hist = list(hist)
# total_pix = img.size
# for ix in range(len(hist)):
#     hist[ix] = hist[ix] / total_pix

# # thresAlgorithm = otsu.OtsuFonk
# thresAlgorithm = kapur.KapurFonk
# for i in range(2, 11):
#     init(hist, thresAlgorithm, esik=i, name="kapur" + "_" +
#          imgName[imIndex] + "_" + str(i))
#     print(i)
