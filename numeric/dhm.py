p            = 613144603035200518605071627722399281527
base         = 347449578131074797459449734586666998031
alice_secret = 474140564715023867271727810192114419457
bob_secret   = 556327197178837163583577967104054021837
alice_sends  = pow(base,        alice_secret, p)
bob_sends    = pow(base,        bob_secret,   p)
alice_key    = pow(bob_sends,   alice_secret, p)
bob_key      = pow(alice_sends, bob_secret,   p)

print 'Alice,Bob probable prime', p
print 'Alice,Bob base          ', base
print 'Alice sends Bob         ', alice_sends
print 'Bob   sends Alice       ', bob_sends
print 'Alice creates key       ', alice_key
print 'Bob   creates key       ', bob_key
