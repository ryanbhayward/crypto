# return offsets of repeated trigrams

from string import letters, punctuation
from sys import stdin

ptxt = ''
for line in stdin:
  for c in line:
    if c in letters:
      ptxt += c

for k in range(len(ptxt)-2):
  trigram = ptxt[k:k+3]
  for j in range(k+3, len(ptxt)-2):
    if trigram == ptxt[j:j+3]:
      print k, j, j-k, trigram
