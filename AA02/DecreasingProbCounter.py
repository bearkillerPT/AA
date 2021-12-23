import sys
import random
import math
comps = 0
class DecreasingProbCounter():
    def __init__(self, filename, prob_decrease=lambda x:1/(math.sqrt(3)**x)):
        fp = open(filename, "r")
        self.index = self.count_decreasing_prob(fp, prob_decrease)

    def count_decreasing_prob(self, fp, prob_decrease):
        global comps
        index = {}
        i = 0
        current_prob = 1
        for line in fp.readlines():
            for word in line.split(' '):
                for char in word:
                    to_count = random.random()
                    if to_count <= current_prob:
                        if char in index.keys():
                            index[char] += 1
                        else:    
                            index[char] = 1
                        comps += 1
                        i += 1
                        current_prob = current_prob + prob_decrease(i)
                    comps += 1
        return index

if __name__ == "__main__":
    min_length_filter=0
    stop_word_list = []
    porter_stemmer = True
    if len(sys.argv) == 1:
        usage = 'Usage:\n\tpython3 DecreasingProbCounter.py filename'
        print(usage)
    elif len(sys.argv) == 2:
        exact_counter = DecreasingProbCounter(sys.argv[1])
        index_sorted_by_value = dict(sorted(exact_counter.index.items(), key=lambda item: item[1], reverse=True))
        print(index_sorted_by_value)
        print("Comps: " + str(comps))
