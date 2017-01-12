# simple book cipher
from random import randint
from sys import stdin, argv
from string import ascii_lowercase # ab ... z

inchars = ' .,:;abcdefghijklmnopqrstuvwxyz'

def condense(infile):
  out = ''
  for line in infile:
    for c in line.lower():
      if c in inchars: out += c
  return out

def init(s):
  H = {} # dictionary of character homophones
  for c in inchars: 
    H[c] = []
  for j in range(len(s)):
    H[s[j]].append(j)
  return H

def encrypt(H):
  for line in stdin:
    for c in line:
      if c in H: 
        homs = H[c]
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
  print("\nusage: python beale.py -f bookfile [-d] < txtfile ")
else:
  instring = condense(open(argv[2]).read()) + inchars
  H = init(instring)
  # print instring, H
  if len(argv)==4: # beale.py -f bkf -d, so decrypt
    decrypt(instring)
  else: 
    encrypt(H)
