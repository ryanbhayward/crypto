import sys
from string import ascii_lowercase

L = sys.stdin.readlines()
  
for k in range(len(L)):
  L[k] = L[k].strip('\n')

def alphaOp(s1,op,s2):
  mylen = min(len(s1),len(s2))
  result = ''
  assert op in '+-'
  for j in range(mylen):
    c1,c2 = s1[j],s2[j]
    if c1 in ascii_lowercase and c2 in ascii_lowercase:
      if op == '-': 
        offset = ( ord(c1) - ord(c2) ) %26
      else:
        offset = ( ord(c1) + ord(c2) - 2*ord('a')) %26
      result += chr(ord('a') + offset)
    elif c1==' ' and c2==' ':
      result += ' '
    else:
      result += '.'
  return result

indent = '  '
for k in L:
  print indent + k
  
for j in range(2):
  print '\ntry guess as plaintext', 1+j
  key =  alphaOp(L[j],'-',L[2])
  print indent + key
  print indent + alphaOp(L[1-j],'-',key)
