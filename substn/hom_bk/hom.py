# homophonic substitution 
#            : encrypt sequential hom.
#     -r     : encryp  random     "   
#     -d     : decrypt 

# WARNING: to guarantee decrypt(encrypt(txt)) == txt 
#   txt should not contain any non-lowercase homophones

import sys, random

alph    = "abcdefghijklmnopqrstuvwxyz"
homAlph = "aaabcddeeeeefghhhiiijkllmnnnoooopqrrrsssttttuvwxyz"
cipAlph = "uXdGkNrUyaDhKoRvYAeHlOsVbEiLpSwBfImPtWcFjMqTxCgJnQ"

#homAlph = "aaabcdeeeefghijklmnoopqrstttuvwxyz"
#cipAlph = "TheCZatinHByDrSusvwxzfgjklmopqcAEF"

assert len(alph)==26
assert len(homAlph)==len(cipAlph)
# each alph character should be in homAlph
for ch in alph:
  assert 0 <= homAlph.find(ch) < len(homAlph)
# cipAlph should have no duplicates
for j in range( len(cipAlph) ):
  assert cipAlph.find( cipAlph[j] ) == j

# init Homophone list from homAlph, cipAlph
Homophones = [""]*len(alph)  # each char has list of homophones
for j in range( len(homAlph) ):
  ch = homAlph[j]
  idx = alph.find(ch)
  Homophones[idx] += cipAlph[j]
Count = [0]*len(alph)  # used in sequential homophonic encryption

def substLine(ln,inAlph,outAlph):
  txt = ""
  for ch in ln:
    idx = inAlph.find(ch)
    if 0 <= idx < len(inAlph): 
      txt += outAlph[idx]
    else:
      txt += ch
  return txt

def encryptLine(ln,alph,Homs):
  txt = ""
  for ch in ln:
    idx = alph.find(ch)
    if 0 <= idx < len(alph):
      txt += Homs[idx][Count[idx]]
      Count[idx] += 1
      if Count[idx]==len(Homs[idx]):
        Count[idx] = 0
    else:
      txt += ch
  return txt

def randomEncryptLine(ln,alph,Homs):
  txt = ""
  for ch in ln:
    idx = alph.find(ch)
    if 0 <= idx < len(alph):
      str = Homs[idx]
      txt += str[random.randint(0,len(str)-1)]
    else:
      txt += ch
  return txt

# main block
if len(sys.argv)==1:  # python hom.py < infile
  for line in sys.stdin:
    txt = encryptLine(line,alph,Homophones)
    print txt,
elif sys.argv[1]=="-r":  # random homophonic substitution
  for line in sys.stdin:
    txt = randomEncryptLine(line,alph,Homophones)
    print txt,
elif sys.argv[1]=="-d":  # decrypt
  for line in sys.stdin:
    txt = substLine(line,cipAlph,homAlph)
    print txt,
else:
  print("\nusage: python hom.py [-d] [-r] < infile")
