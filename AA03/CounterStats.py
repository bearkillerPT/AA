from calendar import c
from os import stat
import sys
import math
import json
from ExactCounter import ExactCounter
from LossyCount import LossyCount
class CounterStats():
    def __init__(self, filename, k, n_tests=100) -> None:
        index = {}
        self.counter = LossyCount(filename, k)
        exact_counter = ExactCounter(filename)
        self.zero_abs_err_count = 0
        for word in self.counter.index:
            index[word] = {}
            index[word]["exact_val"] = exact_counter.index[word]
            index[word]["expected"] = self.counter.index[word]
            index[word]["abs_err"] = abs(index[word]["expected"] - index[word]["exact_val"])
            if(index[word]["abs_err"] == 0):
                self.zero_abs_err_count += 1
            index[word]["rel_err"] = str(int(abs(index[word]["expected"] - index[word]["exact_val"]) / index[word]["exact_val"]*100)/100) + "%"
        self.index = dict(sorted(index.items(), key=lambda item: item[1]["abs_err"], reverse=True))

if __name__ == "__main__":
    save_file = "stats.json"
    min_length_filter=0
    stop_word_list = []
    porter_stemmer = True
    if len(sys.argv) == 1:
        usage = 'Usage:\n\tpython3 CounterStats.py filename k\n\tk - k paramether for the LossyCounter'
        print(usage)
    elif len(sys.argv) == 3:
        stats = CounterStats(sys.argv[1], int(sys.argv[2]))
        print(stats.index)
        json.dump(stats.index, open(save_file, 'w'))
        print("n/k -> " + str(stats.counter.n /  int(sys.argv[2])))
        print("n -> " + str(stats.counter.n ))
        print("zero abs error count:  " + str(stats.zero_abs_err_count))
        
