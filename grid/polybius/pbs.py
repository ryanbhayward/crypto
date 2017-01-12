import sys
from string import whitespace
# IN PROGRESS

def initIndices(L):
  return L[0]

def initGrid(L,n):
  Grid = ''
  for j in range(n):
    Grid += L[j+1].translate(None,whitespace)
  return Grid

def initPsns(G,n):
  P = {}
  for j in range(len(G)):
    P[G[j]] = j
  return P

def pbsEncrypt(n,I,G,P,txt):
  assert(n==len(I))
  out = ''
  for c in txt:
    if c in G:
      out += I[P[c] / n] + I[P[c] % n]
    else:
      out += c
  return out

def pbsDecrypt(n,I,G,txt):
  assert(n==len(I))
  out = ''
  tx = txt.translate(None,whitespace)
  assert(len(tx)%2 == 0)
  for c in tx: 
    assert c in I
  Lookup = {}
  for j in range(len(I)):
    Lookup[I[j]] = j
  out = ''
  for j in range(len(tx)/2):
    out += Grid[n*Lookup[tx[2*j]]+ Lookup[tx[2*j+1]]]
  return out

Lines   = sys.stdin.read().split('\n')
Indices = initIndices(Lines)
n       = len(Indices)
Grid    = initGrid   (Lines,n)
Psns    = initPsns   (Grid, n)

print Indices
for j in range(n):
  print Lines[j+1]
#print 'Psns:'
#for p in Psns:
#  print p, Psns[p]
for j in range(len(Lines)-(n+1)):
  if len(sys.argv)==1:  # python pbs.py < infile
    print pbsEncrypt(n,Indices,Grid,Psns,Lines[j+n+1])
  elif sys.argv[1]=="-d":  # python pbs.py -d < infile
    print pbsDecrypt(n,Indices,Grid,Lines[j+n+1])
  else:  print 'format error?'
