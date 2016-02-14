import sys
from string import ascii_lowercase

def words(text):
  W = []
  wrds = text.split()
  for w in wrds:
    #wstr = "'"+ w + "',"
    #print wstr,
    W.append(w)
  return W

def MorseEncrypt(txt):
  out = ''
  for c in txt:
    if c in ascii_lowercase:
      out += M[ord(c)-ord('a')] + ' '
    else:
      out += c
  return out

M = ['._', '_...', '_._.', '_..', '.', 
     '.._.', '__.', '....', '..', '.___',
     '_._', '._..', '__', '_.', '___', 
     '.__.', '__._', '._.', '...', '_', 
     '.._', '..._', '.__', '_.._', '_.__', '__..']

text = sys.stdin.read()
print MorseEncrypt(text)
