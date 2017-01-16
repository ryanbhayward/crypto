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
#for u in sorted(Unigrams, key=Unigrams.get, reverse=True):
  #if Unigrams[u]>= threshold: 
    #print u, '%3d' % Unigrams[u], '  ',
    #newlinecheck(ItemsThisLine, itemsPerLine)
for u in sorted(Unigrams, key=Unigrams.get, reverse=True):
  if Unigrams[u]>= threshold: 
    print u, 
print ''
for u in sorted(Unigrams, key=Unigrams.get, reverse=True):
  if Unigrams[u]>= threshold: 
    print '%2d' % Unigrams[u], 
print ''

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
    print d, Digrams[d], '   ',
    newlinecheck(ItemsThisLine, itemsPerLine)

alph = 'abcdefghijklmnopqrstuvwxyz'
print '\n\n ',
for c in alph:
  print '  ' + c,
print ''
for c in alph:
  print c,
  for d in alph:
    if c+d in Digrams:
      print '%3d' % Digrams[c+d],
    else:
      print '%3d' % 0,
  print ''
