from bisect import bisect
import json

class Range:
    
    def __init__(self, bottom: int, top: int):
        self.top = top
        self.bottom = bottom

    def is_in_range(self, score: int) -> bool:
        return self.bottom <= score <= self.top

    def __str__(self):
        return "(" + self.top.__str__() + " - " + self.bottom.__str__() + ")"

class ScoreMap:

    max_range_value = 1200

    def __init__(self, data: json):
        self.range_map = {}
        self.aggregated_range_map = {}
        self.total = data['dd18']
        self.range_map[Range(601, 1200)] = data['dd1']
        self.range_map[Range(501, 600)] = data['dd2']
        self.range_map[Range(491, 500)] = data['dd4']
        self.range_map[Range(481, 490)] = data['dd5']
        self.range_map[Range(471, 480)] = data['dd6']
        self.range_map[Range(461, 470)] = data['dd7']
        self.range_map[Range(451, 460)] = data['dd8']
        self.range_map[Range(441, 450)] = data['dd10']
        self.range_map[Range(431, 440)] = data['dd11']
        self.range_map[Range(421, 430)] = data['dd12']
        self.range_map[Range(411, 420)] = data['dd13']
        self.range_map[Range(401, 410)] = data['dd14']
        self.range_map[Range(351, 400)] = data['dd15']
        self.range_map[Range(301, 350)] = data['dd16']
        self.range_map[Range(0, 300)] = data['dd17']
        self.aggregated_range_map[Range(601, 1200)] = data['dd1']
        self.aggregated_range_map[Range(501, 600)] = data['dd2']
        self.aggregated_range_map[Range(451, 500)] = data['dd3']
        self.aggregated_range_map[Range(401, 450)] = data['dd9']
        self.aggregated_range_map[Range(351, 400)] = data['dd15']
        self.aggregated_range_map[Range(301, 350)] = data['dd16']
        self.aggregated_range_map[Range(0, 300)] = data['dd17']
        self.range_lookup = [None] * (self.max_range_value + 1)
        for interval in self.range_map.keys():
            for x in range(interval.bottom, interval.top + 1):
                self.range_lookup[x] = interval

    def get_range(self, score: int) -> Range:
        return self.range_lookup[score]
    
    def calculate_approx_rank(self, score: int) -> int:
        if 0 <= score and score <= 1200:
            rank = 0
            for interval, number in self.range_map.items():
                number = number.replace(",", "")
                number = int(number)
                if interval.bottom <= score  and score <= interval.top:
                    # score lies within this range
                    total_range = interval.top - interval.bottom + 1
                    remaining_range = interval.top - score
                    proportion = remaining_range / total_range
                    rank += int(number * proportion)
                elif interval.bottom > score:
                    # score is below this range
                    rank += number
                else:
                    # score is above this range
                    continue
            return 1 if rank == 0 else rank
        else:
            return -1