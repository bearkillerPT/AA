import sys
comps = 0
class ExactCounter():
    def __init__(self, filename):
        fp = open(filename, "r", encoding='utf-8')
        self.index = self.parse(fp)

    def parse(self, fp):
        global comps
        index = {}
        for line in fp.read().splitlines():
            for word in line.split(' '):
                if word in index.keys():
                    index[word] += 1
                else:    
                    index[word] = 1
                comps += 1
        return index

if __name__ == "__main__":
    min_length_filter=0
    stop_word_list = []
    porter_stemmer = True
    if len(sys.argv) == 1:
        usage = 'Usage:\n\tpython3 ExactCounter.py filename'
        print(usage)
    elif len(sys.argv) == 2:
        exact_counter = ExactCounter(sys.argv[1])
        index_sorted_by_value = dict(sorted(exact_counter.index.items(), key=lambda item: item[1], reverse=True))
        print("Count:")
        print(index_sorted_by_value)
        print("Comps: " + str(comps))
