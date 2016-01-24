# smooth english letter frequencies:
# a -> any of aj
# e -> any of eqx
# t -> any of tz
from sys import stdin, argv
from random import randint

def randchar(s):
  return s[randint(0,len(s)-1)]

def smooth(line):
  out = ''
  count = [0,0,0] # bigs occurrences, mod subs length
  for x in line:
    if   x == 'a':  out += randchar('ja')
    elif x == 'e':  out += randchar('xeq')
    elif x == 't':  out += randchar('zt')
    elif x in 'jqxz': out += 'k'
    else:             out += x
  return out

def unsmooth(line):
  out = ''
  for x in line:
    if   x == 'j':  out += 'a'
    elif x in 'qx': out += 'e'
    elif x == 'z':  out += 't'
    else:           out +=  x
  return out

Input = []
for line in stdin:
  if len(argv)==1:  # ... < infile
    print smooth(line)
  else:
    print unsmooth(line)
