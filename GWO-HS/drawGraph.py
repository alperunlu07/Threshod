import json
from Model import Result, Images, Opti, Thresholding, AlgNames, Export, ResultThresh
import matplotlib.pyplot as plt

with open('kapur_result.json', 'r') as f:
    data = json.load(f)
    # data = f.read()
imgName = ["barbara", "couple", "boat", "goldhill", "lake", "aerial"]


def getData(imageIndex, threshold):  # threshold 2, 3, ..., 10
    return data["images"][imageIndex]["results"][threshold - 2]


def getFintnessVal(imageIndex, threshold):
    return getData(imageIndex, threshold)["fitnetVal"]


def getPositionsVal(imageIndex, threshold):
    return getData(imageIndex, threshold)["positions"]


def getGlobalBestVal(imageIndex, threshold):
    return getData(imageIndex, threshold)["bestVals"]


def getTimeVal(imageIndex, threshold):
    return getData(imageIndex, threshold)["timeVal"]


globalBest = getGlobalBestVal(0, 10)
plt.plot(globalBest)
plt.title("globalBest")
plt.savefig("kapur_barbara_globalBest.png")
plt.close()
plt.show()

# print(getData(0, 2))
# print("--------------")
# print(getFintnessVal(0, 2))
# print("--------------")
# print(getPositionsVal(0, 2))
# print("--------------")
# print(getGlobalBestVal(0, 2))
# print("--------------")
# print(getTimeVal(0, 2))
