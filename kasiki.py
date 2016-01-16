# demo kasiki method for cracking Vigenere cipher
# usage: python kasiki < ciphertext
from sys import stdin
from collections import Counter
from string import ascii_lowercase # ab ... z

englishFreq = (.081, .001, .027, .042, .127, .022, .020, .061, .070, .002, .008, .040, .024, .067, .075, .019, .001, .060, .063, .091, .028, .010, .024, .002, .020, .001)

def vigStrings(L,k): # split L text into k substrings
  strings = []
  for _ in range(k):
    strings.append('')
  j = 0 # string index
  for line in L:
    for x in line:
      if x in ascii_lowercase: 
        strings[j] += x
        if j + 1 == k: j = 0
        else: j += 1
  return strings

def letterFreq(S): 
  freq = Counter()
  for x in S: 
    freq += Counter(x)
  return freq # dictionary of a..z freqs in S

def ratios(F): # indexed in alphabetic order
  numChars = sum(F.values())
  R = []
  for x in ascii_lowercase: 
    R.append(1.0*F[x]/numChars)
  return R

def imc(X,Y): # index of mutual coincidence vectors X,Y
  return sum(map(lambda x,y: x*y, X, Y))

def imcdemo(S,V): # index of mutual coincidence S with vector v
  print S
  alpha = len(ascii_lowercase)
  assert(len(S)>0) and (len(V)==alpha)
  freq = letterFreq(S)
  print freq
  R = ratios(freq)
  bestshift, maxval = 0, 0.0
  for shift in range(alpha):
    imcval, j = 0.0, 0
    for j in range(alpha):
      imcval += V[j]*R[(j+shift)%alpha]
    if imcval > maxval: 
      bestshift, maxval = shift, imcval
    print 'shift', shift, imcval
  return ascii_lowercase[bestshift]
      
def ioc(S): # return index of coincidence of S
  assert(len(S)>0)
  freq = letterFreq(S)
  numChars = 0
  for x in ascii_lowercase:
    numChars += freq[x]

  ioc = 0.0
  for x in ascii_lowercase:
    fraction = freq[x]*1.0/numChars
    ioc += 1.0*freq[x]*(freq[x]-1)*1.0/(numChars*(numChars-1))
  return ioc

Input = []
for line in stdin:
  Input.append(line)

def findkeylength(Input, maxlength):
  bestk, maxioc = 1, 0.0
  for k in range(1,maxlength+1):
    S = vigStrings(Input,k)
    total = 0.0
    for s in S:
      total += ioc(s)
    avgioc = total/k
    print 'key length', k, ':', avgioc, '\n'
    if avgioc > maxioc:
      bestk, maxioc = k, avgioc
  return bestk

b = findkeylength(Input,10)
print b

S = vigStrings(Input,b)
bestkey = ''
for s in S:
  print s
  bestkey += imcdemo(s, englishFreq)
print 'best key', bestkey
