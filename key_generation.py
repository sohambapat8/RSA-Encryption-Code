import random

p = 11
q = 13 #set to small numbers for testing purposes, prime randomiser function would be used instead of this.

publickeytwo = p*q

privatekeytwo = publickeytwo

def coprime(n):
  factorlist = []
  coprimelist = []
  for i in range(1,n):
    if n % i == 0:
      factorlist.append(i)
    flag = True
    for k in range(len(factorlist)):
      if i % factorlist[k] == 0 and factorlist[k]!=1:
        flag = False
    if flag == True:
      coprimelist.append(i)
  return coprimelist

coprime_n = coprime(publickeytwo)

coprime_n_size = (p-1)*(q-1)

if len(coprime_n) == coprime_n_size:
  print("Successful check of co-prime")
else:
  print("Went wrong somewhere")

coprime_phi_n = coprime(coprime_n_size)

combinedlist = []

for i in range(len(coprime_n)):
  if coprime_n[i] in coprime_phi_n and coprime_n[i] > 1 and coprime_n[i] < coprime_n_size:
    combinedlist.append(coprime_n[i])

publickeyone = random.choice(combinedlist)

print("Public keys: {},{}".format(publickeyone,publickeytwo))


def extendedeuclidean(dividend,divisor):
    s=[1,0]
    t=[0,1]
    counter = 1 #starts off at index 1
    remainder = 2
    while(remainder != 0):
        quotient = dividend // divisor
        remainder = dividend % divisor
        dividend = divisor
        divisor = remainder
        svalue = s[counter-1] - quotient*s[counter]
        tvalue = t[counter-1] - quotient*t[counter]
        s.insert(counter+1,svalue)
        t.insert(counter+1,tvalue)
        counter = counter+1
        remainder = dividend % divisor
    
    return(s[-1],t[-1])


test,privatekeyone = extendedeuclidean(coprime_n_size,publickeyone)
if privatekeyone < 0:
    privatekeyone = privatekeyone + coprime_n_size
    
    
print("Private keys: {},{}. Note this would be kept secret in an industrial application".format(privatekeyone,privatekeytwo))




#TESTING
    
originalmessage = 2

print("Original message:{}".format(originalmessage))


encoded = (originalmessage ** publickeyone) % publickeytwo

print("Encoded message:{}".format(encoded))

decoded = (encoded**privatekeyone) % publickeytwo

print("Decoded message:{}".format(decoded))






#Above code refers to the generation of the public key.

# print(factorsofn)
# print(coprime)


#Push to file path: Encryption/RSA_Encryption.ipynb