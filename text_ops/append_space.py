# on each line, append space character to every character
import sys

L = sys.stdin.readlines()
  
for line in L:
  for c in line:
    print c,
  print ''
