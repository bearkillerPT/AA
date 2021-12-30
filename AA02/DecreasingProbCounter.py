import sys
import random
import math
comps = 0
class DecreasingProbCounter():
    def __init__(self, filename, prob_decrease=1/math.sqrt(3)):
        fp = open(filename, "r", encoding='utf-8')
        self.index = self.count_decreasing_prob(fp, prob_decrease)
        
    def count_decreasing_prob(self, fp, prob_decrease=1/math.sqrt(3)):
        global comps
        index = {}
        probs = {}
        for line in fp.readlines():
            line = "".join(filter(str.isalpha,line))
            for word in line.split(' '):
                for char in word:
                    if char not in probs:
                        probs[char] = 1
                    to_count = random.random()
                    if to_count <= probs[char]:
                        if char in index.keys():
                            index[char] += 1
                        else:    
                            index[char] = 1
                        comps += 1
                        probs[char] *= prob_decrease
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
        expected_counts = {}
        for char in exact_counter.index:
            expected_counts[char] = (math.sqrt(3)**exact_counter.index[char] - math.sqrt(3) + 1) / (math.sqrt(3) - 1)
        index_sorted_by_value = dict(sorted(exact_counter.index.items(), key=lambda item: item[1], reverse=True))
        expected_index_sorted_by_value = dict(sorted(expected_counts.items(), key=lambda item: item[1], reverse=True))
        print("Counter")
        print(index_sorted_by_value)
        print("Expected counts")
        print(expected_index_sorted_by_value)
        print("Comps: " + str(comps))
