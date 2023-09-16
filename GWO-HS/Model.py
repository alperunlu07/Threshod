import json


class Images:
    def __init__(self, imageId):
        self.results = []  # results
        self.imageId = imageId

    # def to_json(self):
    #     return json.dumps(self.__dict__)

    # @classmethod
    # def from_json(cls, json_str):
    #     data = json.loads(json_str)
    #     instance = cls(data['imageId'])
    #     instance.__dict__.update(data)
    #     return instance


class ResultThresh:
    def __init__(self):
        self.optiResults = []
        self.alg = ""

        # self.thresh = []


class Opti:
    def __init__(self):
        self.images = []  # results
        self.thresAlgIndex = 0
        # self.algNames = []  # algNames

    # def to_json(self):
    #     return json.dumps(self.__dict__)

    # @classmethod
    # def from_json(cls, json_str):
    #     data = json.loads(json_str)
    #     instance = cls()
    #     instance.__dict__.update(data)
    #     return instance


class Result:
    def __init__(self, bestVals, fitnetVal, positions, timeVal, thres):
        self.fitnetVal = fitnetVal
        self.timeVal = timeVal
        self.positions = positions
        self.bestVals = bestVals
        self.thres = thres

    # def to_json(self):
    #     return json.dumps(self.__dict__)

    # @classmethod
    # def from_json(cls, json_str):
    #     data = json.loads(json_str)
    #     instance = cls(data['bestVals'], data['fitnetVal'],
    #                    data['positions'], data['timeVal'], data['thres'])
    #     return instance


# AlgNames enum'unun Python'daki karşılığı:
class AlgNames:
    Genetic = 'GA'
    Gwolf = 'GWO'
    Harmony = 'HS'
    Hybrit = 'GWO-HS'
    Pso = 'PSO'
    Sa = 'SA'


class Thresholding:
    def __init__(self):
        self.images = []

# Custom JSON encoder to handle custom objects


class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Images):
            return obj.__dict__
        elif isinstance(obj, Opti):
            return obj.__dict__
        elif isinstance(obj, Result):
            return obj.__dict__
        elif isinstance(obj, AlgNames):
            return obj.value  # Serialize AlgNames as its string value
        elif isinstance(obj, Thresholding):
            return obj.__dict__
        return super().default(obj)


class Export:
    def __init__(self):
        self.data = []

    def Write(self, thresholding_data, name):
        output_file = name + ".json"
        with open(output_file, "w") as file:
            json.dump(thresholding_data, file, indent=3, cls=CustomJSONEncoder)
            # json.dump(thresholding_data, file,
            #           indent=3, cls=CustomJSONEncoder)


# result1 = Result(0.95, 10.2, [1.2, 2.3, 3.4, 4.5])
# result2 = Result(0.85, 5.7, [2.5, 4.7, 6.3, 8.1])
# result3 = Result(0.78, 8.9, [3.1, 5.6, 9.2, 7.8])

# opti1 = Opti([result1, result2], AlgNames.Genetic)
# opti2 = Opti([result3], AlgNames.Pso)

# image1 = Images(1, [opti1, opti2])
# image2 = Images(2, [opti2])

# thresholding_data = Thresholding()
# thresholding_data.images = [image1, image2]


# print(thresholding_data)
# JSON dosyasına veriyi kaydetme
# output_file = "veri1.json"
# with open(output_file, "w") as file:
#     json.dump(thresholding_data, file, indent=4, cls=CustomJSONEncoder)
