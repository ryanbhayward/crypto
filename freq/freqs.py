# unigram and digram frequency,
#   restricted to letters, punctuation, blank

from string import letters, punctuation
from sys import stdin

Unigrams = {} # dict indexed by character
Chars = letters + punctuation + ' '
Instring = ''
for c in Chars:
  Unigrams[c] = 0

for line in stdin:
  for c in line:
    if c in Chars:
      Unigrams[c] += 1
      Instring += c

def newlinecheck(X,y):
  if X[0]==y-1:
    print ''
    X[0] = 0
  else: 
    X[0] += 1

threshold, ItemsThisLine, itemsPerLine = 1, [0], 5
for u in sorted(Unigrams, key=Unigrams.get, reverse=True):
  if Unigrams[u]>= threshold: 
    print u, '%3d' % Unigrams[u], '  ',
    newlinecheck(ItemsThisLine, itemsPerLine)

Digrams = {}
for j in range(len(Instring)-1):
  d = Instring[j:j+2]
  if d in Digrams:
    Digrams[d] += 1
  else:
    Digrams[d] = 1

threshold, ItemsThisLine, itemsPerLine = 2, [0], 5
for d in sorted(Digrams, key=Digrams.get, reverse=True):
  if Digrams[d]>=threshold: 
    print d, '%3d' % Digrams[d], '   ',
    newlinecheck(ItemsThisLine, itemsPerLine)