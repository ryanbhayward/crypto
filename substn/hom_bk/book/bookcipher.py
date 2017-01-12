# simple book cipher... initials labelled from 0
from random import randint
from sys import stdin, argv
from string import ascii_lowercase

def condense(infile):
  out, getNextLetter = '', True
  for c in infile:
    if getNextLetter:
      if c.lower() in ascii_lowercase:
        out += c.lower()
        getNextLetter = False
    else:
      if c.lower() not in ascii_lowercase:
        getNextLetter = True
  return out

def init(s):
  H = {} # dictionary of character homophones
  for c in ascii_lowercase: 
    H[c] = []
  for j in range(len(s)):
    H[s[j]].append(j)
  # ensure each letter has at least one homophone:
  for c in reversed(sorted(H)): 
    if len(H[c])==0: 
      print 'warning: adding', c
      H[c].append(len(s))
      s += c
  return H, s

def encrypt(H):
  for line in stdin:
    for c in line:
      if c.lower() in H: 
        homs = H[c.lower()]
        assert len(homs) > 0 # otw, no way to encrypt
        print homs[randint(0,len(homs)-1)],
    print ''

def decrypt(instring):
  outline = ''
  for line in stdin:
    for n in line.split():
      outline += instring[int(n)]
  print outline

if len(argv)==1:  
  print("\nusage: python bookcipher.py -f bookfile [-d] < txtfile ")
else:
  instring = condense(open(argv[2]).read())
  H, keystring = init(instring)
  #print H, keystring
  if len(argv)==4: # beale.py -f bkf -d, so decrypt
    decrypt(keystring)
  else: 
    encrypt(H)
