import random 
import os
import string
import sys
import re

stopWordsList = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours",
            "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its",
            "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that",
            "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having",
            "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
            "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
            "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
            "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
            "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
            "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

delimiters = " \t,;.?!-:@[](){}_*/"

def getIndexes(seed):
    random.seed(seed)
    n = 10000
    number_of_lines = 50000
    ret = []
    for i in range(0,n):
        ret.append(random.randint(0, 50000-1))
    return ret

def process(userID):
    indices = getIndexes(userID)
    ret = []
    # TO DO
   # thanks https://www.programcreek.com/python/example/161/re.escape
    deli = '|'.join(map(re.escape, delimiters))

    Counter = {}
    file = sys.stdin
    titles = [ title for title in file]
    for i in indices:    
        # thanks https://stackoverflow.com/questions/21107505/word-count-from-a-txt-file-program DELIMITER /// strip() - remove  leading/trailing /// lower() - convert to lower case
        words = [x.strip().lower() for x in re.split(deli, titles[i])]
        for token in words:
            if token not in stopWordsList + ['']:  # to avoid the STOPLIST
                if token in Counter:
                    Counter[token] += 1       
                else:
                    Counter[token] = 1
                                
    items = sorted(Counter, key=lambda x: (-Counter.get(x), x))
    
    ret = items[:20]
 
    for word in ret:
        print word
    
process(sys.argv[1])
