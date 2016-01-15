def binary(x):
   bits = []
   while x:
      x, rmost = divmod(x, 2)
      bits.append(rmost)
   return ''.join(str(b) for b in reversed(bits or [0]))

def bits(x):
   b = []
   while x:
      x, rmost = divmod(x, 2)
      b.append(rmost)
   return b

def slowSlowModExp(a,exp,n):  # a**exp % n
  x = 1
  for _ in range(exp):
    x = x*a
  return x%n

def slowModExp(a,exp,n):  # a**exp % n
   x = 1
   for _ in range(exp):
     x = x*a % n
   return x

def fastModExp(a,exp,n):  # a**exp % n
  print '  compute',a,'**',exp,'(mod',n,')'
  b = bits(exp)
  b.reverse()
  x,e = 1,0
  print '        x =',x
  for j in range(len(b)):
    print b[j], '     ',
    print 'x = x*x',
    x,e = x*x %n, e*2
    if (b[j]):
      x,e = x*a %n, e+1
      print '*a',
    else:
      print '  ',
    print '= x**',e,'=',x

for y in range(8):
   print y, binary(y), '\n'

for y in range(8):
   print y, bits(y), '\n'

for y in range(8):
   print y, slowModExp(2,y,1001)
   print y
   fastModExp(2,y,1001)

n = 1001
big = 10**4
print "python", y, pow(2,big,n)
#print "slow", y, slowModExp(2,big,n)
#print "slow slow", y, slowSlowModExp(2,big,1001)
fastModExp(2,big,n)
