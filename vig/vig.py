# vigenere     based on Miller&Ranum, tips from Kondrak.

# takes arbitrarily long key 
# key stripped of non-alph., upper --> lower
# key psn shifts *only* with alph. ptxt char

# input:  key, line starting with #, ptxt
# usage: python vig.py [-d] < infile
import sys

alphabet = "abcdefghijklmnopqrstuvwxyz"
alphLen = len(alphabet)
assert(26==alphLen)

def ltrToIdx(ch):
  idx = alphabet.find(ch.lower())
  assert idx >= 0
  return idx

def idxToLtr(idx):
  assert (0 <= idx and idx <= alphLen)
  return alphabet[idx]

def vigAdd(kCh,pCh):
  return idxToLtr((ltrToIdx(pCh) + ltrToIdx(kCh)) % alphLen)

def vigSub(kCh,cCh):
  return idxToLtr((ltrToIdx(cCh) - ltrToIdx(kCh)) % alphLen)

def stripAndLower(str):
  new = ""
  for ch in str:
    if ch.isalpha():
      new += ch.lower()
  return new

def encipher(intxt,key,add):
  outtxt = ""
  keyLen = len(key)
  chCount = 0
  for ch in intxt:
    if ch.isalpha(): 
      if add:
        outtxt += vigAdd(key[chCount%keyLen],ch)
      else:
        outtxt += vigSub(key[chCount%keyLen],ch)
      chCount += 1
    else:
      outtxt += ch
  return outtxt

def readInput():
  k = ""
  ptx = ""
  readingKey = True
  for line in sys.stdin:
    if line[0] == '#':
      readingKey = False
    elif readingKey:
      k += line
    else:
      ptx += line
  k = stripAndLower(k)
  assert(len(k) > 0)
  return k,ptx

key,txt = readInput()
print(key)
print('#')
if len(sys.argv)==1:  # python vig.py < infile
  print(encipher(txt,key,True)),
elif sys.argv[1]=="-d":  # python vig.py -d < infile
  print(encipher(txt,key,False)),
else:
  print("\nusage: python vig.py [-d] < infile")
