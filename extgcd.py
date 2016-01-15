def ext_gcd(a,b):  # a >= b > 0
  if (a<b) or (b<=0):
    print '   sorry, want a >= b > 0'
    return
  print '   compute gcd(a,b), a=',a,'  b=',b
  u,v,Q,A = a,b,[],[a,b]
  while (v != 0):
    q,r = u/v, u%v
    print u, '-', v, '*', q, '=', r
    Q.append(q)
    A.append(r)
    u,v = v,r
  print'   express gcd as linear combination of a,b'
  gcd = u   ; A.pop()     ; Q.pop() 
  x,y = 0,1 ; b = A.pop() ; a = A.pop();
  for _ in range(len(Q)):
    x,y = y,       x-Q.pop()*y
    a,b = A.pop(), a
    print u,' = ',a,'*',x,' + ',b,'*',y

#ext_gcd(135,99)
#ext_gcd(21440803,4223527)
#ext_gcd(2144080392351199,422352037373659)
ext_gcd(60534384,35717371)
