# usage: python ioc.py < frequencyfile
# index of coincidence is sum of squares of frequencies
from sys import stdin
ioc = 0.0 
for line in stdin:
  freqs = map(float, line.split())
  for f in freqs: 
    print f,
    ioc += f*f
  print ''
print ioc
