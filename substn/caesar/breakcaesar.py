from sys import stdin
from string import ascii_lowercase # ab ... z

Input = []
for line in stdin:
  Input.append(line)

for shift in range(26):
  print 'shift', shift
  outstring = ''
  for line in Input:
    for x in line:
      if x in ascii_lowercase:
        outstring += ascii_lowercase[(shift + ord(x)-ord('a'))%26]
      else: outstring += x
  print outstring
