# return offsets of repeated k-grams
# k is subtring length

from string import letters, punctuation
from sys import stdin

ptxt = ''
for line in stdin:
  for c in line:
    if c in letters:
      ptxt += c

ssl = 3 # substring length

for k in range(len(ptxt)-(ssl-1)):
  kgram = ptxt[k:k+ssl]
  for j in range(k+ssl, len(ptxt)-(ssl-1)):
    if kgram == ptxt[j:j+ssl]:
      print k, j, j-k, kgram
