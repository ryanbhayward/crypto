# simple caesar shift cipher
# usage: python caesar.py < caesar.in

#   sample caesar.in (remove #):
# 3
# hello world

#   sample output:
# khoor zruog

#   to decrypt, use this caesar.in:
# -3  <== or here, 23 instead of -3
# khoor zruog

from sys import stdin
from string import ascii_lowercase # ab ... z

# shift <- number on 1st line of input file
shift = int(stdin.readline().split()[0])

# plaintext is on 2nd line of input file
output = ''
for c in stdin.readline():
  if c in ascii_lowercase:
    output += chr(ord('a')+ (shift + ord(c) - ord('a'))%26)
  else:
    output += c
print output,
