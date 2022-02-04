import sys
import math
import copy
from datetime import date, datetime

comps = 0
class LossyCount():
    def __init__(self, filename, k):
        time_start = datetime.now()
        fp = open(filename, "r", encoding='utf-8')
        self.index = self.count(fp, k)
        time_end = datetime.now()
        self.index_time = time_end - time_start

    def count(self, fp, k):
        global comps
        index = {}
        self.n = 0
        delta = 0
        for line in fp.read().splitlines():
            for word in line.split(' '):
                self.n += 1
                if word in index.keys():
                    index[word] += 1
                else:
                    index[word] = 1 + delta
                comps += 1
                if math.floor(self.n/k) != delta:
                    delta = math.floor(self.n/k)
                    index_keys = copy.deepcopy(set(index.keys()))
                    for word in index_keys:
                        comps += 1
                        if index[word] < delta:
                            index.pop(word)
        return index

if __name__ == "__main__":
    min_length_filter=0
    stop_word_list = []
    porter_stemmer = True
    if len(sys.argv) == 1:
        usage = 'Usage:\n\tpython3 LossyCount.py filename k'
        print(usage)
    elif len(sys.argv) == 3:
        lossy_boy = LossyCount(sys.argv[1], int(sys.argv[2]))
        index_sorted_by_value = dict(sorted(lossy_boy.index.items(), key=lambda item: item[1], reverse=True))
        print("Count:")
        print(index_sorted_by_value)
        print("Comps: " + str(comps))
