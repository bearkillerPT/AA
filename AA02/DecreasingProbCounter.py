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
        prob = prob_decrease(i)

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
                        i += 1
                        prob = prob_decrease(i)
                    comps += 1
        return index

if __name__ == "__main__":
    random.seed(88194)
    min_length_filter=0
    stop_word_list = []
    porter_stemmer = True
    if len(sys.argv) == 1:
        usage = 'Usage:\n\tpython3 DecreasingProbCounter.py filename'
        print(usage)
    elif len(sys.argv) == 2:
        exact_counter = DecreasingProbCounter(sys.argv[1])
        expected_counts = {}
        for char in exact_counter.index:
            expected_counts[char] =  math.floor(math.log(exact_counter.index[char] ,math.sqrt(3))) + 1
        index_sorted_by_value = dict(sorted(exact_counter.index.items(), key=lambda item: item[1], reverse=True))
        expected_index_sorted_by_value = dict(sorted(expected_counts.items(), key=lambda item: item[1], reverse=True))
        print("Counter")
        print(index_sorted_by_value)
        print("Expected counts")
        print(expected_index_sorted_by_value)
        print("Comps: " + str(comps))
