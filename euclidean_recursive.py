def euclidean(a,b):
  r = a%b
  if r == 0:
    return False
  if euclidean(b,r) == False:
    return r
  else:
    return euclidean(b,r)


print(euclidean(888,54))

# this algorithm was adapted and used in the key generation phase to work out the public key.
# Similarly, an 'extended' version of this algorithm was used to work out the private key. 