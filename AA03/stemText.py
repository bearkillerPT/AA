from nltk.tokenize import word_tokenize
import string
files = ["winters_tale_en", "winters_tale_fr", "odyssey_en","odyssey_se"]
for file in files:
    f = open(file + ".txt", 'r', encoding='utf-8')
    s =  set(string.punctuation)          # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
    content = ""
    for line in f.readlines():
        if line not in s:
            content += " ".join(e for e in word_tokenize(line) if e not in s)
        content += "\n"
    open(file + "_stemmed.txt", 'w', encoding='utf-8').writelines(content)
    