# usage: python imc.py < frequencyfile
# index of mutual coincidence is crosswise product
from sys import stdin
imc = 0.0 
F = []
for line in stdin:
  F.append(map(float, line.split()))
print F
for j in range(len(F[0])):
  imc += F[0][j]*F[1][j]
print imc
