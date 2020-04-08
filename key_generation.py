import random

p = 2
q = 7

publickeytwo = p*q
print("{} is the second part of the public key".format(publickeytwo))

coprimephi = []


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
print(coprime_n)

coprime_n_size = (p-1)*(q-1)

if len(coprime_n) == coprime_n_size:
  print("Successful check of co-prime. Elements in list is {}".format(len(coprime_n)))
else:
  print("Went wrong somewhere")

coprime_phi_n = coprime(coprime_n_size)
print(coprime_phi_n)

combinedlist = []

for i in range(len(coprime_n)):
  if coprime_n[i] in coprime_phi_n and coprime_n[i] > 1 and coprime_n[i] < coprime_n_size:
    combinedlist.append(coprime_n[i])

print(combinedlist)

publickeyone = random.choice(combinedlist)

print(publickeyone)

print("Public keys: {},{}".format(publickeyone,publickeytwo))


#Above code refers to the generation of the public key.

# print(factorsofn)
# print(coprime)


#Push to file path: Encryption/RSA_Encryption.ipynb