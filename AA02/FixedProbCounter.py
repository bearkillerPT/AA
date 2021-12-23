import sys
import random
comps = 0
class FixedProbCounter():
    def __init__(self, filename, prob=1/4):
        fp = open(filename, "r")
        self.index = self.count_fixed_prob(fp, prob)

    def count_fixed_prob(self, fp, prob):
        global comps
        index = {}
        for line in fp.readlines():
            for word in line.split(' '):
                for char in word:
                    to_count = random.random()
                    if to_count <= prob:
                        if char in index.keys():
                            index[char] += 1
                        else:    
                            index[char] = 1
                        comps += 1
                    comps += 1
        return index

if __name__ == "__main__":
    min_length_filter=0
    stop_word_list = []
    porter_stemmer = True
    if len(sys.argv) == 1:
        usage = 'Usage:\n\tpython3 FixedProbCounter.py filename'
        print(usage)
    elif len(sys.argv) == 2:
        exact_counter = FixedProbCounter(sys.argv[1])
        index_sorted_by_value = dict(sorted(exact_counter.index.items(), key=lambda item: item[1], reverse=True))
        print(index_sorted_by_value)
        print("Comps: " + str(comps))
