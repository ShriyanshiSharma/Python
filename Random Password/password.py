# Randon password generator
import random

uc = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
lc = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
nm = ['0','1','2','3','4','5','6','7','8','9']
sc = ['@','#','#','$','$','&','!']

pas = random.choice(uc) + random.choice(lc) + random.choice(nm) + random.choice(sc) + random.choice(uc) + random.choice(lc) + random.choice(nm) + random.choice(sc)

print(pas)
