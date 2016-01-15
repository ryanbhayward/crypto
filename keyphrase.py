# use keyphrase to generate alphabet substitution
#            : after phrase, cycle thru alph from last phrase char
#     -a     : "     "     , "     "    "    "    start of alph

import sys

def keyphrase(alph,phr,lastCh,fromLastChar):
  key = ""
  for ch in phr:
    idx = alph.find(ch)
    if (0 <= idx < len(alph)) and (key.find(ch) < 0):
      key += ch
  if fromLastChar:
    filler = (alph+alph).split(lastCh)[1]
  else:
    filler = alph
  for ch in filler:
    idx = alph.find(ch)
    if (0 <= idx < len(alph)) and (key.find(ch) < 0):
      key += ch
  return key


alphabet = sys.stdin.readline().rstrip() # strip trailing \n
phrase   = sys.stdin.readline().rstrip()
endOfPhrase = phrase[len(phrase)-1]
assert alphabet.find(endOfPhrase) >= 0

if len(sys.argv)==1:  # ... < infile
    print keyphrase(alphabet,phrase,endOfPhrase,True)
elif sys.argv[1]=="-a":  # ... -a < infile
    print keyphrase(alphabet,phrase,endOfPhrase,False)
else:
  print("\nusage: python keyphrase.py [-a] < infile")
