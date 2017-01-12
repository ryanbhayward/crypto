import sys
from string import ascii_lowercase

L = sys.stdin.readlines()
  
for k in range(len(L)):
  L[k] = L[k].strip('\n')

print L[0]

print 'guessing key or plaintext fragments'
for k in range(1,len(L)):
  for j in range(len(L[k])):
    if L[k][j] != ' ':
      print chr(ord('a') + (ord(L[0][j]) - ord(L[k][j]))%26),
  print ''

