from bisect import bisect
import json

class ScoreMap:

    def __init__(self):
        self.rangeMap = {}
        self.rangeMap[Range(601, 1200)] = 0
        self.rangeMap[Range(501-600)] = 0
        self.rangeMap[Range(491,500)] = 0
        self.rangeMap[Range(481, 490)] = 0
        self.rangeMap[Range(471, 480)] = 0
        self.rangeMap[Range(461,470)] = 0
        self.rangeMap[Range(451, 460)] = 0
        self.rangeMap[Range(441, 450)] = 0
        self.rangeMap[Range(431, 440)] = 0
        self.rangeMap[Range(421, 430)] = 0
        self.rangeMap[Range(411, 420)] = 0
        self.rangeMap[Range(401, 410)] = 0
        self.rangeMap[Range(351, 400)] = 0
        self.rangeMap[Range(301, 350)] = 0
        self.rangeMap[Range(0, 300)] = 0
        self.aggregatedRangeMap = {}
        self.aggregatedRangeMap[Range(601, 1200)] = 0
        self.aggregatedRangeMap[Range(501, 600)] = 0
        self.aggregatedRangeMap[Range(451, 500)] = 0
        self.aggregatedRangeMap[Range(401, 450)] = 0
        self.aggregatedRangeMap[Range(351, 400)] = 0
        self.aggregatedRangeMap[Range(301, 350)] = 0
        self.aggregatedRangeMap[Range(0, 300)] = 0
        self.total = 0

    def __init__(self, data: json):
        self.rangeMap = {}
        self.rangeMap[Range(601, 1200)] = data['dd1']
        self.rangeMap[Range(501-600)] = data['dd2']
        self.rangeMap[Range(491,500)] = data['dd4']
        self.rangeMap[Range(481, 490)] = data['dd5']
        self.rangeMap[Range(471, 480)] = data['dd6']
        self.rangeMap[Range(461,470)] = data['dd7']
        self.rangeMap[Range(451, 460)] = data['dd8']
        self.rangeMap[Range(441, 450)] = data['dd10']
        self.rangeMap[Range(431, 440)] = data['dd11']
        self.rangeMap[Range(421, 430)] = data['dd12']
        self.rangeMap[Range(411, 420)] = data['dd13']
        self.rangeMap[Range(401, 410)] = data['dd14']
        self.rangeMap[Range(351, 400)] = data['dd15']
        self.rangeMap[Range(301, 350)] = data['dd16']
        self.rangeMap[Range(0, 300)] = data['dd17']
        self.aggregatedRangeMap = {}
        self.aggregatedRangeMap[Range(601, 1200)] = data['dd1']
        self.aggregatedRangeMap[Range(501, 600)] = data['dd2']
        self.aggregatedRangeMap[Range(451, 500)] = data['dd3']
        self.aggregatedRangeMap[Range(401, 450)] = data['dd9']
        self.aggregatedRangeMap[Range(351, 400)] = data['dd15']
        self.aggregatedRangeMap[Range(301, 350)] = data['dd16']
        self.aggregatedRangeMap[Range(0, 300)] = data['dd17']
        self.total = data['dd18']


    def getRange(self, score):
        bottomRanges = [601, 501, 491, 481, 471, 461, 451, 441, 431, 421, 411, 401, 351, 301, 0]
        insertPoint = bisect(bottomRanges, score)
        return insertPoint

class Range:
    
    def __init__(self, top, bottom):
        self.top = top
        self.bottom = bottom

    def isInRange(self, score) -> bool:
        return self.top <= score <= self.bottom
    
