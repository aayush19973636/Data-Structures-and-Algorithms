a = 'this is a word string having many word'
k = 2

def kFrequency(s,k):
    words = a.split()
    d = {}
    for w in words:
        d[w] = d.get(w, 0) + 1
    for w in d:
        if d[w] == k:
            print(w)
kFrequency(a,k)