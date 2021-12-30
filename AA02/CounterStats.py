from os import stat
import sys
import math
import json
from ExactCounter import ExactCounter
from FixedProbCounter import FixedProbCounter
from DecreasingProbCounter import DecreasingProbCounter
class CounterStats():
    def __init__(self, counter_type, filename, n_tests=100) -> None:
        index = {}
        for i in range(n_tests):
            counter = self.parse(counter_type, filename)
            for char in counter.index:
                if char not in index:
                    index[char] = {"sum": counter.index[char], "count": 1, "max": counter.index[char], "min": counter.index[char]}
                else:
                    index[char]["sum"] += counter.index[char]
                    index[char]["count"] += 1
                    if counter.index[char] < index[char]["min"]:
                        index[char]["min"] = counter.index[char] 
                    elif counter.index[char] > index[char]["max"]:
                        index[char]["max"] = counter.index[char] 
        exact_counter = ExactCounter(filename)
        for char in index:
            index[char]["avg"] = index[char]["sum"] / index[char]["count"]
            index[char]["exact_val"] = exact_counter.index[char]
            if counter_type == "fixed_prob":
                index[char]["expected"] = int(index[char]["avg"] * 4)
            if counter_type == "decreasing_prob":   
                index[char]["expected"] =  int(math.sqrt(3)**index[char]["avg"] - math.sqrt(3) + 1) / (math.sqrt(3) - 1)
            index[char]["abs_err"] = abs(index[char]["expected"] - index[char]["exact_val"])
            index[char]["rel_err"] = int(abs(index[char]["expected"] - index[char]["exact_val"]) / index[char]["exact_val"]*10000)/100

            del index[char]["sum"]
            del index[char]["count"]
        self.index = dict(sorted(index.items(), key=lambda item: item[1]["avg"], reverse=True))

    def parse(self, counter_type, filename):
        if counter_type == "exact":
            return ExactCounter(filename)
        elif counter_type == "fixed_prob":
            return FixedProbCounter(filename)
        elif counter_type == "decreasing_prob":
            return DecreasingProbCounter(filename)
        else:
            return None
        

if __name__ == "__main__":
    save_file = "stats.json"
    min_length_filter=0
    stop_word_list = []
    porter_stemmer = True
    if len(sys.argv) == 1:
        usage = 'Usage:\n\tpython3 CounterStats.py counter_type filename [n_tests]*\n\tcounter_type := exact | fixed_prob | decreasing_prob\n\tn_tests - optional. The number of tests.'
        print(usage)
    elif len(sys.argv) == 3:
        stats = CounterStats(sys.argv[1], sys.argv[2])
        print(stats.index)
        json.dump(stats.index, open(save_file, 'w'))
    elif len(sys.argv) == 4:
        stats = CounterStats(sys.argv[1], sys.argv[2], int(sys.argv[3]))
        print(stats.index)
        json.dump(stats.index, open(save_file, 'w'))