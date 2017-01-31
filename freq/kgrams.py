# in given text, check for repeated k-grams

from string import letters, punctuation
from sys import stdin

txt = ''
for line in stdin:
  for c in line:
    if c in letters:
      txt += c

def kgrams(txt, kgram_length):
  print 'check for repeated', kgram_length, '-grams'
  for j in range(len(txt)-(kgram_length-1)):
    kgram = txt[j:j+kgram_length]
    for k in range(j+kgram_length, len(txt)-(kgram_length-1)):
      if kgram == txt[k:k+kgram_length]:
        print k-j, kgram

for t in range(2,4):
  kgrams(txt, t)
