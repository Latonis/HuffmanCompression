import heapq

def determineFrequency(string):
    frequency = {}
    for char in string:
        frequency[char] = frequency.get(char, 0) + 1
    return frequency

def createDictionary(set):
    chars = set.keys()
    dict = []
    for c in chars:
        dict.append((set[c], c))
    dict.sort()
    return dict

strin = "hello there"

print(createDictionary(determineFrequency(strin)))