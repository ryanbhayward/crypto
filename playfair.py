# playfair cipher
#            : encrypt 
#     -d     : decrypt 
import re, sys, random

# use alphabet with no j
alph    = "abcdefghiklmnopqrstuvwxyz"
assert len(alph)==25
filler  = "qxz"

def randFill():
  return filler[random.randint(0,len(filler)-1)]

# lowercase alphabetic
def lowercasenoj(ln):
  txt = ""
  for ch in ln:
    if ch.isalpha():
      txt += ch.lower()
  txt = re.sub('j','i',txt)  # j--> i
  return txt

# use filler to separate doublet digrams, e.g. oo --> oqo
# use filler if last digram is incomplete, e.g. th en d --> th en dx
def preprocess(ln):
  txt = ""
  state = 0
  for ch in ln:
    if state == 0:
      prevCh = ch
      state = 1-state # change state
    else:  # state == 1
      if ch==prevCh:
        txt += prevCh + randFill()
      else: # ch!=prevCh
        txt += prevCh + ch
	state = 1-state
  if state == 1: #ended with an incomplete digram
    txt += prevCh + randFill()
  return txt + '\n'

def shifthorizontal(rowcol,j):
  return rowcol[0], (rowcol[1]+j)%5

def shiftvertical(rowcol, j):
  return (rowcol[0]-j)%5, rowcol[1]

def psn(rowcol):
  return 5*rowcol[0] + rowcol[1]

def encipher(cipAlph,dgrm,encrypt):
  idx = divmod(cipAlph.find(dgrm[0]),5), divmod(cipAlph.find(dgrm[1]),5), 
  txt = "" 
  for j in range(2):
    if idx[0][0] == idx[1][0]: # same row
      if encrypt:
        txt += cipAlph[ psn(shifthorizontal(idx[j], 1)) ]
      else:
        txt += cipAlph[ psn(shifthorizontal(idx[j], -1)) ]
    elif idx[0][1] == idx[1][1]: # same col
      if encrypt:
        txt += cipAlph[ psn(shiftvertical(idx[j], -1)) ]
      else:
        txt += cipAlph[ psn(shiftvertical(idx[j], 1)) ]
    else: # switch corners of rectangle
      new = idx[j][0], idx[1-j][1]
      txt += cipAlph[psn(new)] # same row, other col
  return txt

# main block
cipherAlphabet = sys.stdin.readline()
print cipherAlphabet,
if len(sys.argv)==1:  # python playfair.py < infile
  for line in sys.stdin:
    txt = preprocess(lowercasenoj(line))
    ctxt = ""
    for j in range(len(txt)/2):
      ctxt += encipher(cipherAlphabet,txt[2*j]+txt[2*j+1], True)
    ctxt += '\n'
    print ctxt,
elif sys.argv[1]=="-d":  # decrypt
  for line in sys.stdin:
    ptxt = ""
    for j in range(len(line)/2):
      ptxt += encipher(cipherAlphabet,line[2*j]+line[2*j+1], False)
    ptxt += '\n'
    print ptxt,
else:
  print("\nusage: python hom.py [-d] [-r] < infile")
