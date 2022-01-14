import sys
import math

comps = 0
class LossyCount():
    def __init__(self, filename, k):
        fp = open(filename, "r", encoding='utf-8')
        self.index = self.count(fp, k)

    def count(self, fp, k):
        global comps
        index = {}
        n = 0
        delta = 0
        for line in fp.readlines():
            for word in line.split(' '):
                n += 1
                if word in index.keys():
                    index[word] += 1
                else:
                    index[word] = 1 + delta
                comps += 1
        res = {}
        if math.floor(n/k) != delta:
            comps += 1
            delta = math.floor(n/k)
            for word in index.keys():
                comps += 1
                if index[word] >= delta:
                    res[word] = index[word]
        return res

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
