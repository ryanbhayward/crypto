# beale cipher, English alphabet
import sys, random

def psn(ch):
  return ord(ch)-ord('a')

def strip(str):
  new = ""
  for ch in str:
    if ch.isalpha() or ch.isspace():  #keep only these
      new += ch
  return new

def initKey(contents):
  H = [[] for x in range(26)]
  Inv = []
  count = 0
  for word in contents.split():
    ch = word[0].lower() #first ch
    H[psn(ch)].append(count)
    Inv.append(ch)
    count += 1
  return H, Inv

def encrypt(ln,H):
  txt = ""
  for ch in ln:
    if ch.isalpha():
      homs = len(H[psn(ch)])
      assert homs > 0 # otw, no way to encrypt
      txt += str(H[psn(ch)][random.randint(0,homs-1)]) + ' '
  return txt

def decrypt(ln,I):
  txt = ""
  for str in ln.split():
    txt += I[int(str)]
  return txt

if len(sys.argv)==1:  
  print("\nusage: python beale.py -f bookfile [-d] < txtfile ")
else:
  bk = open(sys.argv[2]).read()
  Homophones, Inverse = initKey( strip( bk ) )
  if len(sys.argv)==4: # beale.py -f bkf -d, so decrypt
    for line in sys.stdin:
      print decrypt(line,Inverse)
  else: # encrypt
    for line in sys.stdin:
      print encrypt(line,Homophones)
